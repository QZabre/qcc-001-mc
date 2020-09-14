import qz



def setup():
    """Controller setup.
    
    """
    qz.INSTRUMENT.init()
    qz.commands.do_render_splash()
    qz.commands.do_render_status()


def loop():
    """Controller event loop.
    
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
