from qcc_001_mc.instrument import INSTRUMENT



def execute(key):
    """Queries a switch for it's current value.
    
    """
    switch = INSTRUMENT.get_switch(key)
    print(switch.value)
