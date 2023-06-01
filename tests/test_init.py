"""Test energy_meter setup process."""

# Third party libraries
from homeassistant.setup import async_setup_component
import pytest

# Project imports
from custom_components.energy_meter.const import DOMAIN
from tests.const import CHECK_CREATED_EXPECTED_RESULTS, TEST_CASES


@pytest.mark.parametrize(
    ("config", "created_sensors"),
    zip(TEST_CASES, CHECK_CREATED_EXPECTED_RESULTS),
    indirect=("config",),
)
async def test_setup_and_check_created_sensors(hass, config, created_sensors):
    """Test the setup and tests created sensors."""
    # define the current energy & price
    hass.states.async_set("sensor.energy", 100)
    hass.states.async_set("sensor.price", 2)
    hass.states.async_set("sensor.price2", 3)
    await hass.async_block_till_done()

    # setup the integration
    assert await async_setup_component(hass, DOMAIN, config) is True
    await hass.async_block_till_done()

    # asserts the created sensors
    entities = hass.states.async_entity_ids()
    for sensor in created_sensors:
        assert sensor in entities
    assert len(entities) == len(created_sensors) + 3  # add 2 for sensor.energy & prices
