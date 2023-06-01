"""Support for tracking consumption & cost."""
# Standard libraries
import logging

# Third party libraries
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
    CONF_CONF,
    CONF_PRICE,
    CONF_PRICE_ENTITY,
    DATA_ENERGY_METER,
    DOMAIN,
)
from .utils import conf_to_cost_sensor_id

_LOGGER = logging.getLogger(__name__)


# update the default schema w/ new options
ENERGY_METER_CONFIG_SCHEMA = vol.Schema(
    vol.All(
        vol.Schema(METER_CONFIG_SCHEMA.schema.validators[0]).extend(
            {
                vol.Optional(CONF_PRICE): cv.positive_float,
                vol.Optional(CONF_PRICE_ENTITY): cv.entity_id,
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

        # create the select entity
        select_entity = await setup_utility_meter_select(hass, config, meter, conf)

        # Create the utility_meters for the energy
        um_conf = conf.copy()
        await setup_utility_meter_sensors(hass, config, meter, um_conf, select_entity)

        # Create the sensor & utility_meters for the energy cost
        if conf.get(CONF_PRICE) is not None or conf.get(CONF_PRICE_ENTITY) is not None:
            # cost sensor
            # Only create a new one if none have been created before.
            # The creation of sensors is done as following:
            #   - for fixed price, cost sensor is bound to the meter id
            #   - for entity price, cost sensor is bound to the entity
            #     price id
            cache_key = conf_to_cost_sensor_id(meter, conf)
            if cache_key in hass.data[DATA_ENERGY_METER]:
                cost_entity = hass.data[DATA_ENERGY_METER][cache_key]
            else:
                cost_entity = await setup_energy_cost_sensor(hass, config, meter, conf)
                hass.data[DATA_ENERGY_METER][cache_key] = cost_entity

            # utility_meter
            um_conf = conf.copy()
            um_conf[CONF_SOURCE_SENSOR] = cost_entity

            # force a friendly name from the cost entity
            name = um_conf.get(CONF_NAME)
            if not name:
                name = meter.replace("_", " ")
            um_conf[CONF_NAME] = f"{name} Cost"

            # Prevent the reuse of the same unique_id as the
            # utility_meter sensors
            if um_conf.get(CONF_UNIQUE_ID):
                um_conf[CONF_UNIQUE_ID] = f"{um_conf[CONF_UNIQUE_ID]}_cost"

            await setup_utility_meter_sensors(
                hass,
                config,
                f"{meter}_cost",
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
            {CONF_METER: meter, CONF_CONF: meter_conf},
            config,
        ),
    )
    return f"sensor.{'_'.join(conf_to_cost_sensor_id(meter, meter_conf))}_cost"
