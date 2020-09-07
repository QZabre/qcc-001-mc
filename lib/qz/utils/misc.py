import time



def get_datetime_as_iso_8601():
    """Returns local datetime in iso 8601 format.
    
    """
    now = time.localtime()

    return f"{now.tm_year}-{now.tm_mon:02}-{now.tm_mday:02}T{now.tm_hour:02}:{now.tm_min:02}:{now.tm_sec:02}"


# Timer to use when applying excution interval.
# TODO: should be moved inside decorator.
_EXECUTION_TIMER = None

def execute_on_interval(interval_seconds):
    """Decorator to execute inner function every N seconds.
    
    """
    def decorator(func):

        def wrapper() :
            global _EXECUTION_TIMER

            # Initialise time on first pass.
            if _EXECUTION_TIMER is None:
                _EXECUTION_TIMER = time.monotonic()
                return

            # Once trigger interval is surpassed then execute business logic.
            if time.monotonic() - _EXECUTION_TIMER >= interval_seconds:
                _EXECUTION_TIMER = None

                return func()

        return wrapper

    return decorator
