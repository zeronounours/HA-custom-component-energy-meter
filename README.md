# Energy meter

Provides extended features on top of the builtin utility meter to track costs
for each tariff as well as total costs.

## Installation

1. Clone the repository within `custom_components`
```shell
cd /config/custom_components
git clone https://github.com/zeronounours/HA-custom-component-energy-meter.git energy_meter
```

**Note:** the directory of the custom components must be named `energy_meter`

2. Restart Home Assistant

## Configuration

The configuration of the component is mostly the same as the builtin
`utility_meter` integration: https://www.home-assistant.io/integrations/utility_meter/

The only difference is the addition of `price` and `price_entity` options:

---
**price** *float (optional)*

The static price of the tariff (in currency/kWh)

---
**price_entity** *string (optional)*

The entity ID of a sensor giving the current price of the tariff (in currency/kWh)

---

The price must be given in currency/kWh. It depends on your currency
configuration. For instance, if your configured currency is dollar, it must be
in $/kWh.

Only one of `price` or `price_entity` should be given. If both are given,
`price_entity` would have precedence. If none is defined, this integration will
act as a basic utility meter, with no cost tracking.

## Example

```yaml
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
```
