""" philips_airpurifier constants"""

# Integration setup
DOMAIN = "philips_airpurifier_http"
DATA_PHILIPS_FANS = "fan.philips_airpurifier"

# Integration defaults
DEFAULT_NAME = "Philips AirPurifier"
DEFAULT_ICON = "mdi:air-purifier"

# Services
SERVICE_SET_FUNCTION = "set_function"
SERVICE_SET_TARGET_HUMIDITY = "set_target_humidity"
SERVICE_SET_LIGHT_BRIGHTNESS = "set_light_brightness"
SERVICE_SET_CHILD_LOCK = "set_child_lock"
SERVICE_SET_TIMER = "set_timer"
SERVICE_SET_DISPLAY_LIGHT = "set_display_light"
SERVICE_SET_USED_INDEX = "set_used_index"

# Service attributes
SERVICE_ATTR_ENTITY_ID = "entity_id"
SERVICE_ATTR_FUNCTION = "function"
SERVICE_ATTR_HUMIDITY = "humidity"
SERVICE_ATTR_BRIGHTNESS_LEVEL = "level"
SERVICE_ATTR_CHILD_LOCK = "lock"
SERVICE_ATTR_TIMER_HOURS = "hours"
SERVICE_ATTR_DISPLAY_LIGHT = "light"
SERVICE_ATTR_USED_INDEX = "used_index"

# Device attribute keys
ATTR_MODEL = "model"
ATTR_FUNCTION = "function"
ATTR_USED_INDEX = "used_index"
ATTR_PM25 = "pm25"
ATTR_ALLERGEN_INDEX = "allergen_index"
ATTR_TEMPERATURE = "temperature"
ATTR_HUMIDITY = "humidity"
ATTR_TARGET_HUMIDITY = "target_humidity"
ATTR_WATER_LEVEL = "water_level"
ATTR_LIGHT_BRIGHTNESS = "light_brightness"
ATTR_DISPLAY_LIGHT = "display_light"
ATTR_CHILD_LOCK = "child_lock"
ATTR_TIMER = "timer"
ATTR_TIMER_REMAINGING_MINUTES = "timer_remaining_minutes"
ATTR_PRE_FILTER = "pre_filter"
ATTR_WICK_FILTER = "wick_filter"
ATTR_CARBON_FILTER = "carbon_filter"
ATTR_HEPA_FILTER = "hepa_filter"

# Philips API keys
PHILIPS_ALLERGEN_INDEX = "iaql"
PHILIPS_LIGHT_BRIGHTNESS = "aqil"
PHILIPS_CHILD_LOCK = "cl"
PHILIPS_FUNCTION = "func"
PHILIPS_HUMIDITY = "rh"
PHILIPS_MODE = "mode"
PHILIPS_PM25 = "pm25"
PHILIPS_POWER = "pwr"
PHILIPS_SPEED = "om"
PHILIPS_TARGET_HUMIDITY = "rhset"
PHILIPS_TEMPERATURE = "temp"
PHILIPS_TIMER = "dt"
PHILIPS_TIMER_REMAINING = "dtrs"
PHILIPS_USED_INDEX = "ddp"
PHILIPS_WATER_LEVEL = "wl"
PHILIPS_DISPLAY_LIGHT = "uil"

PHILIPS_MODEL_NAME = "name"
PHILIPS_MAC_ADDRESS = "macaddress"

# Philips API values
PHILIPS_SPEED_SILENT = "s"
PHILIPS_SPEED_TURBO = "t"
PHILIPS_MODE_AUTO = "P"
PHILIPS_MODE_ALLERGEN = "A" 
PHILIPS_MODE_SLEEP = "M"
PHILIPS_MODE_BACTERIA = "B"
PHILIPS_FUNCTION_PURIFICATION = "P"
PHILIPS_FUNCTION_BOTH = "PH"

# Speed values
SPEED_SILENT = "Silent"
SPEED_1 = "Speed 1"
SPEED_2 = "Speed 2"
SPEED_3 = "Speed 3"
SPEED_TURBO = "Turbo"

SPEED_NAMES = [SPEED_SILENT, SPEED_1, SPEED_2, SPEED_3, SPEED_TURBO]
SPEED_MAP = {
    PHILIPS_SPEED_SILENT: SPEED_SILENT,
    "1": SPEED_1,
    "2": SPEED_2,
    "3": SPEED_3,
    PHILIPS_SPEED_TURBO: SPEED_TURBO,
}

# Mode values
MODE_AUTO = "auto"
MODE_ALLERGEN = "allergen"
MODE_SLEEP = "sleep"
MODE_MANUAL = "manual"
MODE_BACTERIA = "bacteria"
MODE_NIGHT = "night"

MODE_NAMES = [
    MODE_AUTO,
    MODE_ALLERGEN,
    MODE_SLEEP,
    MODE_MANUAL,
    MODE_BACTERIA,
    MODE_NIGHT,
]

MODE_MAP = {
    PHILIPS_MODE_AUTO: MODE_AUTO,
    PHILIPS_MODE_ALLERGEN: MODE_ALLERGEN,
    PHILIPS_MODE_SLEEP: MODE_SLEEP,
    PHILIPS_MODE_BACTERIA: MODE_BACTERIA,
}


# Function values
FUNCTION_PURIFICATION = "Purification"
FUNCTION_BOTH = "Purification & Humidification"
FUNCTION_MAP = {
    PHILIPS_FUNCTION_PURIFICATION: FUNCTION_PURIFICATION,
    PHILIPS_FUNCTION_BOTH: FUNCTION_BOTH,
}


# Misc values

DISPLAY_LIGHT_MAP = {
    "0": False,
    "1": True,
}

USED_INDEX_MAP = {"1": "PM2.5", "0": "IAI"}

TARGET_HUMIDITY_LIST = [40, 50, 60]
LIGHT_BRIGHTNESS_LIST = [0, 25, 50, 75, 100]
