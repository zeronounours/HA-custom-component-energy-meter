"""Helper sensor for calculating utility costs."""
from __future__ import annotations

import logging
from typing import Optional

from homeassistant.components.energy.sensor import (
    EnergyCostSensor as BaseEnergyCostSensor,
    SourceAdapter,
)
from homeassistant.components.utility_meter import CONF_SOURCE_SENSOR
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import CONF_CONF, CONF_PRICE, CONF_PRICE_ENTITY


_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the cost sensor."""
    if discovery_info is None:
        _LOGGER.error(
            "This platform is not available to configure "
            "from 'sensor:' in configuration.yaml"
        )
        return

    conf = discovery_info[CONF_CONF]
    source = conf[CONF_SOURCE_SENSOR]
    price = conf.get(CONF_PRICE)
    price_entity = conf.get(CONF_PRICE_ENTITY)

    async_add_entities([EnergyCostSensor(source, price, price_entity)])


class EnergyCostSensor(BaseEnergyCostSensor):
    """Calculate costs incurred by consuming energy.

    This is intended as a fallback for when no specific cost sensor is
    available for the utility.
    """

    _attr_entity_registry_visible_default = True

    def __init__(
        self,
        source_entity: str,
        price: Optional[float],
        price_entity: Optional[str],
    ) -> None:
        """Initialize the sensor."""
        super().__init__(
            SourceAdapter(
                source_type="grid",
                flow_type="flow_from",
                stat_energy_key="stat_energy_from",
                total_money_key="stat_cost",
                name_suffix="Cost",
                entity_id_suffix="cost",
            ),
            {
                "stat_energy_from": source_entity,
                "stat_cost": None,
                "entity_energy_price": price_entity,
                "number_energy_price": price,
            },
        )
