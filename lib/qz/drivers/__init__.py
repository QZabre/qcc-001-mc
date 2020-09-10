import board

from qz import constants
from qz.drivers.display import Display
from qz.drivers.switch import Switch
from qz.drivers.temperature_sensor import TemperatureSensor



# Full set of instrument drivers.
_DRIVERS = [
    # ... TFT display
    Display("MAIN"),

    # ... amplifier switch
    Switch(constants.SWITCH_AMP, board.D13),

    # ... apd switch
    Switch(constants.SWITCH_APD, board.D9),

    # ... amplifier temperature sensor
    TemperatureSensor("AMP", 0x48, (
        (-25.0, 45.0),
        (-20.0, 40.0),
    )),

    # ... ??? temperature sensor
    TemperatureSensor("APD", 0x49, None),
]


def get_display(key):
    """Returns a display matched by key.
    
    :param key: Display key.

    """
    return _get_driver(Display, key)


def get_switch(key):
    """Returns a switch matched by key.
    
    :param key: Switch key.

    """
    return _get_driver(Switch, key)


def get_switches():
    """Returns full set of switches.
    
    """
    return [i for i in _DRIVERS if isinstance(i, Switch)]


def get_temperature_sensor(key):
    """Returns a temperature sensor matched by key.
    
    :param key: Temperature sensor key.

    """
    return _get_driver(TemperatureSensor, key)


def init():
    """Initialises drivers for use.
    
    """
    for driver in _DRIVERS:
        try:
            driver.init
        except AttributeError:
            pass
        else:
            driver.init()


def _get_driver(typeof, key):
    """Returns a driver matched by type & key.
    
    :param typeof: Device type, i.e. class that wraps driver.
    :param key: Device key.

    """
    for driver in _DRIVERS:
        if isinstance(driver, typeof) and driver.key == key:
            return driver

    raise ValueError(f"Invalid driver reference: {typeof} :: {key}")
