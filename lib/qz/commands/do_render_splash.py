import time

from qz import INSTRUMENT
from qz import constants



def execute():
    """Renders splash screen.
    
    """
    INSTRUMENT.display.set_image(constants.IMG_SPLASH)
    time.sleep(1.0)
