from qcc_001_mc.instrument import INSTRUMENT



def execute():
    """Command execution entry point.
    
    """
    print(INSTRUMENT.amplifer.temperature_sensor.temperature)
