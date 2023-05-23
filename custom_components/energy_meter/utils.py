"""Helper functions for the rest of the modules."""

# Third party libraries
from homeassistant.components.utility_meter import CONF_SOURCE_SENSOR
from homeassistant.core import split_entity_id
from homeassistant.helpers.typing import ConfigType

from .const import CONF_PRICE_ENTITY


def conf_to_cost_sensor_id(meter: str, config: ConfigType) -> tuple[str]:
    """Generate the entity id of the cost sensor.

    The ID of sensors is bound to the source entity and:
      - for fixed price, the meter id
      - for entity price, to the entity price id

    """
    energy_source = split_entity_id(config[CONF_SOURCE_SENSOR])[1]
    price_entity = config.get(CONF_PRICE_ENTITY)
    if price_entity:
        return (energy_source, split_entity_id(price_entity)[1])
    return (energy_source, meter)
