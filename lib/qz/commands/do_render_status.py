from qz import INSTRUMENT



# Map: from system state to image file.
_MAP_STATE_IMG = {
    "00": "_01.bmp",
    "01": "_01.bmp",
    "10": "_02.bmp",
    "11": "_02.bmp",
    "20": "_03.bmp",
    "21": "_03.bmp",
    "30": "_04.bmp",
    "31": "_04.bmp",
    "40": "_05.bmp",
    "41": "_05.bmp",
    "50": "_06.bmp",
    "51": "_06.bmp",
}

# Defualt image to display - should never be used.
_DEFAULT_IMG = "_01.bmp"


def execute():
    """Renders current state of switches.
    
    """
    # Set name of image file to render.
    fname = _MAP_STATE_IMG.get(f"{components.amplifer.status}{components.apd.status}.bmp", _DEFAULT_IMG)

    # Render image.
    INSTRUMENT.display.set_image(fname)
