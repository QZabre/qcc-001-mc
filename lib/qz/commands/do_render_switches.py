from qz import devices
from qz import utils



def execute():
    """Renders current state of switches.
    
    """
    # From switches derive filename of bmp that represents state permutation, e.g. 01.
    fparts = "".join([str(int(i.value)) for i in devices.SWITCHES])
    fname = f"QCC{fparts}.bmp"

    # Render image.
    devices.display.set_image(fname)
