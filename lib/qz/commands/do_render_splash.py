import time

from qz import constants
from qz.instrument import INSTRUMENT



def execute():
    """Renders splash screen.
    
    """
    INSTRUMENT.display.set_image(constants.IMG_SPLASH)
    time.sleep(1.0)
