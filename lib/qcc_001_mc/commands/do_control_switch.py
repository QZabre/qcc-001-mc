from qcc_001_mc import commands
from qcc_001_mc import utils
from qcc_001_mc.instrument import INSTRUMENT



def execute(key: str, value: int):
    """Sets value of a switch.
    
    """
    switch = INSTRUMENT.get_switch(key)
    switch.set_value(value)
    commands.do_render_status()
