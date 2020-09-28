import digitalio

from qcc_001_mc import constants



class Switch():
    """Wraps a digital I/O driver.

    """
    def __init__(self, pin):
        """Constructor.
        
        :param pin: Pin upon circuit board to which switch is bound.

        """
        self._driver = digitalio.DigitalInOut(pin)
        self._driver.direction = digitalio.Direction.OUTPUT


    @property
    def status(self):
        """Returns current switch status."""
        return self._driver.value

    @property
    def value(self):
        """Returns current switch state."""
        return self._driver.value


    @property
    def is_on(self):
        """Returns true if switch state -> 1."""
        return self.value == constants.SWITCH_STATE_ON


    @property
    def is_off(self):
        """Returns true if switch state -> 0."""
        return self.value == constants.SWITCH_STATE_OFF


    def set_value(self, value):
        """Sets switch value to either on or off.
        
        """
        # Parse value.
        try:
            value = int(value)
        except ValueError:
            pass

        # Validate value.
        if value not in constants.SWITCH_STATES:
            raise ValueError(f"Invalid switch value: {value}")

        self._driver.value = value


    def switch_off(self):
        """Sets switch state -> 0.
        
        """
        self.set_value(constants.SWITCH_STATE_ON)


    def switch_on(self):
        """Sets switch state -> 1.
        
        """
        self.set_value(constants.SWITCH_STATE_OFF)


    def toggle(self):
        """Toggles switch state.
        
        """
        self.set_value(constants.SWITCH_STATE_OFF if self.is_on else constants.SWITCH_STATE_ON)
