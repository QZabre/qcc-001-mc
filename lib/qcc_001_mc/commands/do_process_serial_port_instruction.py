import supervisor

from qcc_001_mc import constants
from qcc_001_mc import commands



def _is_low_level(data):
    """Returns true if a low level instruction."""
    return data.count(':') == 2 and data[4] == ':'


def _is_switch_instruction(data):
    """Returns true if a switch instruction."""
    return _is_low_level(data) and \
           data[0:4] == "SOUR" and \
           data[5:9] == "DIGI" and \
           data[10:13] in constants.SWITCH_KEYS


def _is_control_switch(data):
    """Returns true if a control switch instruction."""
    return _is_switch_instruction(data) and not _is_query_switch(data)


def _is_query_temperature_of_amplifier(data):
    """Returns true if an amplifier temperature query instruction."""
    return _is_low_level(data) and \
           data[0:4] == "MEAS" and \
           data[5:9] == "TEMP" and \
           data[10:13] == "AMP"


def _is_query_idn(data):
    """Returns true if an idn query instruction."""
    return data == "*IDN?"


def _is_query_switch(data):
    """Returns true if an switch query instruction."""
    return _is_switch_instruction(data) and data[-1] == "?"


def _is_query_temperature_of_instrument(data):
    """Returns true if an temperature query instruction."""
    return _is_low_level(data) and \
           data[0:4] == "MEAS" and \
           data[5:9] == "TEMP"


def _get_command(data):
    """Parses a command recieved over serial port and returns command to be executed.

    :param instruction: Instrument control instruction.

    """
    if _is_query_idn(data):
        return commands.query_idn

    if _is_query_switch(data):
        return lambda: commands.query_switch(data[10:13])

    if _is_query_temperature_of_amplifier(data):
        return commands.query_amplifier_temperature

    if _is_query_temperature_of_instrument(data):
        return commands.query_temperature

    if _is_control_switch(data):
        return lambda: commands.do_control_switch(data[10:13], data[13])

    raise Exception(f"Serial Port command unsupported: {data}")


def execute():
    """Parses serial port instruction & executes appropriate sub-command.
    
    """
    # Escape if instruction is null.
    if not supervisor.runtime.serial_bytes_available:
        return

    # Decode instruction
    try:
        instruction = input().strip()
    except Exception as err:
        raise Exception("Serial Port command invalid")

    # Map instruction to command & execute.
    if instruction not in ["", "\n", "\r"]:
        command = _get_command(instruction)
        command()
