""" philips_air_purifier platform setup """

import logging

from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http.view import HomeAssistantView

import json
from os import walk, path

from .const import (
    DOMAIN,
    ICONLIST_URL,
    ICONS,
    ICONS_PATH,
    ICONS_URL,
    LOADER_PATH,
    LOADER_URL,
    PAP,
)

_LOGGER = logging.getLogger(__name__)

# icons code thanks to Thomas Loven:
# https://github.com/thomasloven/hass-fontawesome/blob/master/custom_components/fontawesome/__init__.py
class ListingView(HomeAssistantView):
    _LOGGER.debug("ListingView called")
    requires_auth = False

    def __init__(self, hass, url):
        self._hass = hass
        self.url = url
        self.name = "Icon Listing"

    async def get(self, request):
        return json.dumps(self._hass.data[DOMAIN][ICONS])


async def async_setup(hass, config) -> bool:
    """Set up the icons for the Philips Air Purifier integration."""
    _LOGGER.debug("async_setup called")

    hass.http.register_static_path(
        LOADER_URL,
        hass.config.path(LOADER_PATH),
        True)

    add_extra_js_url(hass, LOADER_URL)

    iset = PAP
    iconpath = hass.config.path(ICONS_PATH + "/" + iset)

    # walk the directory to get the icons
    icons = []
    for (dirpath, dirnames, filenames) in walk(iconpath):
        icons.extend(
            [
                {"name": path.join(dirpath[len(iconpath) :], fn[:-4])}
                for fn in filenames
                if fn.endswith(".svg")
            ]
        )

    # store icons
    data = hass.data.get(DOMAIN)
    if data is None:
        hass.data[DOMAIN] = {}

    hass.data[DOMAIN][ICONS] = icons

    # register path and view
    hass.http.register_static_path(ICONS_URL + "/" + iset, iconpath, True)
    hass.http.register_view(ListingView(hass, ICONLIST_URL + "/" + iset))

    return True


async def async_setup_entry(hass, entry):
    return True


async def async_remove_entry(hass, entry):
    return True
