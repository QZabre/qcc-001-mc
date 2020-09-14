from qz import INSTRUMENT



def execute(switch_key):
    """Queries a switch for it's current value.
    
    """
    switch = INSTRUMENT.get_switch(switch_key)
    print(switch.value)
