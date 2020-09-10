from qz import drivers



def execute(switch_key):
    """Queries a switch for it's current value.
    
    """
    switch = drivers.get_switch(switch_key)
    print(switch.value)
