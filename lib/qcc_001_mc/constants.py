# Image: splash screen.
IMG_SPLASH = "splash.bmp"

# Instrument identifier.
INSTRUMENT_IDENTIFIER = "QCC-001"

# Instrument manafacturer.
INSTRUMENT_MANAFACTURER = "qcc_001_mcabre"

# Switch key: AMP.
SWITCH_AMP = "AMP"

# Switch key: APD.
SWITCH_APD = "APD"

# Switch keys.
SWITCH_KEYS = {
    SWITCH_AMP,
    SWITCH_APD,
}

# Switch state: on.
SWITCH_STATE_ON = 1

# Switch state: off.
SWITCH_STATE_OFF = 0

# Switch states.
SWITCH_STATES = {
    SWITCH_STATE_ON,
    SWITCH_STATE_OFF,
    }

# Temperature state: in standard operational range.
TEMPERATURE_STATE_OK = 0

# Temperature state: exceeds normal range but still operational.
TEMPERATURE_STATE_WARNING = 1

# Temperature state: exceeds operational range.
TEMPERATURE_STATE_CRITICAL = 9

# Temperature states.
TEMPERATURE_STATES = {
    TEMPERATURE_STATE_OK,
    TEMPERATURE_STATE_WARNING,
    TEMPERATURE_STATE_CRITICAL,
    }
