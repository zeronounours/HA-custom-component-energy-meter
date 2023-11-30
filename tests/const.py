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
    ################################
    # Create utility meter defined #
    ################################
    # No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "create_utility_meter": "yes",
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
                "create_utility_meter": "yes",
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
                "create_utility_meter": "yes",
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
                "create_utility_meter": "yes",
            },
        },
    },
    ##################################
    # Create only Energy cost sensor #
    ##################################
    # No price No tariff
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "create_utility_meter": "no",
            },
        },
    },
    # Price entity No tariff
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "price_entity": "sensor.price",
                "create_utility_meter": "no",
            },
        },
    },
    # Fixed price entity No tariff
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "price": 2,
                "create_utility_meter": "no",
            },
        },
    },
    # Price entity & fixed price No tariff
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
    # No price 2 tariffs
    {
        DOMAIN: {
            "energy_cost_only": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "create_utility_meter": "no",
            },
        },
    },
    # Price entity 2 tariffs
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
    # Fixed price 2 tariffs
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
    # Price entity & fixed price 2 tariffs
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
    # No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "source_type": "from_grid",
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
                "source_type": "from_grid",
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
                "source_type": "from_grid",
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
                "source_type": "from_grid",
            },
        },
    },
    #######################
    # to_grid source_type #
    #######################
    # No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "source_type": "to_grid",
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
                "source_type": "to_grid",
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
                "source_type": "to_grid",
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
                "source_type": "to_grid",
            },
        },
    },
    ###################
    # gas source_type #
    ###################
    # No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "source_type": "gas",
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
                "source_type": "gas",
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
                "source_type": "gas",
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
                "source_type": "gas",
            },
        },
    },
    #####################
    # water source_type #
    #####################
    # No price 2 tariffs
    {
        DOMAIN: {
            "daily_energy": {
                "source": "sensor.energy",
                "tariffs": ["peak", "offpeak"],
                "source_type": "water",
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
                "source_type": "water",
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
                "source_type": "water",
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
                "source_type": "water",
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
    ################################
    # Create utility meter defined #
    ################################
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
    ##################################
    # Create only Energy cost sensor #
    ##################################
    # No price No tariff
    [],
    # Price entity No tariff
    [
        "sensor.energy_price_cost",
    ],
    # Fixed price entity No tariff
    [
        "sensor.energy_energy_cost_only_cost",
    ],
    # Price entity & fixed price No tariff
    [
        "sensor.energy_price_cost",
    ],
    # No price 2 tariffs
    [],
    # Price entity 2 tariffs
    [
        "sensor.energy_price_cost",
    ],
    # Fixed price 2 tariffs
    [
        "sensor.energy_energy_cost_only_cost",
    ],
    # Price entity & fixed price 2 tariffs
    [
        "sensor.energy_price_cost",
    ],
    #########################
    # from_grid source_type #
    #########################
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
    #######################
    # to_grid source_type #
    #######################
    # No price 2 tariffs
    [
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "select.daily_energy",
    ],
    # Price entity 2 tariffs
    [
        "sensor.energy_price_compensation",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_compensation_peak",
        "sensor.daily_energy_compensation_offpeak",
        "select.daily_energy",
    ],
    # Fixed price 2 tariffs
    [
        "sensor.energy_daily_energy_compensation",
        "sensor.daily_energy_peak",
        "sensor.daily_energy_offpeak",
        "sensor.daily_energy_compensation_peak",
        "sensor.daily_energy_compensation_offpeak",
        "select.daily_energy",
    ],
    # Price entity & fixed price 2 tariffs
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
    #####################
    # water source_type #
    #####################
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

CHECK_UM_SOURCES_EXPECTED_RESULTS = [
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
        "sensor.daily_energy": "sensor.energy",
    },
    # Price entity No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
    },
    # Fixed price entity No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_daily_energy_cost",
    },
    # Price entity & fixed price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
    },
    #############
    # 2 TARIFFS #
    #############
    # No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    ###################
    # 2 ENERGY_METERS #
    ###################
    # 2 meters with same entity price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
        "sensor.monthly_energy": "sensor.energy",
        "sensor.monthly_energy_cost": "sensor.energy_price_cost",
    },
    # 2 meters with same entity price 2 tariff
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
    # 2 meters with same price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_daily_energy_cost",
        "sensor.monthly_energy": "sensor.energy",
        "sensor.monthly_energy_cost": "sensor.energy_monthly_energy_cost",
    },
    # 2 meters with same price 2 tariff
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
    # 2 meters with different entity price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
        "sensor.monthly_energy": "sensor.energy",
        "sensor.monthly_energy_cost": "sensor.energy_price2_cost",
    },
    # 2 meters with different entity price 2 tariff
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
    # 2 meters with different price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_daily_energy_cost",
        "sensor.monthly_energy": "sensor.energy",
        "sensor.monthly_energy_cost": "sensor.energy_monthly_energy_cost",
    },
    # 2 meters with different price 2 tariff
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
    # 2 meters with different prices & entity No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
        "sensor.monthly_energy": "sensor.energy",
        "sensor.monthly_energy_cost": "sensor.energy_monthly_energy_cost",
    },
    # 2 meters with different prices & entity 2 tariff
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
    # No price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
    },
    # Price entity No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
    },
    # Fixed price entity No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_daily_energy_cost",
    },
    # Price entity & fixed price No tariff
    {
        "sensor.daily_energy": "sensor.energy",
        "sensor.daily_energy_cost": "sensor.energy_price_cost",
    },
    # No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    ################################
    # Create utility meter defined #
    ################################
    # No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # Price entity & fixed price 2 tariffs
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
    # No price No tariff
    {},
    # Price entity No tariff
    {},
    # Fixed price entity No tariff
    {},
    # Price entity & fixed price No tariff
    {},
    # No price 2 tariffs
    {},
    # Price entity 2 tariffs
    {},
    # Fixed price 2 tariffs
    {},
    # Price entity & fixed price 2 tariffs
    {},
    #########################
    # from_grid source_type #
    #########################
    # No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    #######################
    # to_grid source_type #
    #######################
    # No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_compensation_peak": "sensor.energy_price_compensation",
        "sensor.daily_energy_compensation_offpeak": "sensor.energy_price_compensation",
    },
    # Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_compensation_peak": "sensor.energy_daily_energy_compensation",
        "sensor.daily_energy_compensation_offpeak": "sensor.energy_daily_energy_compensation",
    },
    # Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_compensation_peak": "sensor.energy_price_compensation",
        "sensor.daily_energy_compensation_offpeak": "sensor.energy_price_compensation",
    },
    ###################
    # gas source_type #
    ###################
    # No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    #####################
    # water source_type #
    #####################
    # No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    #########################
    # from_grid source_type #
    #########################
    # No price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
    },
    # Price entity 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
    # Fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_daily_energy_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_daily_energy_cost",
    },
    # Price entity & fixed price 2 tariffs
    {
        "sensor.daily_energy_peak": "sensor.energy",
        "sensor.daily_energy_offpeak": "sensor.energy",
        "sensor.daily_energy_cost_peak": "sensor.energy_price_cost",
        "sensor.daily_energy_cost_offpeak": "sensor.energy_price_cost",
    },
]
