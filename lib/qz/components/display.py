import board
import displayio
import terminalio

import gc

import adafruit_imageload
import adafruit_st7789



# NOTE: this is a hack to get things up and running - it 
#       will be removed once system if fully functional.
_bitmap = displayio.Bitmap(240, 240, 1)
_palette = displayio.Palette(1)
_palette[0] = 0x000000


class Display():
    """Wraps a TFT display driver.

    """
    def __init__(self, key):
        """Constructor.
        
        :param key: Device key used for disambiguation purposes.

        """
        self.key = key
        self._driver = None


    def init(self):
        """Device initialiser.
        
        """
        # Release any display resources currently in use.
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
        # Flush memory in advance.
        self._flush()

        # Set bitmap.
        bitmap, palette = adafruit_imageload.load(
            f"assets/img/{fname}",
            bitmap=displayio.Bitmap,
            palette=displayio.Palette,
            )

        # Set tile grid.
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette, x=0, y=0)

        # Set group.
        group = displayio.Group(max_size=10)
        group.append(tile_grid)

        # Render.
        self._driver.show(group)


    def _flush(self):
        """Flushes display in readiness for rendering an image.
        
        """
        # NOTE: this is a hack to get things up and running - it 
        #       will be removed once system if fully functional.

        def get_background_sprite():
            color_bitmap = displayio.Bitmap(240, 240, 1)
            color_palette = displayio.Palette(1)
            color_palette[0] = 0x000000  # Bright Green

            return displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

        def get_group():
            group = displayio.Group()
            group.append(get_background_sprite())

            return group

        self._driver.show(get_group())
        gc.collect()
