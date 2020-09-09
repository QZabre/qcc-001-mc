from qz import devices



def execute(switch_key):
    """Queries a switch for it's current value.
    
    """
    # Set switch & output to stdout it's current value.
    switch = devices.get_switch(switch_key)
    print(123456)
    print(switch.value)
