"""Support for tracking consumption & cost."""
# Standard libraries
import logging

# Third party libraries
from homeassistant.components.energy.sensor import (
    SOURCE_ADAPTERS,
    SourceAdapter,
)
from homeassistant.components.select import DOMAIN as SELECT_DOMAIN
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.components.utility_meter import (
    CONF_METER,
    CONF_SOURCE_SENSOR,
    CONF_TARIFF,
    CONF_TARIFF_ENTITY,
    CONF_TARIFFS,
    DATA_TARIFF_SENSORS,
    DATA_UTILITY,
    DOMAIN as UM_DOMAIN,
    METER_CONFIG_SCHEMA,
)
from homeassistant.const import CONF_NAME, CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType
import voluptuous as vol

from .const import (
    CONF_ADAPTER,
    CONF_CONF,
    CONF_PRICE,
    CONF_PRICE_ENTITY,
    CONF_SOURCE_TYPE,
    CONF_UTILITY_METER,
    DATA_ENERGY_METER,
    DOMAIN,
)
from .utils import conf_to_cost_sensor_id

_LOGGER = logging.getLogger(__name__)


SOURCE_TYPE_TO_SOURCE_ADAPTER = {
    "from_grid": ("grid", "flow_from"),
    "to_grid": ("grid", "flow_to"),
    "gas": ("gas", None),
    "water": ("water", None),
}


