"""Config flow for Philips AirPurifier integration."""

import logging

from pyairctrl.http_client import HTTPAirClient
import voluptuous as vol

from homeassistant import config_entries

from .const import DATA_PHILIPS_FANS, DOMAIN, PHILIPS_MAC_ADDRESS
from .philips_airpurifier_fan import PhilipsAirPurifierFan

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
                client = await self.hass.async_add_executor_job(
                    lambda: HTTPAirClient(host, False)
                )
                wifi_info = await self.hass.async_add_executor_job(client.get_wifi)
                _LOGGER.debug(f"WiFi info: {wifi_info}")
                mac_address = wifi_info.get(PHILIPS_MAC_ADDRESS)  # Use the correct key
                _LOGGER.debug(f"Retrieved MAC address: {mac_address}")

                if not mac_address:
                    _LOGGER.error("Cannot retrieve MAC address from the device.")
                    errors["base"] = "cannot_retrieve_mac"
                else:
                    if name == default_title:
                        name = f"{default_title} {mac_address}"

                    await self.async_set_unique_id(mac_address)
                    self._abort_if_unique_id_configured()
                    _LOGGER.info(
                        f"Setting up Philips AirPurifier with MAC address: {mac_address}"
                    )

                    # Create and set up the device
                    device = PhilipsAirPurifierFan(self.hass, client, name, mac_address)
                    if DATA_PHILIPS_FANS not in self.hass.data:
                        self.hass.data[DATA_PHILIPS_FANS] = []
                    self.hass.data[DATA_PHILIPS_FANS].append(device)

                    #                   # Forward the entry setup to the fan platform
                    #                    await self.hass.config_entries.async_forward_entry_setup(self.config_entry, "fan")

                    return self.async_create_entry(
                        title=name, data={"host": host, "name": name}
                    )
            except Exception as e:
                _LOGGER.error(f"Error setting up Philips AirPurifier: {e}")
                errors["base"] = "cannot_connect"
        else:
            user_input = {}
            user_input["host"] = ""
            user_input["name"] = default_title

        data_schema = vol.Schema(
            {
                vol.Required("host", default=user_input["host"]): str,
                vol.Optional("name", default=user_input["name"]): str,
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )
