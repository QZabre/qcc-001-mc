from qz.instrument import INSTRUMENT



# Map: from system state to image file.
_MAP_STATE_IMG = {
    # Amp on & temp OK. Apd off.
    "00": "QCC_00.bmp",

    # Amp on & temp OK. Apd on.
    "01": "QCC_01.bmp",

    # Amp on & temp warning. Apd off.
    "10": "QCC_10.bmp",

    # Amp on & temp warning. Apd on.
    "11": "QCC_11.bmp",

    # Amp on & temp critical. Apd on.
    # Note - should never be in this state.
    "20": "_03.bmp",

    # Amp on & temp critical. Apd off.
    # Note - should never be in this state.
    "21": "_03.bmp",

    # Amp off & temp ok. Apd off.
    "30": "_04.bmp",

    # Amp off & temp ok. Apd on.
    "31": "_04.bmp",

    # Amp off & temp warning. Apd off.
    "40": "QCC_40.bmp",

    # Amp off & temp warning. Apd on.
    "41": "QCC_41.bmp",

    # Amp off & temp critical. Apd off.
    "50": "QCC_50.bmp",

    # Amp off & temp critical. Apd on.
    "51": "QCC_51.bmp",
}

# Defualt image to display - should never be used.
_DEFAULT_IMG = "_01.bmp"


def execute():
    """Renders current state of switches.
    
    """
    # Map system state to image file.
    status_amp = components.amplifer.status
    status_apd = components.apd.status
    fname = _MAP_STATE_IMG.get(f"{status_amp}{status_apd}.bmp", _DEFAULT_IMG)

    # Render image.
    INSTRUMENT.display.set_image(fname)
