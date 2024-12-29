"""Support for Philips AirPurifier fans."""

import asyncio
import logging

from homeassistant.components.fan import FanEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant  # Updated import

from .const import DATA_PHILIPS_FANS, DOMAIN, SERVICE_ATTR_ENTITY_ID
from .philips_airpurifier_fan import PhilipsAirPurifierFan
from .services import AIRPURIFIER_SERVICE_SCHEMA, SERVICE_TO_METHOD

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities
):
    """Set up Philips AirPurifier fan based on a config entry."""
    fans = hass.data.get(DATA_PHILIPS_FANS, [])

    if not fans:
        _LOGGER.error("No fans found in hass.data[DATA_PHILIPS_FANS]")
        return False

    async_add_entities(fans, update_before_add=True)
    return True

    for air_purifier_service in SERVICE_TO_METHOD:
        schema = SERVICE_TO_METHOD[air_purifier_service].get(
            "schema", AIRPURIFIER_SERVICE_SCHEMA
        )
        hass.services.async_register(
            DOMAIN, air_purifier_service, async_service_handler, schema=schema
        )
