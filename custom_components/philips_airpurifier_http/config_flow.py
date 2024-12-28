from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class PhilipsAirPurifierConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Philips AirPurifier HTTP", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("host"): str,
            })
        )
