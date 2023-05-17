"""Support for tracking consumption & price over given periods of time."""
import logging

import voluptuous as vol

from homeassistant.const import CONF_NAME
from homeassistant.components.select import DOMAIN as SELECT_DOMAIN
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.components.utility_meter import (
    CONF_METER,
    CONF_SOURCE_SENSOR,
    CONF_TARIFF,
    CONF_TARIFFS,
    CONF_TARIFF_ENTITY,
    DATA_TARIFF_SENSORS,
    DATA_UTILITY,
    DOMAIN as UM_DOMAIN,
    METER_CONFIG_SCHEMA,
)
from homeassistant.core import HomeAssistant, split_entity_id
from homeassistant.helpers import discovery
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.typing import ConfigType

from .const import (
    CONF_CONF,
    CONF_PRICE,
    CONF_PRICE_ENTITY,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)


# update the default schema w/ new options
ENERGY_METER_CONFIG_SCHEMA = vol.Schema(
    vol.All(
        vol.Schema(METER_CONFIG_SCHEMA.schema.validators[0]).extend(
            {
                vol.Optional(CONF_PRICE): cv.small_float,
                vol.Optional(CONF_PRICE_ENTITY): cv.entity_id,
            }
        ),
        *METER_CONFIG_SCHEMA.schema.validators[1:],
    )
)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema({cv.slug: ENERGY_METER_CONFIG_SCHEMA}),
    },
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up an Energy Meter."""
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
            cost_entity = await setup_energy_cost_sensor(hass, config, conf)

            # utility_meter
            um_conf = conf.copy()
            um_conf[CONF_SOURCE_SENSOR] = cost_entity
            # force a friendly name from the cost entity
            cost_state = hass.states.get(cost_entity)
            if cost_state:
                name = cost_state.name
            else:
                name = split_entity_id(cost_entity)[0].replace("_", " ")
            um_conf[CONF_NAME] = name

            await setup_utility_meter_sensors(
                hass, config, f"{meter}_cost", um_conf, select_entity
            )

    return True


async def setup_utility_meter_select(
    hass: HomeAssistant, config: ConfigType, meter: str, conf: dict
) -> str:
    # Only create the select if multiple tariffs are created
    if not conf[CONF_TARIFFS]:
        return ""

    # create tariff selection
    hass.async_create_task(
        discovery.async_load_platform(
            hass,
            SELECT_DOMAIN,
            UM_DOMAIN,
            {CONF_METER: meter, CONF_TARIFFS: conf[CONF_TARIFFS]},
            config,
        )
    )

    # create the select entity ID the same way utility_meter does
    return "{}.{}".format(SELECT_DOMAIN, meter)


async def setup_utility_meter_sensors(
    hass: HomeAssistant, config: ConfigType, meter: str, conf: dict, select_entity: str
):
    # use of copy of the conf to keep data of energy & cost separate
    hass.data[DATA_UTILITY][meter] = conf.copy()
    hass.data[DATA_UTILITY][meter][DATA_TARIFF_SENSORS] = []

    if not conf[CONF_TARIFFS]:
        # only one entity is required
        hass.async_create_task(
            discovery.async_load_platform(
                hass,
                SENSOR_DOMAIN,
                UM_DOMAIN,
                {meter: {CONF_METER: meter}},
                config,
            )
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

            hass.async_create_task(
                discovery.async_load_platform(
                    hass, SENSOR_DOMAIN, UM_DOMAIN, tariff_confs, config
                )
            )


async def setup_energy_cost_sensor(
    hass: HomeAssistant, config: ConfigType, meter_conf: dict
):
    hass.async_create_task(
        discovery.async_load_platform(
            hass,
            SENSOR_DOMAIN,
            DOMAIN,
            {CONF_CONF: meter_conf},
            config,
        )
    )
    return "{}_cost".format(meter_conf[CONF_SOURCE_SENSOR])
