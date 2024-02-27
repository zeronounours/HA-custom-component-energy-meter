"""Constants for energy_meter tests."""

# Project imports
from custom_components.energy_meter.const import DOMAIN

# A list of test cases for parametrized pytests creation
TEST_CASES = [
    #############
    # NO CONFIG #
    #############
    # 0 - No config
    {},
    #############
    # NO TARIFF #
    #############
    # 1 - No price No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
            },
        },
    },
    # 2 - Price entity No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
            },
        },
    },
    # 3 - Fixed price entity No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
            },
        },
    },
    # 4 - Price entity & fixed price No tariff
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
    # 5 - No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
            },
        },
    },
    # 6 - Price entity 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "tariffs": ["peak", "offpeak"],
            },
        },
    },
    # 7 - Fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
            },
        },
    },
    # 8 - Price entity & fixed price 2 tariffs
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
    # 9 - 2 meters with same entity price No tariff
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
    # 10 - 2 meters with same entity price 2 tariff
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
    # 11 - 2 meters with same price No tariff
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
    # 12 - 2 meters with same price 2 tariff
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
    # 13 - 2 meters with different entity price No tariff
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
    # 14 - 2 meters with different entity price 2 tariff
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
    # 15 - 2 meters with different price No tariff
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
    # 16 - 2 meters with different price 2 tariff
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
    # 17 - 2 meters with different prices & entity No tariff
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
    # 18 - 2 meters with different prices & entity 2 tariff
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
    # 19 - No price No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "unique_id": "energy_meter_daily_energy",
            },
        },
    },
    # 20 - Price entity No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "unique_id": "energy_meter_daily_energy",
            },
        },
    },
    # 21 - Fixed price entity No tariff
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
                "unique_id": "energy_meter_daily_energy",
            },
        },
    },
    # 22 - Price entity & fixed price No tariff
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
    # 23 - No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "unique_id": "energy_meter_daily_energy",
            },
        },
    },
    # 24 - Price entity 2 tariffs
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
    # 25 - Fixed price 2 tariffs
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
    # 26 - Price entity & fixed price 2 tariffs
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
    ################################
    # Create utility meter defined #
    ################################
    # 27 - No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "create_utility_meter": "yes",
            },
        },
    },
    # 28 - Price entity 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "tariffs": ["peak", "offpeak"],
                "create_utility_meter": "yes",
            },
        },
    },
    # 29 - Fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "create_utility_meter": "yes",
            },
        },
    },
    # 30 - Price entity & fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "create_utility_meter": "yes",
            },
        },
    },
    ##################################
    # Create only Energy cost sensor #
    ##################################
    # 31 - No price No tariff
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "create_utility_meter": "no",
            },
        },
    },
    # 32 - Price entity No tariff
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "create_utility_meter": "no",
            },
        },
    },
    # 33 - Fixed price entity No tariff
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "price": 2,
                "create_utility_meter": "no",
            },
        },
    },
    # 34 - Price entity & fixed price No tariff
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "price": 2,
                "create_utility_meter": "no",
            },
        },
    },
    # 35 - No price 2 tariffs
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "create_utility_meter": "no",
            },
        },
    },
    # 36 - Price entity 2 tariffs
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "tariffs": ["peak", "offpeak"],
                "create_utility_meter": "no",
            },
        },
    },
    # 37 - Fixed price 2 tariffs
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "create_utility_meter": "no",
            },
        },
    },
    # 38 - Price entity & fixed price 2 tariffs
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "create_utility_meter": "no",
            },
        },
    },
    #########################
    # from_grid source_type #
    #########################
    # 39 - No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "source_type": "from_grid",
            },
        },
    },
    # 40 - Price entity 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "tariffs": ["peak", "offpeak"],
                "source_type": "from_grid",
            },
        },
    },
    # 41 - Fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "source_type": "from_grid",
            },
        },
    },
    # 42 - Price entity & fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "source_type": "from_grid",
            },
        },
    },
    #######################
    # to_grid source_type #
    #######################
    # 43 - No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "source_type": "to_grid",
            },
        },
    },
    # 44 - Price entity 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "tariffs": ["peak", "offpeak"],
                "source_type": "to_grid",
            },
        },
    },
    # 45 - Fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "source_type": "to_grid",
            },
        },
    },
    # 46 - Price entity & fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "source_type": "to_grid",
            },
        },
    },
    ###################
    # gas source_type #
    ###################
    # 47 - No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "source_type": "gas",
            },
        },
    },
    # 48 - Price entity 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "tariffs": ["peak", "offpeak"],
                "source_type": "gas",
            },
        },
    },
    # 49 - Fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "source_type": "gas",
            },
        },
    },
    # 50 - Price entity & fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "source_type": "gas",
            },
        },
    },
    #####################
    # water source_type #
    #####################
    # 51 - No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "source_type": "water",
            },
        },
    },
    # 52 - Price entity 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "tariffs": ["peak", "offpeak"],
                "source_type": "water",
            },
        },
    },
    # 53 - Fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "source_type": "water",
            },
        },
    },
    # 54 - Price entity & fixed price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "price": 2,
                "tariffs": ["peak", "offpeak"],
                "source_type": "water",
            },
        },
    },
]


