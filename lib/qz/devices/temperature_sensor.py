import board
import busio

import adafruit_adt7410



class TemperatureSensor():
    """Wraps a adafruit_adt7410 thermal sensor device embedded upon a circuit board.

    """
    def __init__(self, address, i2c_pin_1=None, i2c_pin_2=None):
        """Constructor.
        
        :param address: I2C address.

        """
        self._driver = adafruit_adt7410.ADT7410(
            busio.I2C(
                i2c_pin_1 or board.SCL,
                i2c_pin_2 or board.SDA,
                ),
            address=address,
            )
        self._driver.high_resolution = True


    @property
    def temperature(self):
        """Gets current temperature in C."""
        return self._driver.temperature


    def is_in_range(self, min_temperature, max_temperature):
        """Gets flag indicating whether temperature is within acceptable operating range."""
        return min_temperature < self.temperature < max_temperature
