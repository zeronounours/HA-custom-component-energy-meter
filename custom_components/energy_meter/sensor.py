"""Helper sensor for calculating utility costs."""
from __future__ import annotations

# Standard libraries
import logging

# Third party libraries
from homeassistant.components.energy.sensor import (
    EnergyCostSensor as BaseEnergyCostSensor,
    SourceAdapter,
)
from homeassistant.components.utility_meter import (
    CONF_METER,
    CONF_SOURCE_SENSOR,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import CONF_CONF, CONF_PRICE, CONF_PRICE_ENTITY
from .utils import conf_to_cost_sensor_id

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
            "from 'sensor:' in configuration.yaml",
        )
        return

    conf = discovery_info[CONF_CONF]
    meter = discovery_info[CONF_METER]
    source = conf[CONF_SOURCE_SENSOR]
    price = conf.get(CONF_PRICE)
    price_entity = conf.get(CONF_PRICE_ENTITY)

    async_add_entities(
        [
            EnergyCostSensor(
                source,
                price,
                price_entity,
                conf_to_cost_sensor_id(meter, conf),
            ),
        ],
    )


class EnergyCostSensor(BaseEnergyCostSensor):
    """Calculate costs incurred by consuming energy.

    This is intended as a fallback for when no specific cost sensor is
    available for the utility.
    """

    _attr_entity_registry_visible_default = True

    def __init__(
        self,
        source_entity: str,
        price: float | None,
        price_entity: str | None,
        sensor_id: tuple[str],
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
        # override the entity_id
        self._sensor_id = sensor_id
        suggested_entity_id = (
            f"sensor.{'_'.join(sensor_id)}_{self._adapter.entity_id_suffix}"
        )
        self.entity_id = suggested_entity_id

    # override the unique_id to be truely uniq
    @property
    def unique_id(self) -> str | None:
        """Return the unique ID of the sensor."""
        entity_registry = er.async_get(self.hass)

        # determine the prefix from the source entity id
        if registry_entry := entity_registry.async_get(
            self._config[self._adapter.stat_energy_key],
        ):
            source_prefix = registry_entry.id
        else:
            source_prefix = self._config[self._adapter.stat_energy_key]

        # determine the prefix from the price entity id
        if entity_id := self._config["entity_energy_price"]:
            if registry_entry := entity_registry.async_get(entity_id):
                price_prefix = registry_entry.id
            else:
                price_prefix = entity_id
        else:
            price_prefix = self._sensor_id[1]

        return f"{source_prefix}_{price_prefix}_{self._adapter.source_type}_{self._adapter.entity_id_suffix}"
