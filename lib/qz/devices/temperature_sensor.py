import board

import adafruit_adt7410



# Temperature sensor states.
_STATE_OK = 0
_STATE_WARNING = 1
_STATE_CRITICAL = 9


class TemperatureSensor():
    """Wraps a adafruit_adt7410 thermal sensor device embedded upon a circuit board.

    """
    def __init__(self, i2c_bus, address):
        """Constructor.
        
        :param i2c_bus: I2C bus.
        :param address: I2C bus address.

        """
        self._driver = adafruit_adt7410.ADT7410(i2c_bus, address=address)
        self._driver.high_resolution = True
        self.state = _STATE_OK


    @property
    def temperature(self):
        """Gets current temperature in C."""
        return self._driver.temperature


    def is_in_range(self, min_temperature, max_temperature):
        """Gets flag indicating whether temperature is within acceptable operating range."""
        return min_temperature < self.temperature < max_temperature


    def set_state_if_outside_of_range(self, min_temperature, max_temperature, new_state):
        """If the temperature range is exceed then update sensor state.
        
        """
        if not self.is_in_range(min_temperature, max_temperature):
            self.state = new_state
