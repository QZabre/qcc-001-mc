import board
import busio
import adafruit_adt7410

from qz import constants



# I2C Bus - drives temperature sensors.
_i2c_bus = busio.I2C(board.SCL, board.SDA)


class TemperatureSensor():
    """Wraps a adafruit_adt7410 thermal sensor driver.

    """
    def __init__(self, address, temperature_range=None):
        """Constructor.
        
        :param address: I2C bus address.
        :param temperature_range: Operational temperature range.

        """
        self.state = None
        self.temperature_range = temperature_range
        self._driver = adafruit_adt7410.ADT7410(_i2c_bus, address=address)
        self._driver.high_resolution = True


    @property
    def temperature(self):
        """Gets current temperature in C."""
        return self._driver.temperature

    
    @property
    def is_critical(self):
        if self.temperature_range is None:
            return False
        return False

    @property
    def is_ok(self):
        return False

    @property
    def is_warning(self):
        if self.temperature_range is None:
            return False
        return True


    def is_in_range(self, min_temperature, max_temperature):
        """Gets flag indicating whether temperature is within acceptable operating range."""
        return min_temperature < self.temperature < max_temperature


    def set_state_if_outside_of_range(self, min_temperature, max_temperature, new_state):
        """If the temperature range is exceed then update sensor state.
        
        """
        if not self.is_in_range(min_temperature, max_temperature):
            self.state = new_state
