import board

from qcc_001_mc import constants
from qcc_001_mc import components



class Cooling():
    """Cooling sub-system.

    NOTE: At present this wraps a simple on/off switch that controls both a pump & fan.  
          However in due course this will mutate to a gradiated control mechanism.
    
    """
    def __init__(self):
        """Instance constructor.
        
        """
        self.switch = components.Switch(board.D10)


    @property
    def status(self):
        """Returns current state.
        
        """ 
        return 1 if self.switch.is_on else 0
