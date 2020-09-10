import supervisor
import time

import qz



def setup():
    """Controller setup.
    
    """
    # Initialise drivers.
    qz.drivers.init()

    # Display logo.
    qz.commands.do_render_splash()
    time.sleep(0.5)

    # Display initial state.
    qz.commands.do_render()


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
        qz.utils.logger.log_error(err)
