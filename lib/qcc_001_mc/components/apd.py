import board

from qcc_001_mc import constants
from qcc_001_mc import components



class Apd():
    """Accelerated photon device.
    
    """
    def __init__(self):
        """Instance constructor.
        
        """
        self.switch = components.Switch(board.D9)


    @property
    def status(self):
        """Returns current state.
        
        """ 
        return 1 if self.switch.is_on else 0
