from qz.instrument import INSTRUMENT
from qz import commands
from qz import components
from qz import utils


def _setup():
    """Controller setup.
    
    """
    utils.logger.log("micro-controller initialisation: begins")

    INSTRUMENT.init()
    commands.do_render_splash()
    commands.do_render_status()

    utils.logger.log("micro-controller initialisation: complete")
    

def _loop():
    """Controller event loop.
    
    """
    def _on_loop():
        commands.do_check_amplifier_heat_stress()
        commands.do_process_serial_port_instruction()   
 
    utils.logger.log("micro-controller event loop: begins")
    while True:
        try:
            _on_loop()
        except Exception as err:
            utils.logger.log_error(err)
    utils.logger.log("micro-controller event loop: ends")


# Setup controller, execute event loop, trap all errors.
_setup()
_loop()
