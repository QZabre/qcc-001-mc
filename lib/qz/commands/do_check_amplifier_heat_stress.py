import time

from qz import commands
from qz import constants
from qz import drivers
from qz import utils



# Internval between which teperature sesor will be analysed.
_INTERVAL_SECONDS = 0.5

# Operational temperature range.
_TEMPERATURE_RANGE = (
    (-25.0, 45.0),
    (-20.0, 40.0),
)


@utils.execute_on_interval(_INTERVAL_SECONDS)
def execute():
    """Checks AMP temperature sensor for heat stress indication, if strressed then AMP is switched off.
    
    """
    # Set drivers.
    switch = drivers.get_switch(constants.SWITCH_AMP)
    temperature_sensor = drivers.get_temperature_sensor("AMP")
        
    # Escape if switched off.
    if switch.is_off:
        return

    # Process amplifier temperature:    
    # ... temperature is in critical state
    temperature_sensor.set_state_if_outside_of_range(
        _TEMPERATURE_MIN_CRITICAL,
        _TEMPERATURE_MAX_CRITICAL,
        constants.TEMPERATURE_STATE_CRITICAL,
    )

    if temperature_sensor.state != constants.TEMPERATURE_STATE_CRITICAL

    if not temperature_sensor.is_in_range(_TEMPERATURE_MIN, _TEMPERATURE_MAX):
        _on_critical()

    # ... temperature is in warning state
    elif not temperature_sensor.is_in_range(_TEMPERATURE_MIN_WARNING, _TEMPERATURE_MAX_WARNING):
        _on_warning()
    

def _on_warning():
    """Event handler: executed when temperature range is within warning range.
    
    """
    # Emit log event.
    utils.logger.log_warning("AMP operational temperature safety threshold almost exceeded")

    # Re-render display.
    commands.do_render()


def _on_critical():
    """Event handler: executed when temperature range is outside of critical range.
    
    """
    # Emit log event.
    utils.logger.log_warning("AMP operational temperature safety threshold exceeded")

    # Switch off amplifier & re-render display.
    commands.do_control_switch(constants.SWITCH_AMP, 0)
    commands.do_render()
