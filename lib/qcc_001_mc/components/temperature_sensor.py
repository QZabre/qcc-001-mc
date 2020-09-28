import board
import busio
import adafruit_adt7410

from qcc_001_mc import constants



# I2C Bus - drives temperature sensors.
_i2c_bus = busio.I2C(board.SCL, board.SDA)


class TemperatureSensor():
    """Wraps a adafruit_adt7410 thermal sensor driver.

    """
    def __init__(self, address, temperature_range):
        """Constructor.
        
        :param address: I2C bus address.
        :param temperature_range: 4 member tuple: min, min_warning, max_warning, max.

        """
        self.state = None
        self.temperature_range = temperature_range
        self._driver = adafruit_adt7410.ADT7410(_i2c_bus, address=address)
        self._driver.high_resolution = True


    @property
    def status(self):
        """Gets current status."""
        return constants.TEMPERATURE_STATE_OK if self.is_ok else \
               constants.TEMPERATURE_STATE_WARNING if self.is_overheating else \
               constants.TEMPERATURE_STATE_CRITICAL


    @property
    def temperature(self):
        """Gets current temperature in C."""
        return self._driver.temperature


    @property
    def is_overheated(self):
        """Returns true if operating temperature exceeds safety range.
        
        """
        if self.temperature_range is None:
            return False

        min_temp, _, _, max_temp = self.temperature_range

        return self.temperature <= min_temp or self.temperature >= max_temp


    @property
    def is_overheating(self):
        if self.temperature_range is None:
            return False

        _, min_temp, max_temp, _ = self.temperature_range

        return self.temperature <= min_temp or self.temperature >= max_temp


    @property
    def is_ok(self):
        """Returns true if operating temperature is within safety range.
        
        """
        return not self.is_overheated and not self.is_overheating
