"""Test energy_meter setup process."""

# Third party libraries
from homeassistant.setup import async_setup_component
import pytest

# Project imports
from custom_components.energy_meter.const import DOMAIN


@pytest.mark.parametrize(
    ("config", "created_sensors"),
    [
        #############
        # NO CONFIG #
        #############
        # No config
        (
            {},
            [],
        ),
        #############
        # NO TARIFF #
        #############
        # No price No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                    },
                },
            },
            [
                "sensor.daily_energy",
            ],
        ),
        # Price entity No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
            ],
        ),
        # Fixed price entity No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price": 2,
                    },
                },
            },
            [
                "sensor.energy_daily_energy_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
            ],
        ),
        # Price entity & fixed price No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "price": 2,
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
            ],
        ),
        #############
        # 2 TARIFFS #
        #############
        # No price 2 tariffs
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "tariffs": ["peak", "offpeak"],
                    },
                },
            },
            [
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "select.daily_energy",
            ],
        ),
        # Price entity 2 tariffs
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "tariffs": ["peak", "offpeak"],
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
            ],
        ),
        # Fixed price 2 tariffs
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price": 2,
                        "tariffs": ["peak", "offpeak"],
                    },
                },
            },
            [
                "sensor.energy_daily_energy_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
            ],
        ),
        # Price entity & fixed price 2 tariffs
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "price": 2,
                        "tariffs": ["peak", "offpeak"],
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
            ],
        ),
        ###################
        # 2 ENERGY_METERS #
        ###################
        # 2 meters with same entity price No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                    },
                    "monthly_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
                "sensor.monthly_energy",
                "sensor.monthly_energy_cost",
            ],
        ),
        # 2 meters with same entity price 2 tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "tariffs": ["peak", "offpeak"],
                    },
                    "monthly_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "tariffs": ["peak", "offpeak"],
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
                "sensor.monthly_energy_peak",
                "sensor.monthly_energy_offpeak",
                "sensor.monthly_energy_cost_peak",
                "sensor.monthly_energy_cost_offpeak",
                "select.monthly_energy",
            ],
        ),
        # 2 meters with same price No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price": 2,
                    },
                    "monthly_energy": {
                        "source": "sensor.energy",
                        "price": 2,
                    },
                },
            },
            [
                "sensor.energy_daily_energy_cost",
                "sensor.energy_monthly_energy_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
                "sensor.monthly_energy",
                "sensor.monthly_energy_cost",
            ],
        ),
        # 2 meters with same price 2 tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price": 2,
                        "tariffs": ["peak", "offpeak"],
                    },
                    "monthly_energy": {
                        "source": "sensor.energy",
                        "price": 2,
                        "tariffs": ["peak", "offpeak"],
                    },
                },
            },
            [
                "sensor.energy_daily_energy_cost",
                "sensor.energy_monthly_energy_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
                "sensor.monthly_energy_peak",
                "sensor.monthly_energy_offpeak",
                "sensor.monthly_energy_cost_peak",
                "sensor.monthly_energy_cost_offpeak",
                "select.monthly_energy",
            ],
        ),
        # 2 meters with different entity price No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                    },
                    "monthly_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price2",
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.energy_price2_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
                "sensor.monthly_energy",
                "sensor.monthly_energy_cost",
            ],
        ),
        # 2 meters with different entity price 2 tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "tariffs": ["peak", "offpeak"],
                    },
                    "monthly_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price2",
                        "tariffs": ["peak", "offpeak"],
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.energy_price2_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
                "sensor.monthly_energy_peak",
                "sensor.monthly_energy_offpeak",
                "sensor.monthly_energy_cost_peak",
                "sensor.monthly_energy_cost_offpeak",
                "select.monthly_energy",
            ],
        ),
        # 2 meters with different price No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price": 2,
                    },
                    "monthly_energy": {
                        "source": "sensor.energy",
                        "price": 3,
                    },
                },
            },
            [
                "sensor.energy_daily_energy_cost",
                "sensor.energy_monthly_energy_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
                "sensor.monthly_energy",
                "sensor.monthly_energy_cost",
            ],
        ),
        # 2 meters with different price 2 tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price": 2,
                        "tariffs": ["peak", "offpeak"],
                    },
                    "monthly_energy": {
                        "source": "sensor.energy",
                        "price": 3,
                        "tariffs": ["peak", "offpeak"],
                    },
                },
            },
            [
                "sensor.energy_daily_energy_cost",
                "sensor.energy_monthly_energy_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
                "sensor.monthly_energy_peak",
                "sensor.monthly_energy_offpeak",
                "sensor.monthly_energy_cost_peak",
                "sensor.monthly_energy_cost_offpeak",
                "select.monthly_energy",
            ],
        ),
        # 2 meters with different prices & entity No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                    },
                    "monthly_energy": {
                        "source": "sensor.energy",
                        "price": 3,
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.energy_monthly_energy_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
                "sensor.monthly_energy",
                "sensor.monthly_energy_cost",
            ],
        ),
        # 2 meters with different prices & entity 2 tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "tariffs": ["peak", "offpeak"],
                    },
                    "monthly_energy": {
                        "source": "sensor.energy",
                        "price": 3,
                        "tariffs": ["peak", "offpeak"],
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.energy_monthly_energy_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
                "sensor.monthly_energy_peak",
                "sensor.monthly_energy_offpeak",
                "sensor.monthly_energy_cost_peak",
                "sensor.monthly_energy_cost_offpeak",
                "select.monthly_energy",
            ],
        ),
        ##############
        # Unique IDs #
        ##############
        # No price No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "unique_id": "energy_meter_daily_energy",
                    },
                },
            },
            [
                "sensor.daily_energy",
            ],
        ),
        # Price entity No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "unique_id": "energy_meter_daily_energy",
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
            ],
        ),
        # Fixed price entity No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price": 2,
                        "unique_id": "energy_meter_daily_energy",
                    },
                },
            },
            [
                "sensor.energy_daily_energy_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
            ],
        ),
        # Price entity & fixed price No tariff
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "price": 2,
                        "unique_id": "energy_meter_daily_energy",
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.daily_energy",
                "sensor.daily_energy_cost",
            ],
        ),
        # No price 2 tariffs
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "tariffs": ["peak", "offpeak"],
                        "unique_id": "energy_meter_daily_energy",
                    },
                },
            },
            [
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "select.daily_energy",
            ],
        ),
        # Price entity 2 tariffs
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "tariffs": ["peak", "offpeak"],
                        "unique_id": "energy_meter_daily_energy",
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
            ],
        ),
        # Fixed price 2 tariffs
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price": 2,
                        "tariffs": ["peak", "offpeak"],
                        "unique_id": "energy_meter_daily_energy",
                    },
                },
            },
            [
                "sensor.energy_daily_energy_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
            ],
        ),
        # Price entity & fixed price 2 tariffs
        (
            {
                DOMAIN: {
                    "daily_energy": {
                        "source": "sensor.energy",
                        "price_entity": "sensor.price",
                        "price": 2,
                        "tariffs": ["peak", "offpeak"],
                        "unique_id": "energy_meter_daily_energy",
                    },
                },
            },
            [
                "sensor.energy_price_cost",
                "sensor.daily_energy_peak",
                "sensor.daily_energy_offpeak",
                "sensor.daily_energy_cost_peak",
                "sensor.daily_energy_cost_offpeak",
                "select.daily_energy",
            ],
        ),
    ],
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


#
#    # ensure no error where logged
#    for record in caplog.records:
#        assert record.levelno < logging.ERROR
