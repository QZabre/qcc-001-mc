from qcc_001_mc import constants
from qcc_001_mc import utils
from qcc_001_mc.instrument import INSTRUMENT



# Map: from system state to image file.
_MAP_STATE_IMG = {
    # Amp off. Amp temp OK. Apd off.
    "00_0": "QCC-001-00-0.bmp",

    # Amp off. Amp temp warning. Apd off.
    "01_0": "QCC-001-01-0.bmp",

    # Amp off. Amp temp critical. Apd off.    
    "02_0": "QCC-001-02-0.bmp",
    
    # Amp on. Amp temp OK. Apd off.
    "10_0": "QCC-001-10-0.bmp",

    # Amp on. Amp temp warning. Apd off.
    "11_0": "QCC-001-11-0.bmp",

    # Amp off. Amp temp OK. Apd on.
    "00_1": "QCC-001-00-1.bmp",

    # Amp off. Amp temp warning. Apd on.
    "01_1": "QCC-001-01-1.bmp",

    # Amp off. Amp temp critical. Apd on.    
    "02_1": "QCC-001-02-1.bmp", 

    # Amp on. Amp temp OK. Apd on.
    "10_1": "QCC-001-10-1.bmp",

    # Amp on. Amp temp warning. Apd on.
    "11_1": "QCC-001-11-1.bmp",    
}


def execute():
    """Renders current state of switches.
    
    """
    # Set system state.
    state = f"{INSTRUMENT.amplifer.status}_{INSTRUMENT.apd.status}"

    # Set image.
    try:
        img = _MAP_STATE_IMG[state]
    except KeyError:
        img = constants.IMG_SPLASH
        utils.logger.log_warning(f"instrument state could not be mapped to an image: {state}")
    
    # Render image.
    try:
        INSTRUMENT.display.set_image(img)
    except:
        pass
