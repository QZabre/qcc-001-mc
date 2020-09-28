from qz.instrument import INSTRUMENT



def execute():
    """Command execution entry point.
    
    """
    print(f"{INSTRUMENT.metadata.manafacturer} {INSTRUMENT.metadata.identifier}")
