"""Global helpers for tests."""

# Project imports
from custom_components.energy_meter.const import DOMAIN


def assert_logger(logger_mock, method):
    """Assert errors match expectations."""
    # method was called
    getattr(logger_mock, method).assert_called()
    # logged message contains the DOMAIN
    for call in getattr(logger_mock, method).call_args_list:
        message = call.args[0] % call.args[1:]
        assert DOMAIN in message
