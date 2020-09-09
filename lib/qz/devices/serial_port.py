from qz import commands
from qz import constants




def _is_high_level(data):
    """Returns true if a high level instruction."""
    return data[0] == "*"


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


def _is_query_idn(data):
    """Returns true if an idn query instruction."""
    return _is_high_level(data) and data[1:5] == "IDN?"


def _is_query_switch(data):
    """Returns true if an switch query instruction."""
    return _is_switch_instruction(data) and data[13] == "?"


def _is_query_temperature(data):
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

    if _is_query_temperature(data):
        return commands.query_temperature

    if _is_control_switch(data):
        return lambda: commands.do_control_switch(data[10:13], data[13])

    raise Exception(f"Serial Port command unsupported: {data}")


def execute_instruction(instruction):
    """Executes an instruction recieved over serial port.

    :param instruction: Instrument control instruction.

    """
    # Map instruction to a supported command.
    command = _get_command(instruction)

    # Execute command.
    command()
