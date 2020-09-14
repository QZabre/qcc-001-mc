class Apd():
    """Accelerated photon device.
    
    """
    def __init__(self, switch):
        """Instance constructor.
        
        """
        self.key = "APD"
        self.switch = switch
    

    @property
    def status(self):
        """Returns current state.
        
        """ 
        return 1 if self.switch.is_on else 0
