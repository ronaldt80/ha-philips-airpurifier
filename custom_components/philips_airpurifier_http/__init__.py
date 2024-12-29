"""The Philips AirPurifier component."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DATA_PHILIPS_FANS, DOMAIN


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Philips AirPurifier component."""
    hass.data[DOMAIN] = {}
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Philips AirPurifier from a config entry."""
    # Forward setup to the fan platform
    await hass.config_entries.async_forward_entry_setups(entry, ["fan"])
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # Unload the fan platform
    await hass.config_entries.async_forward_entry_unload(entry, "fan")
    return True
