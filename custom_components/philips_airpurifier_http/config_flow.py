from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

class PhilipsAirPurifierConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            host = user_input["host"]
            client = await self.hass.async_add_executor_job(lambda: HTTPAirClient(host, False))
            mac_address = client.get_mac_address()  # Method to retrieve MAC address
            await self.async_set_unique_id(mac_address)
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title="Philips AirPurifier", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("host"): str,
                vol.Required("api_key"): str,
            })
        )
