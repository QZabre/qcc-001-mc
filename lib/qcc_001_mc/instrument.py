from qcc_001_mc import constants
from qcc_001_mc import components



class InstrumentMetaData():
    """Encapsulates instrument metadata.
    
    """
    def __init__(self):
        """Instance constructor.
        
        """
        self.manafacturer = constants.INSTRUMENT_MANAFACTURER
        self.identifier = constants.INSTRUMENT_IDENTIFIER


class Instrument():
    """Encapsulates the instrument plus associated commands + components.
    
    """
    def __init__(self):
        """Instance constructor.
        
        """
        self.amplifer = components.Amplifier()
        self.apd = components.Apd()
        self.cooling_fan = components.CoolingFan()
        self.display = components.Display()
        self.metadata = InstrumentMetaData()
        self.temperature_sensor = components.TemperatureSensor(0x49, None)


    def __iter__(self):
        """Instance iterator.

        """
        return iter([
            self.amplifer,
            self.apd,
            self.display,
            self.temperature_sensor,
        ])


    def get_switch(self, key):
        """Returns a switch matched by key.
        
        :param key: Switch key.

        """
        if key == constants.SWITCH_AMP:
            return self.amplifer.switch
        if key == constants.SWITCH_APD:
            return self.apd.switch

        raise KeyError(f"Invalid switch key: :: {key}")


    def init(self):
        """Initialises drivers for use.
        
        """
        for component in self:
            try:
                component.init
            except AttributeError:
                pass
            else:
                component.init()


# Singleton.
INSTRUMENT = Instrument()
