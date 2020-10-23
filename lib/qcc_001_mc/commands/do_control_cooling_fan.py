from qcc_001_mc import utils
from qcc_001_mc.instrument import INSTRUMENT



# Interval between which command will be executed.
_INTERVAL_SECONDS = 0.5


@utils.execute_on_interval(_INTERVAL_SECONDS)
def execute():
    """Checks AMP switch state & turns on cooling fan if necessary.
    
    """
    if INSTRUMENT.amplifer.is_on:
        if INSTRUMENT.cooling_fan.switch.is_off:
            INSTRUMENT.cooling_fan.switch.switch_on()
    else:
        if INSTRUMENT.cooling_fan.switch.is_on:
            INSTRUMENT.cooling_fan.switch.switch_off()

