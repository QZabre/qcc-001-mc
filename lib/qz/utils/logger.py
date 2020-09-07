from qz.utils.misc import get_datetime_as_iso_8601



# Set of supported logging levels.
LOG_LEVEL_DEBUG = 'DEBUG'
LOG_LEVEL_INFO = 'INFO'
LOG_LEVEL_WARNING = 'WARN'
LOG_LEVEL_ERROR = 'ERROR'
LOG_LEVEL_CRITICAL = 'CRITICAL'
LOG_LEVEL_FATAL = 'FATAL'
LOG_LEVEL_TODO = 'TODO'

# Text to display when passed a null message.
_NULL_MSG = '-------------------------------------------------------------------------------'


def log(msg=None, level=LOG_LEVEL_INFO):
    """Outputs a message to log.

    :param str msg: Message to be written to log.
    :param str level: Message level (e.g. INFO).

    """
    # TODO use structlog/logstash.
    print(_get_formatted_message(msg, level))


def log_error(err):
    """Logs a runtime error.

    :param str err: Error to be written to log.

    """
    msg = '!! RUNTIME ERROR !! :: '
    if issubclass(BaseException, err.__class__):
        msg += '{} :: {}'.format(err.__class__, err)
    else:
        msg += '{}'.format(err)
    log(msg, LOG_LEVEL_ERROR)


def log_todo(msg):
    """Outputs a todo message to log.

    :param str msg: Message to be written to log.

    """
    log(msg, LOG_LEVEL_TODO)


def log_warning(err):
    """Logs a runtime warning.

    :param str err: Error to be written to log.

    """
    if issubclass(BaseException, err.__class__):
        msg = '{} :: {}'.format(err.__class__, err)
    else:
        msg = '{}'.format(err)
    log(msg, LOG_LEVEL_WARNING)


def _get_formatted_message(msg, level):
    """Returns a message formatted for logging.

    """
    return _NULL_MSG if msg is None else \
           f"{get_datetime_as_iso_8601()} [{level}] :: QZABRE :: {str(msg).strip()}"

