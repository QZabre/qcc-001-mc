from qz.instrument import INSTRUMENT



def execute():
    """Command execution entry point.
    
    """
    print(INSTRUMENT.temperature_sensor.temperature)
