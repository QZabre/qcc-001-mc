from qz import devices



def execute(switch_key):
    """Queries a switch for it's current value.
    
    """
    switch = devices.get_switch(switch_key)

    return switch.value
