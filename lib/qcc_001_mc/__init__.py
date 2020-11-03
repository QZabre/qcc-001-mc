import supervisor

from qcc_001_mc.instrument import INSTRUMENT
from qcc_001_mc import commands
from qcc_001_mc import components
from qcc_001_mc import utils


def _setup():
    """Controller setup.
    
    """
    INSTRUMENT.init()
    for cmd in (
        commands.do_control_cooling,
        commands.do_render_splash,
        commands.do_render_status,
    ):
        try:
            cmd()
        except Exception as err:
            utils.logger.log_error(err)


def _loop():
    """Controller event loop.
    
    """
    utils.logger.log("micro-controller event loop: begins")
    while True:
        for cmd in (
            commands.do_check_amplifier_heat_stress,
            commands.do_process_serial_port_instruction
        ):
            try:
                cmd()
            except Exception as err:
                utils.logger.log_error(err)


# Setup controller, execute event loop - trap all errors.
_setup()
_loop()
