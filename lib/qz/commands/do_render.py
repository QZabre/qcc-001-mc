from qz import drivers
from qz import utils



def execute():
    """Renders current state of switches.
    
    """
    # Set drivers.
    display = drivers.get_display("MAIN")
    switches = drivers.get_switches()

    # Derive filename of bmp that represents state permutation, e.g. 01.
    fparts = "".join([str(int(i.value)) for i in switches])
    fname = f"QCC{fparts}.bmp"

    # Render image.
    display.set_image(fname)
