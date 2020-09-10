import board
import displayio

import adafruit_imageload
import adafruit_st7789



class Display():
    """Wraps a TFT display driver.

    """
    def __init__(self, key):
        """Constructor.
        
        :param key: Device key used for disambiguation purposes.

        """
        self.key = key
        self._driver = None
        self._img_group = None


    def init(self):
        """Device initialiser.
        
        """
        # Release any resources currently in use for the displays
        displayio.release_displays()

        # Instantiate & configure driver.
        self._driver = adafruit_st7789.ST7789(
            displayio.FourWire(
                board.SPI(),
                command=board.A4,
                chip_select=board.A5,
            ),
            width=240,
            height=240,
            rowstart=80
            )

        
    def set_image(self, fname):
        """Renders an image within display.
        
        """
        # Unset previous image.
        if self._img_group is not None:
            self._img_group.pop()
        
        # Set bitmap.
        fpath = f"assets/img/{fname}"
        bitmap, palette = adafruit_imageload.load(fpath)
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0)

        # Set group.
        if self._img_group is None: 
            self._img_group = displayio.Group()
        self._img_group.append(tile_grid)

        # Render.
        _driver.show(_image_group)
