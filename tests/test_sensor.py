"""Test energy_meter sensor."""
# Standard libraries
from unittest.mock import patch

# Third party libraries
from homeassistant.setup import async_setup_component


async def test_direct_setup_exception(hass, config):
    """Test direct setup of the sensor raise an error."""
    with patch("custom_components.energy_meter.sensor._LOGGER") as logger:
        await async_setup_component(
            hass,
            "sensor",
            config | {"sensor": [{"platform": "energy_meter"}]},
        )
        await hass.async_block_till_done()
        # assert an error is logged
        logger.error.assert_called()
        # no sensor created
        assert len(hass.states.async_entity_ids()) == 0
