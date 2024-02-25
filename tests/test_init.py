"""Test energy_meter setup process."""
# Standard libraries
from unittest.mock import patch

# Third party libraries
from homeassistant.components.utility_meter.sensor import ATTR_SOURCE_ID
from homeassistant.setup import async_setup_component
import pytest

# Project imports
from custom_components.energy_meter import get_energy_cost_sensor_adapter
from custom_components.energy_meter.const import CONF_SOURCE_TYPE, DOMAIN
from tests.const import (
    CHECK_CREATED_EXPECTED_RESULTS,
    CHECK_UM_SOURCES_EXPECTED_RESULTS,
    TEST_CASES,
)
from tests.utils import assert_logger


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
    assert await async_setup_component(hass, DOMAIN, config) is True, "Failed to setup"
    await hass.async_block_till_done()

    # asserts the created sensors
    entities = hass.states.async_entity_ids()
    for sensor in created_sensors:
        assert sensor in entities, "Unexpected sensor name"

    # add constant for sensor.energy & prices
    assert (
        len(entities) == len(created_sensors) + 3
    ), "Invalid number of created sensors"


@pytest.mark.parametrize(
    ("config", "um_sources"),
    zip(TEST_CASES, CHECK_UM_SOURCES_EXPECTED_RESULTS),
    indirect=("config",),
)
async def test_setup_and_utility_meter_sources(hass, config, um_sources):
    """Test the setup and tests created sensors."""
    # define the current energy & price
    hass.states.async_set("sensor.energy", 100)
    hass.states.async_set("sensor.price", 2)
    hass.states.async_set("sensor.price2", 3)
    await hass.async_block_till_done()

    # setup the integration
    assert await async_setup_component(hass, DOMAIN, config) is True, "Failed to setup"
    await hass.async_block_till_done()

    # asserts the created sensors
    for utility_meter, source in um_sources.items():
        assert (
            state := hass.states.get(utility_meter)
        ) is not None, "No utility meter found"
        assert (
            state.attributes[ATTR_SOURCE_ID] == source
        ), "Invalid tracked entity of utility meter"


@pytest.mark.parametrize(
    ("em_source_type", "adapter_source_type", "adapter_flow_type"),
    [
        (None, "grid", "flow_from"),
        ("from_grid", "grid", "flow_from"),
        ("to_grid", "grid", "flow_to"),
        ("gas", "gas", None),
        ("water", "water", None),
    ],
)
async def test_valid_source_adapter_resolution(
    em_source_type,
    adapter_source_type,
    adapter_flow_type,
):
    """Test resolution of the SourceAdapter."""
    # define the config and get the adapter
    conf = {CONF_SOURCE_TYPE: em_source_type} if em_source_type else {}
    adapter = get_energy_cost_sensor_adapter(conf)

    # assert expected adapter
    assert adapter is not None, "Adapter not defined"
    assert (
        adapter.source_type == adapter_source_type
    ), "Adapter source_type is not the expected one"
    assert (
        adapter.flow_type == adapter_flow_type
    ), "Adapter flow_type is not the expected one"


async def test_unknown_source_type_adapter_resolution():
    """Test errors on unknown source_type."""
    with patch("custom_components.energy_meter._LOGGER") as logger:
        # define the config and get the adapter
        conf = {CONF_SOURCE_TYPE: "invalid_value"}
        adapter = get_energy_cost_sensor_adapter(conf)

        # assert expected adapter
        assert adapter is None, "Adapter defined"
        # assert an error is logged
        assert_logger(logger, "error")


async def test_failed_adapter_resolution():
    """Test errors on failed adapter resolution.

    Ensure an error is raised if builtin AdapterSources change and we
    cannot find one anymore.
    """
    # patch source_type to SourceAdapter mapping
    with patch(
        "custom_components.energy_meter.SOURCE_TYPE_TO_SOURCE_ADAPTER",
        new={
            "test_source": ("unknown_type", "unknown_flow"),
        },
    ), patch("custom_components.energy_meter._LOGGER") as logger:
        # define the config and get the adapter
        conf = {CONF_SOURCE_TYPE: "test_source"}
        adapter = get_energy_cost_sensor_adapter(conf)

        # assert expected adapter
        assert adapter is None, "Adapter defined"
        # assert an error is logged
        assert_logger(logger, "error")


async def test_creation_with_invalid_adapter(hass, config):
    """Test errors creation of meter with invalid adapter."""
    # define the current energy & price
    hass.states.async_set("sensor.energy", 100)
    hass.states.async_set("sensor.price", 2)
    await hass.async_block_till_done()

    # patch source_type to SourceAdapter mapping
    with patch(
        "custom_components.energy_meter.SOURCE_TYPE_TO_SOURCE_ADAPTER",
        new={
            "to_grid": ("unknown_type", "unknown_flow"),
        },
    ), patch("custom_components.energy_meter._LOGGER") as logger:
        # setup the integration
        assert (
            await async_setup_component(
                hass,
                DOMAIN,
                config
                | {
                    DOMAIN: {
                        "daily_energy": {
                            "source": "sensor.energy",
                            "price_entity": "sensor.price",
                            "tariffs": ["peak", "offpeak"],
                            "source_type": "to_grid",
                        },
                    },
                },
            )
            is True
        ), "Failed to setup"
        await hass.async_block_till_done()

        # asserts the created sensors
        entities = hass.states.async_entity_ids()
        created_sensors = [
            "sensor.daily_energy_peak",
            "sensor.daily_energy_offpeak",
            "select.daily_energy",
            # the cost entities should not be created and an error
            # should be logged
        ]
        for sensor in created_sensors:
            assert sensor in entities, "Unexpected sensor name"
        # add constant for sensor.energy & prices
        assert (
            len(entities) == len(created_sensors) + 2
        ), "Invalid number of created sensors"
        # assert an error is logged
        assert_logger(logger, "error")
