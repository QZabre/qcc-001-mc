from qz import drivers



def execute():
    """Command execution entry point.
    
    """
    sensor = drivers.get_temperature_sensor("APD")

    print(sensor.temperature)
