import board
import busio

from qz import constants
from qz.devices import display
from qz.devices.switch import Switch
from qz.devices.temperature_sensor import TemperatureSensor



# I2C Bus - drives temperature sensors.
i2c_bus = busio.I2C(board.SCL, board.SDA)

# AMP device switch.
amp_switch = Switch(constants.SWITCH_AMP, board.D13)

# AMP device temperature sensor.
amp_temperature_sensor = TemperatureSensor(i2c_bus, 0x48)

# APD device switch.
apd_switch = Switch(constants.SWITCH_APD, board.D9)

# Instrument temperature sensor.
temperature_sensor = TemperatureSensor(i2c_bus, 0x49)

# Collection: instrument switches.
SWITCHES = [
    amp_switch,
    apd_switch,
]

# Collection: instrument devices.
DEVICES = SWITCHES + [
    amp_temperature_sensor,
    display,
    temperature_sensor,
]


def get_switch(key):
    """Returns first switch that matches a key.
    
    :param key: Switch key.

    """
    for switch in SWITCHES:
        if switch.key == key:
            return switch

    raise KeyError(f"Invalid switch key: {key}")
