import esphome.codegen as cg
from esphome.components import binary_sensor
import esphome.config_validation as cv
from esphome.const import (
    CONF_ID,
    # TODO: device class
)

from . import CONF_ADAFRUIT_TRELLIS_ID, AdafruitTrellis

DEPENDENCIES = ["adafruit_trellis"]

CODEOWNERS = ["@nonik0"]

CONF_BUTTON_1 = "button_1"
CONF_BUTTON_2 = "button_2"
CONF_BUTTON_3 = "button_3"
CONF_BUTTON_4 = "button_4"
CONF_BUTTON_5 = "button_5"
CONF_BUTTON_6 = "button_6"
CONF_BUTTON_7 = "button_7"
CONF_BUTTON_8 = "button_8"
CONF_BUTTON_9 = "button_9"
CONF_BUTTON_10 = "button_10"
CONF_BUTTON_11 = "button_11"
CONF_BUTTON_12 = "button_12"
CONF_BUTTON_13 = "button_13"
CONF_BUTTON_14 = "button_14"
CONF_BUTTON_15 = "button_15"
CONF_BUTTON_16 = "button_16"

ICON_BUTTON = "mdi:gesture-tap"
ICON_LED = "mdi:led-on"

BUTTONS = [
    CONF_BUTTON_1,
    CONF_BUTTON_2,
    CONF_BUTTON_3,
    CONF_BUTTON_4,
    CONF_BUTTON_5,
    CONF_BUTTON_6,
    CONF_BUTTON_7,
    CONF_BUTTON_8,
    CONF_BUTTON_9,
    CONF_BUTTON_10,
    CONF_BUTTON_11,
    CONF_BUTTON_12,
    CONF_BUTTON_13,
    CONF_BUTTON_14,
    CONF_BUTTON_15,
    CONF_BUTTON_16
]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_ADAFRUIT_TRELLIS_ID): cv.use_id(AdafruitTrellis),
        cv.Optional(CONF_BUTTON_1): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_2): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_3): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_4): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_5): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_6): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_7): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_8): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_9): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_10): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_11): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_12): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_13): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_14): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_15): binary_sensor.binary_sensor_schema(),
        cv.Optional(CONF_BUTTON_16): binary_sensor.binary_sensor_schema()
    }
)

async def to_code(config):
    hub = await cg.get_variable(config[CONF_ADAFRUIT_TRELLIS_ID])
    for key in BUTTONS:
        if key in config:
            conf = config[key]
            sens = cg.new_Pvariable(conf[CONF_ID])
            await binary_sensor.register_binary_sensor(sens, conf)
            cg.add(getattr(hub, f"set_{key}_binary_sensor")(sens))
