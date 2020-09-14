from qz import constants
from qz import components



class Apd():
    """Accelerated photon device.
    
    """
    def __init__(self):
        """Instance constructor.
        
        """
        self.switch = components.Switch(board.D13)


    @property
    def status(self):
        """Returns current state.
        
        """ 
        return 1 if self.switch.is_on else 0
