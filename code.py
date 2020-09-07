import supervisor
import time

import qz
from qz import utils


def setup():
    """Controller setup.
    
    """
    # Initialise instrument.
    qz.init()

    # Display logo.
    qz.commands.do_render_splash()
    time.sleep(0.5)

    # Display initial switch state.
    qz.commands.do_render_switches()


def loop():
    """Executed each time controller event loop fires.
    
    """
    qz.commands.do_check_amplifier_heat_stress()
    qz.commands.do_process_serial_port_instruction()


# Setup controller, execute event loop, trap all errors.
setup()
while True:
    try:
        loop()
    except Exception as err:
        utils.logger.log_error(err)
