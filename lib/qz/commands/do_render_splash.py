from qz import constants
from qz import drivers



def execute():
    """Renders splash screen.
    
    """
    display = drivers.get_display("MAIN")
    display.set_image(constants.IMG_SPLASH)
