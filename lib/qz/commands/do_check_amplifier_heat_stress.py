import time

from qz import commands
from qz import constants
from qz import devices
from qz import utils



# Internval between which teperature sesor will be analysed.
_INTERVAL_SECONDS = 0.5

# Threshold after which related device(s) temperature is considered unsafe and 
# instrument protected action needs to be taken.   
_TEMPERATURE_MAX = 45.0

# Threshold after which related device(s) temperature is considered unsafe and 
# instrument protected action needs to be taken.   
_TEMPERATURE_MIN = -20.0

@utils.execute_on_interval(_INTERVAL_SECONDS)
def execute():
    """Checks AMP temperature sensor for heat stress indication, if strressed then AMP is switched off.
    
    """
    # Escape if device is off.
    if devices.amp_switch.is_off:
        return

    # Escape if within acceptable operating temperature range.    
    if devices.amp_temperature_sensor.is_in_range(_TEMPERATURE_MIN, _TEMPERATURE_MAX):
        return

    # Emit log event.
    utils.logger.log_warning("AMP operational temperature safety threshold exceeded")

    # Switch off amplifier & re-render display.
    commands.do_control_switch(constants.SWITCH_AMP, 0)
    commands.do_render_switches()
