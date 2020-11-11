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
        self.cooling = components.Cooling()
        # self.display = components.Display()
        self.metadata = InstrumentMetaData()
        # self.temperature_sensor = components.TemperatureSensor(0x49, None)
        self.switch_map = {
            constants.SWITCH_AMP: self.amplifer.switch,
            constants.SWITCH_APD: self.apd.switch,
        }


    def __iter__(self):
        """Instance iterator.

        """
        return iter([
            self.amplifer,
            self.apd,
            self.cooling,
            # self.display,
            # self.temperature_sensor,
        ])


    def get_switch(self, key):
        """Returns a switch matched by key.
        
        :param key: Switch key.

        """
        try:
            return self.switch_map[key]
        except KeyError:
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
