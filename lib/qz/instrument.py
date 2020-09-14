from qz import constants
from qz import components



class Instrument():
    """Encapsulates the instrument plus associated commands + components.
    
    """
    def __init__(self):
        """Instance constructor.
        
        """
        self.amplifer = components.Amplifier()
        self.apd = components.Apd()
        self.display = components.Display()
        self.metadata = InstrumentMetaData()
        self.temperature_sensor = components.TemperatureSensor("MAIN", 0x49, None)


    def __iter__(self):
        """Instance iterator.

        """
        return iter([
            self.amplifer,
            self.apd,
            self.display,
            self.temperature_sensor,
        ])


    @property
    def switches(self):
        """Returns set of associated switches."""
        return [
            self.amplifer.switch,
            self.apd.switch,
        ]


    def get_switch(self, key):
        """Returns a switch matched by key.
        
        :param key: Switch key.

        """
        try:
            return self.switches[key]
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


class InstrumentMetaData():
    """Encapsulates instrument metadata.
    
    """
    def __init__(self):
        """Instance constructor.
        
        """
        self.manafacturer = constants.INSTRUMENT_MANAFACTURER
        self.identifier = constants.INSTRUMENT_IDENTIFIER