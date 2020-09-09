import digitalio



# Constant: switch on representation.
_STATE_ON = 1

# Constant: switch off representation.
_STATE_OFF = 0

# Set: valid states.
_STATES = {_STATE_ON, _STATE_OFF}


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


    @property
    def value(self):
        """Returns current switch state."""
        return self._driver.value


    @property
    def is_on(self):
        """Returns true if switch state -> 1."""
        return self.value == _STATE_ON


    @property
    def is_off(self):
        """Returns true if switch state -> 0."""
        return self.value == _STATE_OFF


    def set_value(self, value):
        """Sets switch value to either on or off.
        
        """
        # Parse value.
        try:
            value = int(value)
        except ValueError:
            pass

        # Validate value.
        if value not in _STATES:
            raise ValueError(f"Invalid switch value: {value}")

        self._driver.value = value


    def switch_off(self):
        """Sets switch state -> 0.
        
        """
        self.set_value(_STATE_ON)


    def switch_on(self):
        """Sets switch state -> 1.
        
        """
        self.set_value(_STATE_OFF)


    def toggle(self):
        """Toggles switch state.
        
        """
        self.set_value(_STATE_OFF if self.is_on else _STATE_ON)
