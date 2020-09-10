from qz import drivers



def execute(switch_key, value):
    """Sets value of a switch.
    
    """
    switch = drivers.get_switch(switch_key)
    switch.set_value(value)