CHECK_CREATED_EXPECTED_RESULTS = [
    #############
    # NO CONFIG #
    #############
    # 0 - No config
    [],
    #############
    # NO TARIFF #
    #############
    # 1 - No price No tariff
    [
        "sensor.daily_energy",
    ],
    # 2 - Price entity No tariff
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    # 3 - Fixed price entity No tariff
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    # 4 - Price entity & fixed price No tariff
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    #############
    # 2 TARIFFS #
    #############
    # 5 - No price 2 tariffs
    [
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "select.daily_energy",
    ],
    # 6 - Price entity 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 7 - Fixed price 2 tariffs
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 8 - Price entity & fixed price 2 tariffs
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
    # 9 - 2 meters with same entity price No tariff
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
        "sensor.monthly_energy",
        "sensor.monthly_energy_cost",
    ],
    # 10 - 2 meters with same entity price 2 tariff
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
    # 11 - 2 meters with same price No tariff
    [
        "sensor.energy_daily_energy_cost",
        "sensor.energy_monthly_energy_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
        "sensor.monthly_energy",
        "sensor.monthly_energy_cost",
    ],
    # 12 - 2 meters with same price 2 tariff
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
    # 13 - 2 meters with different entity price No tariff
    [
        "sensor.energy_price_cost",
        "sensor.energy_price2_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
        "sensor.monthly_energy",
        "sensor.monthly_energy_cost",
    ],
    # 14 - 2 meters with different entity price 2 tariff
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
    # 15 - 2 meters with different price No tariff
    [
        "sensor.energy_daily_energy_cost",
        "sensor.energy_monthly_energy_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
        "sensor.monthly_energy",
        "sensor.monthly_energy_cost",
    ],
    # 16 - 2 meters with different price 2 tariff
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
    # 17 - 2 meters with different prices & entity No tariff
    [
        "sensor.energy_price_cost",
        "sensor.energy_monthly_energy_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
        "sensor.monthly_energy",
        "sensor.monthly_energy_cost",
    ],
    # 18 - 2 meters with different prices & entity 2 tariff
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
    # 19 - No price No tariff
    [
        "sensor.daily_energy",
    ],
    # 20 - Price entity No tariff
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    # 21 - Fixed price entity No tariff
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    # 22 - Price entity & fixed price No tariff
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy",
        "sensor.daily_energy_cost",
    ],
    # 23 - No price 2 tariffs
    [
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "select.daily_energy",
    ],
    # 24 - Price entity 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 25 - Fixed price 2 tariffs
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 26 - Price entity & fixed price 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    ################################
    # Create utility meter defined #
    ################################
    # 27 - No price 2 tariffs
    [
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "select.daily_energy",
    ],
    # 28 - Price entity 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 29 - Fixed price 2 tariffs
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 30 - Price entity & fixed price 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    ##################################
    # Create only Energy cost sensor #
    ##################################
    # 31 - No price No tariff
    [],
    # 32 - Price entity No tariff
    [
        "sensor.energy_price_cost",
    ],
    # 33 - Fixed price entity No tariff
    [
        "sensor.energy_energy_cost_only_cost",
    ],
    # 34 - Price entity & fixed price No tariff
    [
        "sensor.energy_price_cost",
    ],
    # 35 - No price 2 tariffs
    [],
    # 36 - Price entity 2 tariffs
    [
        "sensor.energy_price_cost",
    ],
    # 37 - Fixed price 2 tariffs
    [
        "sensor.energy_energy_cost_only_cost",
    ],
    # 38 - Price entity & fixed price 2 tariffs
    [
        "sensor.energy_price_cost",
    ],
    #########################
    # from_grid source_type #
    #########################
    # 39 - No price 2 tariffs
    [
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "select.daily_energy",
    ],
    # 40 - Price entity 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 41 - Fixed price 2 tariffs
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 42 - Price entity & fixed price 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    #######################
    # to_grid source_type #
    #######################
    # 43 - No price 2 tariffs
    [
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "select.daily_energy",
    ],
    # 44 - Price entity 2 tariffs
    [
        "sensor.energy_price_compensation",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_compensation_peak",
        "sensor.daily_energy_compensation_offpeak",
        "select.daily_energy",
    ],
    # 45 - Fixed price 2 tariffs
    [
        "sensor.energy_daily_energy_compensation",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_compensation_peak",
        "sensor.daily_energy_compensation_offpeak",
        "select.daily_energy",
    ],
    # 46 - Price entity & fixed price 2 tariffs
    [
        "sensor.energy_price_compensation",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_compensation_peak",
        "sensor.daily_energy_compensation_offpeak",
        "select.daily_energy",
    ],
    ###################
    # gas source_type #
    ###################
    # 47 - No price 2 tariffs
    [
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "select.daily_energy",
    ],
    # 48 - Price entity 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 49 - Fixed price 2 tariffs
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 50 - Price entity & fixed price 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    #####################
    # water source_type #
    #####################
    # 51 - No price 2 tariffs
    [
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "select.daily_energy",
    ],
    # 52 - Price entity 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 53 - Fixed price 2 tariffs
    [
        "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
    # 54 - Price entity & fixed price 2 tariffs
    [
        "sensor.energy_price_cost",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_cost_peak",
        "sensor.daily_energy_cost_offpeak",
        "select.daily_energy",
    ],
]

