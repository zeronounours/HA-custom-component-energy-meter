"""Constants for energy_meter tests."""

# Project imports
from custom_components.energy_meter.const import DOMAIN

# A list of test cases for parametrized pytests creation
TEST_CASES = [
    #############
    # NO CONFIG #
    #############
    # No config
    {},
    #############
    # NO TARIFF #
    #############
    # No price No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
            },
        },
    },
    # Price entity No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
            },
        },
    },
    # Fixed price entity No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
            },
        },
    },
    # Price entity & fixed price No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "price": 2,
            },
        },
    },
    #############
    # 2 TARIFFS #
    #############
    # No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
            },
        },
    },
    # Price entity 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "tariffs": ["peak", "offpeak"],
            },
        },
    },
    # Fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
            },
        },
    },
    # Price entity & fixed price 2 tariffs
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
    ###################
    # 2 ENERGY_METERS #
    ###################
    # 2 meters with same entity price No tariff
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
    # 2 meters with same entity price 2 tariff
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
    # 2 meters with same price No tariff
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
    # 2 meters with same price 2 tariff
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
    # 2 meters with different entity price No tariff
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
    # 2 meters with different entity price 2 tariff
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
    # 2 meters with different price No tariff
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
    # 2 meters with different price 2 tariff
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
    # 2 meters with different prices & entity No tariff
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
    # 2 meters with different prices & entity 2 tariff
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
    ##############
    # Unique IDs #
    ##############
    # No price No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "unique_id": "energy_meter_daily_energy",
            },
        },
    },
    # Price entity No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "unique_id": "energy_meter_daily_energy",
            },
        },
    },
    # Fixed price entity No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
                "unique_id": "energy_meter_daily_energy",
            },
        },
    },
    # Price entity & fixed price No tariff
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
    # No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "unique_id": "energy_meter_daily_energy",
            },
        },
    },
    # Price entity 2 tariffs
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
    # Fixed price 2 tariffs
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
    # Price entity & fixed price 2 tariffs
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
]


CHECK_CREATED_EXPECTED_RESULTS = [
    #############
    # NO CONFIG #
    #############
    # No config
    [],
    #############
    # NO TARIFF #
    #############
    # No price No tariff
    [
        "sensor.daily_energy",
    ],
    # Price entity No tariff
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    # Fixed price entity No tariff
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    # Price entity & fixed price No tariff
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    #############
    # 2 TARIFFS #
    #############
    # No price 2 tariffs
    [
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "select.daily_energy",
    ],
    # Price entity 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # Fixed price 2 tariffs
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # Price entity & fixed price 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    ###################
    # 2 ENERGY_METERS #
    ###################
    # 2 meters with same entity price No tariff
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
        "sensor.monthly_energy",
        "sensor.monthly_energy_cost",
    ],
    # 2 meters with same entity price 2 tariff
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
    # 2 meters with same price No tariff
    [
        "sensor.energy_daily_energy_cost",
        "sensor.energy_monthly_energy_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
        "sensor.monthly_energy",
        "sensor.monthly_energy_cost",
    ],
    # 2 meters with same price 2 tariff
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
    # 2 meters with different entity price No tariff
    [
        "sensor.energy_price_cost",
        "sensor.energy_price2_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
        "sensor.monthly_energy",
        "sensor.monthly_energy_cost",
    ],
    # 2 meters with different entity price 2 tariff
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
    # 2 meters with different price No tariff
    [
        "sensor.energy_daily_energy_cost",
        "sensor.energy_monthly_energy_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
        "sensor.monthly_energy",
        "sensor.monthly_energy_cost",
    ],
    # 2 meters with different price 2 tariff
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
    # 2 meters with different prices & entity No tariff
    [
        "sensor.energy_price_cost",
        "sensor.energy_monthly_energy_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
        "sensor.monthly_energy",
        "sensor.monthly_energy_cost",
    ],
    # 2 meters with different prices & entity 2 tariff
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
    ##############
    # Unique IDs #
    ##############
    # No price No tariff
    [
        "sensor.daily_energy",
    ],
    # Price entity No tariff
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    # Fixed price entity No tariff
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    # Price entity & fixed price No tariff
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    # No price 2 tariffs
    [
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "select.daily_energy",
    ],
    # Price entity 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # Fixed price 2 tariffs
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # Price entity & fixed price 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
]
