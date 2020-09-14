from qz import INSTRUMENT



def execute(switch_key, value):
    """Sets value of a switch.
    
    """
    switch = INSTRUMENT.get_switch(switch_key)
    switch.set_value(value)