CHECK_UM_SOURCES_EXPECTED_RESULTS = [
    #############
    # NO CONFIG #
    #############
    # 0 - No config
    {},
    #############
    # NO TARIFF #
    #############
    # 1 - No price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
    },
    # 2 - Price entity No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
    },
    # 3 - Fixed price entity No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_daily_energy_cost",
    },
    # 4 - Price entity & fixed price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
    },
    #############
    # 2 TARIFFS #
    #############
    # 5 - No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # 6 - Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # 7 - Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # 8 - Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    ###################
    # 2 ENERGY_METERS #
    ###################
    # 9 - 2 meters with same entity price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
        "sensor.monthly_energy": "sensor.energy",
        "sensor.monthly_energy_cost": "sensor.energy_price_cost",
    },
    # 10 - 2 meters with same entity price 2 tariff
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
        "sensor.monthly_energy_peak": "sensor.energy",
        "sensor.monthly_energy_offpeak": "sensor.energy",
        "sensor.monthly_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.monthly_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # 11 - 2 meters with same price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_daily_energy_cost",
        "sensor.monthly_energy": "sensor.energy",
        "sensor.monthly_energy_cost": "sensor.energy_monthly_energy_cost",
    },
    # 12 - 2 meters with same price 2 tariff
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
        "sensor.monthly_energy_peak": "sensor.energy",
        "sensor.monthly_energy_offpeak": "sensor.energy",
        "sensor.monthly_energy_cost_peak": "sensor.energy_monthly_energy_cost",
        "sensor.monthly_energy_cost_offpeak": "sensor.energy_monthly_energy_cost",
    },
    # 13 - 2 meters with different entity price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
        "sensor.monthly_energy": "sensor.energy",
        "sensor.monthly_energy_cost": "sensor.energy_price2_cost",
    },
    # 14 - 2 meters with different entity price 2 tariff
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
        "sensor.monthly_energy_peak": "sensor.energy",
        "sensor.monthly_energy_offpeak": "sensor.energy",
        "sensor.monthly_energy_cost_peak": "sensor.energy_price2_cost",
        "sensor.monthly_energy_cost_offpeak": "sensor.energy_price2_cost",
    },
    # 15 - 2 meters with different price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_daily_energy_cost",
        "sensor.monthly_energy": "sensor.energy",
        "sensor.monthly_energy_cost": "sensor.energy_monthly_energy_cost",
    },
    # 16 - 2 meters with different price 2 tariff
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
        "sensor.monthly_energy_peak": "sensor.energy",
        "sensor.monthly_energy_offpeak": "sensor.energy",
        "sensor.monthly_energy_cost_peak": "sensor.energy_monthly_energy_cost",
        "sensor.monthly_energy_cost_offpeak": "sensor.energy_monthly_energy_cost",
    },
    # 17 - 2 meters with different prices & entity No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
        "sensor.monthly_energy": "sensor.energy",
        "sensor.monthly_energy_cost": "sensor.energy_monthly_energy_cost",
    },
    # 18 - 2 meters with different prices & entity 2 tariff
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
        "sensor.monthly_energy_peak": "sensor.energy",
        "sensor.monthly_energy_offpeak": "sensor.energy",
        "sensor.monthly_energy_cost_peak": "sensor.energy_monthly_energy_cost",
        "sensor.monthly_energy_cost_offpeak": "sensor.energy_monthly_energy_cost",
    },
    ##############
    # Unique IDs #
    ##############
    # 19 - No price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
    },
    # 20 - Price entity No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
    },
    # 21 - Fixed price entity No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_daily_energy_cost",
    },
    # 22 - Price entity & fixed price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
    },
    # 23 - No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # 24 - Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # 25 - Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # 26 - Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    ################################
    # Create utility meter defined #
    ################################
    # 27 - No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # 28 - Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # 29 - Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # 30 - Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    ##################################
    # Create only Energy cost sensor #
    ##################################
    # Energy cost only does not have utility meter to track source
    # 31 - No price No tariff
    {},
    # 32 - Price entity No tariff
    {},
    # 33 - Fixed price entity No tariff
    {},
    # 34 - Price entity & fixed price No tariff
    {},
    # 35 - No price 2 tariffs
    {},
    # 36 - Price entity 2 tariffs
    {},
    # 37 - Fixed price 2 tariffs
    {},
    # 38 - Price entity & fixed price 2 tariffs
    {},
    #########################
    # from_grid source_type #
    #########################
    # 39 - No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # 40 - Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # 41 - Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # 42 - Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    #######################
    # to_grid source_type #
    #######################
    # 43 - No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # 44 - Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_compensation_peak": "sensor.energy_price_compensation",
        "sensor.daily_energy_compensation_offpeak": "sensor.energy_price_compensation",
    },
    # 45 - Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_compensation_peak": "sensor.energy_daily_energy_compensation",
        "sensor.daily_energy_compensation_offpeak": "sensor.energy_daily_energy_compensation",
    },
    # 46 - Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_compensation_peak": "sensor.energy_price_compensation",
        "sensor.daily_energy_compensation_offpeak": "sensor.energy_price_compensation",
    },
    ###################
    # gas source_type #
    ###################
    # 47 - No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # 48 - Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # 49 - Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # 50 - Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    #####################
    # water source_type #
    #####################
    # 51 - No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # 52 - Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # 53 - Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # 54 - Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
]
