import digitalio



# Constant: switch on representation.
_ON = 1

# Constant: switch off representation.
_OFF = 0


class Switch():
    """Wraps a digital I/O device embedded upon a circuit board.

    """
    def __init__(self, key, pin):
        """Constructor.
        
        :param key: Device key used for disambiguation purposes.
        :param pin: Pin upon circuit board to which switch is bound.

        """
        self.key = key
        self._driver = digitalio.DigitalInOut(pin)
        self._driver.direction = digitalio.Direction.OUTPUT
        self._driver.value = False


    @property
    def value(self):
        return self._driver.value

    @property
    def is_on(self):
        return self.value == _ON

    @property
    def is_off(self):
        return self.value == _OFF

    def set_value(self, value):
        self._driver.value = value

    def switch_off(self):
        self.set_value(0)

    def switch_on(self):
        self.set_value(1)
