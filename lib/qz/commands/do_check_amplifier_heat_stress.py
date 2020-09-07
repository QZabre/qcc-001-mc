import time

from qz import commands
from qz import constants
from qz import devices
from qz import utils



# Internval between which teperature sesor will be analysed.
_INTERVAL_SECONDS = 0.5

# Threshold after which related device(s) temperature is considered unsafe and 
# instrument protected action needs to be taken.   
_TEMPERATURE_THRESHOLD = 27.0


@utils.execute_on_interval(_INTERVAL_SECONDS)
def execute():
    """Checks AMP temperature sensor for heat stress indication, if strressed then AMP is switched off.
    
    """
    # Escape if threshold not reached.
    if devices.amp_switch.is_off or \
       devices.amp_temperature_sensor.temperature < _TEMPERATURE_THRESHOLD:
        return

    # Emit log event.
    utils.logger.log_warning("AMP temperature safety threshold exceeded")

    # Switch off amplifier.
    commands.do_control_switch(constants.SWITCH_AMP, 0)

    # Re-render display.
    commands.do_render_switches()
