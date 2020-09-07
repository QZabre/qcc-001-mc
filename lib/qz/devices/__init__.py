import board

from qz import constants
from qz.devices import display
from qz.devices import serial_port
from qz.devices.switch import Switch
from qz.devices.temperature_sensor import TemperatureSensor



# AMP device switch.
amp_switch = Switch(constants.SWITCH_AMP, board.D13)

# AMP device temperature sensor.
amp_temperature_sensor = TemperatureSensor(0x48, board.SCL, board.SDA)

# APD device switch.
apd_switch = Switch(constants.SWITCH_APD, board.D9)

# Instrument temperature sensor.
temperature_sensor = TemperatureSensor(0x4A)

# Collection: instrument switches.
SWITCHES = [
    amp_switch,
    apd_switch,
]

# Collection: instrument devices.
DEVICES = SWITCHES + [
    amp_temperature_sensor,
    display,
    serial_port,
    temperature_sensor,
]


def get_switch(key):
    """Returns first switch that matches a key.
    
    :param key: Switch key.

    """
    for switch in _SWITCHES:
        if switch.key == key:
            return switch

    raise KeyError(f"Invalid switch key: {key}")
