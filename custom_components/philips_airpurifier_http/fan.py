from homeassistant.components.fan import FanEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import HomeAssistantType
from .philips_airpurifier_fan import PhilipsAirPurifierFan
from .const import DOMAIN, DATA_PHILIPS_FANS, PHILIPS_MAC_ADDRESS, SERVICE_ATTR_ENTITY_ID, SERVICE_TO_METHOD, AIRPURIFIER_SERVICE_SCHEMA
import asyncio
import logging
from pyairctrl.http_client import HTTPAirClient

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up Philips AirPurifier fan based on a config entry."""
    host = entry.data["host"]
    name = entry.data.get("name", "Philips AirPurifier")

    client = await hass.async_add_executor_job(
        lambda: HTTPAirClient(host, False)
    )

    wifi = await hass.async_add_executor_job(client.get_wifi)
    mac_address = wifi.get(PHILIPS_MAC_ADDRESS)

    device = PhilipsAirPurifierFan(hass, client, name, mac_address)
    
    if DATA_PHILIPS_FANS not in hass.data:
        hass.data[DATA_PHILIPS_FANS] = []

    hass.data[DATA_PHILIPS_FANS].append(device)

    async_add_entities([device])

    async def async_service_handler(service):
        entity_ids = service.data.get(SERVICE_ATTR_ENTITY_ID)
        service_method = SERVICE_TO_METHOD.get(service.service)["method"]

        # Params to set to method handler. Drop entity_id.
        params = {
            key: value
            for key, value in service.data.items()
            if key != SERVICE_ATTR_ENTITY_ID
        }

        if entity_ids:
            devices = [
                device
                for device in hass.data[DATA_PHILIPS_FANS]
                if device.entity_id in entity_ids
            ]
        else:
            devices = hass.data[DATA_PHILIPS_FANS]

        update_tasks = []
        for device in devices:
            if not hasattr(device, service_method):
                continue
            await getattr(device, service_method)(**params)
            update_tasks.append(asyncio.create_task(device.async_update_ha_state(True)))

        if update_tasks:
            await asyncio.gather(*update_tasks)

    for air_purifier_service in SERVICE_TO_METHOD:
        schema = SERVICE_TO_METHOD[air_purifier_service].get(
            "schema", AIRPURIFIER_SERVICE_SCHEMA
        )
        hass.services.async_register(
            DOMAIN, air_purifier_service, async_service_handler, schema=schema
        )
