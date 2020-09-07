import supervisor

from qz.devices import serial_port



def execute():
    """Parses serial port instruction & executes appropriate sub-command.
    
    """
    # Escape if instruction is null.
    if not supervisor.runtime.serial_bytes_available:
        return

    # Escape if instruction is terminate.
    sp_instruction = input().strip()
    if sp_instruction in ["\n", "\r"]:
        return

    # Map instruction to supported command & execute.
    serial_port.execute_instruction(sp_instruction)
