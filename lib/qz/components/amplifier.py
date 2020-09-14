import board 

from qz import constants
from qz.components import Switch
from qz.components import TemperatureSensor



# Map: switch state to temeperature state to amplifier.
_AMPLIFIER_STATE = {
    constants.SWITCH_STATE_ON: {
        constants.TEMPERATURE_STATE_OK: 0,
        constants.TEMPERATURE_STATE_WARNING: 1,
        constants.TEMPERATURE_STATE_CRITICAL: 2,
    },
    constants.SWITCH_STATE_OFF: {
        constants.TEMPERATURE_STATE_OK: 3,
        constants.TEMPERATURE_STATE_WARNING: 4,
        constants.TEMPERATURE_STATE_CRITICAL: 5,
    }
}


class Amplifier():
    """Instrument voltage amplifier.
    
    """
    def __init__(self, switch, temperature_sensor):
        """Instance constructor.
        
        """
        self.key = "AMP"
        self.switch = Switch(constants.SWITCH_AMP, board.D13)
        self.temperature_sensor = TemperatureSensor("AMP", 0x48, (
            (-25.0, 45.0),
            (-20.0, 40.0),
        ))
    

    @property
    def status(self):
        """Returns current state.
        
        """ 
        return _AMPLIFIER_STATE[self.switch.status][self.temperature_sensor.status]


    @property
    def is_on(self):
        """Returns true if switch state == 1."""
        return self.switch.is_on

    
    def switch_off(self):
        """Switches amplifier off - invoked when temperature sensor is in critical state.
        
        """
        self.switch.switch_off()