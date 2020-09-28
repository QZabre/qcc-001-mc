from qz import commands
from qz import utils
from qz.instrument import INSTRUMENT



# Interval between which teperature sesor will be analysed.
_INTERVAL_SECONDS = 0.5


@utils.execute_on_interval(_INTERVAL_SECONDS)
def execute():
    """Checks AMP temperature sensor for heat stress indication, if strressed then AMP is switched off.
    
    """
    if INSTRUMENT.amplifer.is_on:
        if INSTRUMENT.amplifer.is_overheated:
            _on_is_overheated()
        elif INSTRUMENT.amplifer.is_overheating:
            _on_is_overheating()


def _on_is_overheated():
    """Event handler: executed when temperature range is outside of critical range.
    
    """
    utils.logger.log_warning("AMP operational temperature safety threshold exceeded")
    INSTRUMENT.amplifer.switch_off()
    commands.do_render_status()


def _on_is_overheating():
    """Event handler: executed when temperature range is within warning range.
    
    """
    utils.logger.log_warning("AMP operational temperature safety threshold almost exceeded")
    commands.do_render_status()
