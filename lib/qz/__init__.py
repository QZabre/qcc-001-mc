from qz.instrument import INSTRUMENT
from qz import commands
from qz import components
from qz import utils


def setup():
    """Controller setup.
    
    """
    INSTRUMENT.init()
    commands.do_render_splash()
    commands.do_render_status()


def loop():
    """Controller event loop.
    
    """
    commands.do_check_amplifier_heat_stress()
    commands.do_process_serial_port_instruction()


# Setup controller, execute event loop, trap all errors.
setup()
while True:
    try:
        loop()
    except Exception as err:
        utils.logger.log_error(err)
