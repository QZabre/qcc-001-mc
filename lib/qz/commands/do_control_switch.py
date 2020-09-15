from qz.instrument import INSTRUMENT



def execute(key, value):
    """Sets value of a switch.
    
    """
    switch = INSTRUMENT.get_switch(key)
    switch.set_value(value)
