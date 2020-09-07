from qz import devices



def execute(switch_key, value):
    """Sets value of a switch.
    
    """
    switch = devices.get_switch(switch_key)
    switch.set_value(value)
