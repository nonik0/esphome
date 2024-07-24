#pragma once

#include "esphome/core/component.h"
#include "esphome/components/binary_sensor/binary_sensor.h"
#include "esphome/components/switch/switch.h"
#include "esphome/components/i2c/i2c.h"

namespace esphome {
namespace adafruit_trellis {

class AdafruitTrellis : public i2c::I2CDevice , public PollingComponent {
 public:
  //void loop() override;
  void dump_config() override;
  void update() override;
  void setup() override;
  float get_setup_priority() const override;

 protected:
  struct Button {
    binary_sensor::BinarySensor *button_{nullptr};
  } buttons_[16];

  struct LED {
    switch_::Switch *led_{nullptr};
  } leds_[16];
};

}  // namespace adafruit_trellis
}  // namespace esphome
