"""Global fixtures for energy_meter integration."""

# Standard libraries
import logging
from unittest.mock import patch

# Third party libraries
from homeassistant.helpers import recorder
import pytest

# Project imports
from custom_components.energy_meter.const import DOMAIN

pytest_plugins = ("pytest_homeassistant_custom_component",)


# Allow increasing logging to debug
logging.basicConfig(level=logging.INFO)
logging.getLogger("sqlalchemy.engine").setLevel(logging.WARN)


def pytest_configure(config: pytest.Config) -> None:
    """Register marker for tests that log exceptions."""
    if config.getoption("verbose") > 0:
        logging.getLogger(f"custom_components.{DOMAIN}").setLevel(logging.DEBUG)


# Used to enable custom_integration
@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable custom integrations for tests."""
    yield


# Used to create a config with necessary sections to run tests
@pytest.fixture(name="config")
def config(request):
    """Create a fixture to add config required for tests."""
    with patch("homeassistant.components.recorder.ALLOW_IN_MEMORY_DB", True):
        yield {"recorder": {"db_url": "sqlite:///:memory:"}} | (
            request.param if hasattr(request, "param") else {}
        )


# Used to initialize the recorder
@pytest.fixture(autouse=True)
def auto_initialize_recorder(hass):
    """Initialize the recorder for tests."""
    recorder.async_initialize_recorder(hass)
    yield


# This fixture is used to prevent HomeAssistant from attempting to
# create and dismiss persistent notifications. These calls would fail
# without this fixture since the persistent_notification integration is
# never loaded during a test.
@pytest.fixture(name="skip_notifications", autouse=True)
def skip_notifications_fixture():
    """Skip notification calls."""
    with patch("homeassistant.components.persistent_notification.async_create"), patch(
        "homeassistant.components.persistent_notification.async_dismiss",
    ):
        yield
