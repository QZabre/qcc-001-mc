import pulseio



class _Fan():
    """Instrument cooling fan.

    """
    def __init__(self, pin):
        """Instance constructor.
        
        """
        self._driver = pulseio.PWMOut(
            board.D10,
            duty_cycle=0x6fff,
            frequency=10000,
            )


class _WaterPump():
    """Instrument cooling pump.

    """
    def __init__(self, pin):
        """Instance constructor.
        
        """
        pass
        # self._driver = pulseio.PWMOut(
        #     board.D10,
        #     duty_cycle=0x6fff,
        #     frequency=10000,
        #     )
    

class Cooling():
    """Instrument cooling mechanism.

    """
    def __init__(self, pin_fan, pin_pump):
        """Instance constructor.
        
        """
        self.fan = _Fan(pin_fan)
        self.waterpump = _WaterPump(pin_pump)


    def set_output(self, percentage):
        """Increases cooling output in response to overheating.
        
        """  
        print(f"TODO: set cooling output: {percentage}")      
