from qz.instrument import INSTRUMENT



# Map: from system state to image file.
_MAP_STATE_IMG = {
    # Amp off & temp OK. Apd off.
    "00": "_01.bmp",

    # Amp off & temp OK. Apd on.
    "01": "_01.bmp",

    # Amp on & temp warning. Apd off.
    "10": "_02.bmp",

    # Amp on & temp warning. Apd on.
    "11": "_02.bmp",

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
    "40": "_05.bmp",

    # Amp off & temp warning. Apd on.
    "41": "_05.bmp",

    # Amp off & temp crticial. Apd off.
    "50": "_06.bmp",

    # Amp off & temp crticial. Apd on.
    "51": "_06.bmp",
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