# update the default schema w/ new options
ENERGY_METER_CONFIG_SCHEMA = vol.Schema(
    vol.All(
        vol.Schema(METER_CONFIG_SCHEMA.schema.validators[0]).extend(
            {
                vol.Optional(CONF_PRICE): cv.positive_float,
                vol.Optional(CONF_PRICE_ENTITY): cv.entity_id,
                vol.Optional(CONF_UTILITY_METER): cv.boolean,
                vol.Optional(CONF_SOURCE_TYPE): vol.Any(
                    *SOURCE_TYPE_TO_SOURCE_ADAPTER.keys(),
                ),
            },
        ),
        *METER_CONFIG_SCHEMA.schema.validators[1:],
    ),
)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema({cv.slug: ENERGY_METER_CONFIG_SCHEMA}),
    },
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up an Energy Meter."""
    hass.data[DATA_ENERGY_METER] = {}

    if DOMAIN not in config:
        return True

    for meter, conf in config[DOMAIN].items():
        _LOGGER.debug("Setup %s.%s", DOMAIN, meter)

        create_utility_meter = conf.get(CONF_UTILITY_METER, True)

        if create_utility_meter:
            # create the select entity
            select_entity = await setup_utility_meter_select(hass, config, meter, conf)

            # Create the utility_meters for the energy
            um_conf = conf.copy()
            await setup_utility_meter_sensors(
                hass,
                config,
                meter,
                um_conf,
                select_entity,
            )

        # Create the sensor & utility_meters for the energy cost
        if conf.get(CONF_PRICE) is not None or conf.get(CONF_PRICE_ENTITY) is not None:
            # cost sensor
            # Only create a new one if none have been created before.
            # The creation of sensors is done as following:
            #   - for fixed price, cost sensor is bound to the meter id
            #   - for entity price, cost sensor is bound to the entity
            #     price id
            sensor_id = conf_to_cost_sensor_id(meter, conf)
            if (adapter := get_energy_cost_sensor_adapter(conf)) is None:
                # stop here as we cannot create a cost sensor
                continue
            cache_key = (sensor_id, adapter.entity_id_suffix)
            if cache_key in hass.data[DATA_ENERGY_METER]:
                cost_entity = hass.data[DATA_ENERGY_METER][cache_key]
            else:
                cost_entity = await setup_energy_cost_sensor(
                    hass,
                    config,
                    meter,
                    conf,
                    adapter,
                )
                hass.data[DATA_ENERGY_METER][cache_key] = cost_entity

            if create_utility_meter:
                # utility_meter
                um_conf = conf.copy()
                um_conf[CONF_SOURCE_SENSOR] = cost_entity

                # force a friendly name from the cost entity
                name = um_conf.get(CONF_NAME)
                if not name:
                    name = meter.replace("_", " ")
                um_conf[CONF_NAME] = f"{name} {adapter.name_suffix}"

                # Prevent the reuse of the same unique_id as the
                # utility_meter sensors
                if um_conf.get(CONF_UNIQUE_ID):
                    um_conf[
                        CONF_UNIQUE_ID
                    ] = f"{um_conf[CONF_UNIQUE_ID]}_{adapter.entity_id_suffix}"

                await setup_utility_meter_sensors(
                    hass,
                    config,
                    f"{meter}_{adapter.entity_id_suffix}",
                    um_conf,
                    select_entity,
                )

    return True


async def setup_utility_meter_select(
    hass: HomeAssistant,
    config: ConfigType,
    meter: str,
    conf: dict,
) -> str:
    """Create the select for utility_meters."""
    # Only create the select if multiple tariffs are created
    if not conf.get(CONF_TARIFFS):
        _LOGGER.debug("Setup %s.%s: skip utility_meter select entity", DOMAIN, meter)
        return ""

    _LOGGER.debug("Setup %s.%s: create utility_meter select entity", DOMAIN, meter)
    # create tariff selection
    hass.async_create_task(
        discovery.async_load_platform(
            hass,
            SELECT_DOMAIN,
            UM_DOMAIN,
            {CONF_METER: meter, CONF_TARIFFS: conf[CONF_TARIFFS]},
            config,
        ),
    )

    # create the select entity ID the same way utility_meter does
    return f"{SELECT_DOMAIN}.{meter}"


async def setup_utility_meter_sensors(
    hass: HomeAssistant,
    config: ConfigType,
    meter: str,
    conf: dict,
    select_entity: str,
):
    """Create the utility_meter sensors linked to the select entity."""
    # use of copy of the conf to keep data of energy & cost separate
    hass.data[DATA_UTILITY][meter] = conf.copy()
    hass.data[DATA_UTILITY][meter][DATA_TARIFF_SENSORS] = []

    if not conf.get(CONF_TARIFFS):
        _LOGGER.debug(
            "Setup %s.%s: create a single utility_meter sensor",
            DOMAIN,
            meter,
        )
        # only one entity is required
        hass.async_create_task(
            discovery.async_load_platform(
                hass,
                SENSOR_DOMAIN,
                UM_DOMAIN,
                {meter: {CONF_METER: meter}},
                config,
            ),
        )
    else:
        # Indicate the select entity for the tariff selection
        hass.data[DATA_UTILITY][meter][CONF_TARIFF_ENTITY] = select_entity

        # add one meter for each tariff for energy
        tariff_confs = {}
        for tariff in conf[CONF_TARIFFS]:
            name = f"{meter} {tariff}"
            tariff_confs[name] = {
                CONF_METER: meter,
                CONF_TARIFF: tariff,
            }

        _LOGGER.debug(
            "Setup %s.%s: create utility_meter sensors for tariffs %s",
            DOMAIN,
            meter,
            conf[CONF_TARIFFS],
        )
        hass.async_create_task(
            discovery.async_load_platform(
                hass,
                SENSOR_DOMAIN,
                UM_DOMAIN,
                tariff_confs,
                config,
            ),
        )


async def setup_energy_cost_sensor(
    hass: HomeAssistant,
    config: ConfigType,
    meter: str,
    meter_conf: dict,
    adapter: SourceAdapter,
):
    """Create a cost sensor to follow an energy sensor."""
    _LOGGER.debug(
        "Setup %s: create energy cost sensor for entity %s",
        DOMAIN,
        meter_conf[CONF_SOURCE_SENSOR],
    )
    hass.async_create_task(
        discovery.async_load_platform(
            hass,
            SENSOR_DOMAIN,
            DOMAIN,
            {CONF_METER: meter, CONF_CONF: meter_conf, CONF_ADAPTER: adapter},
            config,
        ),
    )
    # return the entity id
    return (
        f"sensor."
        f"{'_'.join(conf_to_cost_sensor_id(meter, meter_conf))}"
        f"_{adapter.entity_id_suffix}"
    )


def get_energy_cost_sensor_adapter(conf: dict):
    """Resolve the SourceAdapter from config."""
    # resolve source adapter from source_type
    source_type = conf.get(CONF_SOURCE_TYPE, "from_grid")
    _LOGGER.debug("Setup %s: setup energy cost sensor of type %s", DOMAIN, source_type)

    if source_type not in SOURCE_TYPE_TO_SOURCE_ADAPTER:
        # should never happen if config validation is correctly set
        _LOGGER.error(
            "Setup %s: Unknown source type configured: %s",
            DOMAIN,
            source_type,
        )
        return None

    source_adapter = SOURCE_TYPE_TO_SOURCE_ADAPTER[source_type]

    for adapter in SOURCE_ADAPTERS:
        # find the right
        if (adapter.source_type, adapter.flow_type) == source_adapter:
            return adapter
    # should not happened unless builtin adapter changes
    _LOGGER.error(
        "Setup %s: Failed to find an appropriate source adapter for type %s",
        DOMAIN,
        source_type,
    )
    return None
