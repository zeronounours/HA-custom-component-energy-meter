# Energy Meter

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)

![icon](img/icon.svg)

The Energy Meter integration provides functionality to track consumptions of
various utilities, like the builtin Utility Meter. But on top of it, it adds
entities to track costs for each tariffs.

Provides extended features on top of the builtin utility meter and energy
sensors to track costs for each tariff as well as total costs. It is possible
to achieve the same using templates, but it is long and error-prone to do it
for every single energy entity you want to track

![Example](img/energy_meter_screen.png)

## Installation

### HACS - preferred

This repository is compatible with HACS. This is the preferred way to install
the custom component.

### Manual

1. Download the release zip from [releases pages][releases]
2. Copy it within `<HA config dir>/custom_components/energy_meter`
3. Unzip in place
4. Restart Home Assistant

## Configuration

All configuration should be added to the `configurations.yaml` file. No GUI
configuration is currently supported.

### Basic configuration

The configuration of the component is mostly the same as the builtin
`utility_meter` integration:
https://www.home-assistant.io/integrations/utility_meter/

The main difference is the addition of `price` and `price_entity` options:

---

**price** _float (optional)_

The static price of the tariff (in currency per source unit, e.g. USD/kWh or
USD/m³)

---

**price_entity** _string (optional)_

The entity ID of a sensor giving the current price of the tariff (in currency
per source unit, e.g. USD/kWh or USD/m³)

---

The price must be given in currency/kWh. It depends on your currency
configuration. For instance, if your configured currency is dollar, it must be
in $/kWh.

Only one of `price` or `price_entity` should be given. If both are given,
`price_entity` would have precedence. If none is defined, this integration will
act as a basic utility meter, with no cost tracking.

### Energy cost type (Gas, Water, Return to grid)

The configuration can contain the optional `source_type` option to define the
type of energy being monitored:

---

**source_type** _string (optional)_

The type of energy being followed as source. These are the same as the builtin
energy dashboard. It can be of 4 types:

- `from_grid`: this is the default. To be used if source tracks grid
  consumption.
- `to_grid`: to be used if source tracks energy returned to grid.
- `gas`: to be used if source tracks gas consumption.
- `water`: to be used if source tracks water consumption.

---

Keep in mind that depending on the time, the allowed units for the source will
differ. `from_grid` and `to_grid` needs an electrical energy, while `gas` and
`water` expect a volume.

### Energy cost sensor only

If the use of utility meter is unwanted and you only want energy costs, it is
possible to set option `create_utility_meter` to `false`

---

**create_utility_meter** _boolean (optional)_

Whether to create a utility meter for the energy and energy costs. If set to
`false` only the energy cost entity will be created. Defaults to `true`.

---

### Using tariff

Tariff are like virtual counter associated to your meter. See the [official
documentation utility meters][um-conf] to understand them. They are only used
to increment a different index on the meter. **They won't change price of
energy.**

Tariffs are usually changed through automation based on time of state from
another sensor. The following example shows how to set a different tariff:

```yaml
# in configurations.yaml
automation:
  - id: switch_peak_offpeak_tariff
    alias: "Switch peak/offpeak tariff"
    initial_state: true
    trigger:
      - platform: time
        at: "05:00:00"
        variables:
          tariff: peak
      - platform: time
        at: "20:00:00"
        variables:
          tariff: offpeak
    action:
      - service: select.select_option
        target:
          entity_id:
            - select.daily_energy
            - select.monthly_energy
            - select.yearly_energy
        data:
          option: "{{ tariff }}"
```

The following example provides another way to set tariff with a more complex
logic:

```yaml
# in configurations.yaml
automation:
  - alias: Set Energy Meter Rate
    description: "Set Energy Meter Rate"
    trigger:
      - platform: time
        at: "07:00:30"
      - platform: time
        at: "09:00:30"
      - platform: time
        at: "17:00:30"
      - platform: time
        at: "20:00:30"
      - platform: time
        at: "22:00:30"
      - platform: homeassistant
        event: start
    condition: []
    action:
      - service: select.select_option
        data:
          option: >-
            {% set t = now() %} {%- if (( t.hour >= 7 and t.hour < 9 ) or (
            t.hour >= 17 and t.hour < 20 )) and
            is_state('binary_sensor.workday_sensor', 'on') %}
              peak
            {%- elif (( t.hour >= 9 and t.hour < 17 ) or ( t.hour >= 20 and
            t.hour < 22 )) and is_state('binary_sensor.workday_sensor', 'on')
            %}
              shoulder
            {%- else -%}
              offpeak
            {%- endif -%}
        target:
          entity_id:
            - select.daily_energy
            - select.monthly_energy
            - select.yearly_energy
    mode: single
```

### Examples

```yaml
# in configurations.yaml
energy_meter:
  daily_energy:
    source: sensor.energy
    name: Daily Energy
    cycle: daily
    price_entity: sensor.current_energy_price
    tariffs:
      - peak
      - offpeak
  monthly_energy:
    source: sensor.energy
    name: Monthly Energy
    cycle: monthly
    price: 0.20
    tariffs:
      - peak
      - offpeak

  energy_costs_only:
    name: Energy Costs
    source: sensor.energy
    price: 0.20
    create_utility_meter: false

  monthly_gas:
    source: sensor.gas_consumption
    name: Monthly Gas
    cycle: monthly
    price_entity: sensor.current_gas_price
    source_type: gas
    tariffs:
      - peak
      - offpeak
```

Usually, source energy sensors shares the same price. In order to prevent
configuration issues when changing it in a config, it is advised to use the
anchor feature of YAML:

```yaml
energy_meter:
  daily_energy:
    source: sensor.energy
    name: Daily Energy
    cycle: daily
    price_entity: &entity-price sensor.current_energy_price
    tariffs:
      - peak
      - offpeak
  monthly_energy:
    source: sensor.energy
    name: Monthly Energy
    cycle: monthly
    price: *entity-price
    tariffs:
      - peak
      - offpeak
```

## Services

This integration works on top of the builtin Utility Meter. It does not provide
additional services, but all builtin services are compatible with it.

### Reset

To reset the energy meters, rely on service `utility_meter.reset`:

```yaml
service: utility_meter.reset
target:
  entity_id: select.daily_energy
```

The reset will reset all sensors which relies on the same select, including:

- the energy sensor of each tariff
- the energy cost sensor of each tariff

_Note_: like with builtin utility meter, it is not possible to reset a meter
which do not have tariff. Instead, use the service [Calibrate](#calibrate)

### Calibrate

To reset the energy meters, rely on service `utility_meter.calibrate`:

```yaml
service: utility_meter.calibrate
data:
  value: "3"
target:
  entity_id: sensor.daily_energy_cost_offpeak
```

[releases-shield]:
  https://img.shields.io/github/release/zeronounours/HA-custom-component-energy-meter.svg?style=for-the-badge
[releases]:
  https://github.com/zeronounours/HA-custom-component-energy-meter/releases
[license-shield]:
  https://img.shields.io/github/license/zeronounours/HA-custom-component-energy-meter.svg?style=for-the-badge
[um-conf]: https://www.home-assistant.io/integrations/utility_meter/
