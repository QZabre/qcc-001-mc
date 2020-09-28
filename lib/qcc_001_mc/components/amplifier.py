import board 

from qcc_001_mc import constants
from qcc_001_mc import components



# Map: switch state to temeperature state to amplifier.
_AMPLIFIER_STATE = {
    constants.SWITCH_STATE_ON: {
        constants.TEMPERATURE_STATE_OK: "10",
        constants.TEMPERATURE_STATE_WARNING: "11",
        constants.TEMPERATURE_STATE_CRITICAL: "12",
    },
    constants.SWITCH_STATE_OFF: {
        constants.TEMPERATURE_STATE_OK: "00",
        constants.TEMPERATURE_STATE_WARNING: "01",
        constants.TEMPERATURE_STATE_CRITICAL: "02",
    }
}

# Operational temperature range.
_TEMPERATURE_RANGE = (-25.0, -20.0, 40.0, 45.0)


class Amplifier():
    """Instrument voltage amplifier.
    
    """
    def __init__(self):
        """Instance constructor.
        
        """
        self.switch = components.Switch(board.D13)
        self.temperature_sensor = components.TemperatureSensor(0x48, _TEMPERATURE_RANGE)
    

    @property
    def status(self):
        """Returns current state.
        
        """ 
        return _AMPLIFIER_STATE[self.switch.status][self.temperature_sensor.status]


    @property
    def is_on(self):
        """Returns true if switch state == 1."""
        return self.switch.is_on

    
    @property
    def is_overheated(self):
        """Returns true if temperature is critical."""
        return self.temperature_sensor.is_overheated

    
    @property
    def is_overheating(self):
        """Returns true if temperature is warning."""
        return self.temperature_sensor.is_overheating


    def switch_off(self):
        """Switches amplifier off - invoked when temperature sensor is in critical state.
        
        """
        self.switch.switch_off()
