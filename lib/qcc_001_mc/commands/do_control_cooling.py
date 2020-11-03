import time

from qcc_001_mc.instrument import INSTRUMENT



def execute():
    """Checks AMP switch state & turns on cooling fan if necessary.
    
    """
    INSTRUMENT.cooling.switch_on()
    time.sleep(0.1)
