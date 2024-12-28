from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "philips_airpurifier_http"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    # Setup logic for the integration
    return True
