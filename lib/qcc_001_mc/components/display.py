import gc

import board
import displayio
import terminalio

import adafruit_imageload
import adafruit_st7789



# NOTE: this is a hack to get things up and running - it 
#       will be removed once system if fully functional.
_bitmap = displayio.Bitmap(240, 240, 1)   



class Display():
    """Wraps a TFT display driver.

    """
    def __init__(self):
        """Constructor.
        
        """
    
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
            f"lib/qcc_001_mc/assets/img/{fname}",
            bitmap=displayio.Bitmap,
            palette=displayio.Palette,
            )

        # Create a TileGrid to hold the bitmap
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

        # Create a Group to hold the TileGrid
        group = displayio.Group()

        # Add the TileGrid to the Group
        group.append(tile_grid)

        # Add the Group to the Display
        self._driver.show(group)


    def _flush(self):
        """Flushes display in readiness for rendering an image.
        
        """
        # NOTE: this is a hack to get things up and running - it 
        #       will be removed once system if fully functional.
        group = displayio.Group()
        group.append(displayio.TileGrid(
            displayio.Bitmap(240, 240, 1), 
            pixel_shader=displayio.Palette(1)
            ))
        self._driver.show(group)
        
        gc.collect()
