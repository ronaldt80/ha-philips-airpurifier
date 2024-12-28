from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN
from pyairctrl.http_client import HTTPAirClient  # Correct import path for HTTPAirClient
import logging

_LOGGER = logging.getLogger(__name__)

class PhilipsAirPurifierConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        default_title = "Philips AirPurifier"
        
        if user_input is not None:
            host = user_input["host"]
            name = user_input.get("name", default_title)
            try:
                client = await self.hass.async_add_executor_job(lambda: HTTPAirClient(host, False))
                wifi_info = await self.hass.async_add_executor_job(client.get_wifi)  # Ensure this method exists
                mac_address = wifi_info.get("macaddress")  # Adjust this based on the actual key returned

                if not mac_address:
                    _LOGGER.error("Cannot retrieve MAC address from the device.")
                    errors["base"] = "cannot_retrieve_mac"
                else:
                    # Use the MAC address to create a default title if name is not provided
                    if name == default_title:
                        name = f"{default_title} {mac_address}"

                    await self.async_set_unique_id(mac_address)
                    self._abort_if_unique_id_configured()
                    _LOGGER.info(f"Setting up Philips AirPurifier with MAC address: {mac_address}")
                    return self.async_create_entry(title=name, data={"host": host, "name": name})
            except Exception as e:
                _LOGGER.error(f"Error setting up Philips AirPurifier: {e}")
                errors["base"] = "cannot_connect"
        else:
            user_input = {}
            user_input["host"] = ""
            user_input["name"] = default_title

        data_schema = vol.Schema({
            vol.Required("host", default=user_input["host"]): str,
            vol.Optional("name", default=user_input["name"]): str,
        })

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
