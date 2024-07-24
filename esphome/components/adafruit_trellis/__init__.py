import esphome.codegen as cg
from esphome.components import i2c, binary_sensor
import esphome.config_validation as cv
from esphome.const import CONF_ID

CODEOWNERS = ["@nonik0"]

DEPENDENCIES = ["i2c"]
AUTO_LOAD = ["binary_sensor", "switch"]
MULTI_CONF = True

CONF_ADAFRUIT_TRELLIS_ID = "adafruit_trellis_id"

adafruit_trellis_ns = cg.esphome_ns.namespace("adafruit_trellis")
AdafruitTrellis = adafruit_trellis_ns.class_("AdafruitTrellis", cg.PollingComponent, i2c.I2CDevice)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(AdafruitTrellis),
        }
    )
    .extend(cv.polling_component_schema("500ms")) # TODO: more frequent???
    .extend(i2c.i2c_device_schema(0x18))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    //await uart.register_uart_device(var, config)

    cg.add(var.set_enable_fake_traffic(config[CONF_ENABLE_FAKE_TRAFFIC]))
    cg.add(var.set_rx_timeout(config[CONF_RX_TIMEOUT]))
    cg.add(var.set_modbus_id(config[CONF_MODBUS_ID]))