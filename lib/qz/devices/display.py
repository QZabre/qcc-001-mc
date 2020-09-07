import board
import displayio
import terminalio

import adafruit_imageload
import adafruit_st7789
from adafruit_display_text.label import Label



# ST7789 TFT display.
_driver = None


def init():
    """Device initialiser.
    
    """
    global _driver

    # Release any resources currently in use for the displays
    displayio.release_displays()

    # Instantiate & configure device.
    _driver = adafruit_st7789.ST7789(
        displayio.FourWire(
            board.SPI(),
            command=board.A4,
            chip_select=board.A5,
        ),
        width=240,
        height=240,
        rowstart=80
        )


def set_splash():
    """Renders splash screen.
    
    """
    BG_COLOR = 0x00FF00    # Silver
    FG_COLOR = 0xC0C0C0    # Silver
    TEXT_COLOR = 0xFFFF00    # Silver

    def get_background_sprite():
        color_bitmap = displayio.Bitmap(240, 240, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = BG_COLOR  # Bright Green

        return displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

    def get_inner_rectangle():
        inner_bitmap = displayio.Bitmap(200, 200, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = FG_COLOR    # Silver

        return displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=20, y=20)

    def get_label():
        text_group = displayio.Group(max_size=10, scale=2, x=50, y=120)
        text = "Hello QZabre !"
        text_area = Label(terminalio.FONT, text=text, color=TEXT_COLOR)
        text_group.append(text_area)  # Subgroup for text scaling

        return text_group

    def get_splash():
        group = displayio.Group(max_size=10)
        for sub_group in [
            get_background_sprite,
            get_inner_rectangle,
            get_label,
        ]:
            group.append(sub_group())
        
        return group

    _driver.show(get_splash())


def set_image(fname: str):
    """Renders an image.

    :param fname: Name of image within ./assets/img folder to load.

    """
    # Load image.
    bitmap, palette = adafruit_imageload.load(
        f"assets/img/{fname}",
        bitmap=displayio.Bitmap,
        palette=displayio.Palette
        )

    # Create a TileGrid to hold the bitmap
    tile_grid = displayio.TileGrid(
        bitmap,
        pixel_shader=palette,
        x=0,
        y=0
        )

    # Create a Group to hold the TileGrid
    group = displayio.Group()

    # Add the TileGrid to the Group
    group.append(tile_grid)

    _driver.show(group)
