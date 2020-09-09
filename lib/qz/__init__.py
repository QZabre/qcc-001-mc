from qz import commands
from qz import devices



def init():
    """Initialises instrument for use.
    
    """
    for device in devices.DEVICES:
        try:
            device.init
        except AttributeError:
            pass
        else:
            device.init()
