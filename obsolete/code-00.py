# Write your code here :-)

import board
import busio
import digitalio
import supervisor
import time

# Constants for easier reference

# Amplifier
AMP = 0

# APD
APD = 1

# Cooling
COOL = 2

# 12 volt supplement
TWELVE = 3

# 5 volt output
LASER = 4


# Read/write channel values
def DoSwitch(channel, read, value):
    # case write
    if read == 0:
        if channel == AMP:
            SwitchRF.value = value
        elif channel == APD:
            SwitchAPD.value = value
        elif channel == COOL:
            SwitchCool.value = value
        elif channel == TWELVE:
            Switch12.value = value
        elif channel == LASER:
            SwitchLaser.value = value
        return value
    else:
        #case read
        if channel == AMP:
            return SwitchRF.value
        elif channel == APD:
            return SwitchAPD.value
        elif channel == COOL:
            return SwitchCool.value
        elif channel == TWELVE:
            return Switch12.value
        elif channel == LASER:
            return SwitchLaser.value

# set up all the switches
SwitchRF = digitalio.DigitalInOut(board.D13)
SwitchRF.direction = digitalio.Direction.OUTPUT
SwitchRF.value = False

SwitchAPD = digitalio.DigitalInOut(board.D9)
SwitchAPD.direction = digitalio.Direction.OUTPUT
SwitchAPD.value = False

SwitchCool = digitalio.DigitalInOut(board.D10)
SwitchCool.direction = digitalio.Direction.OUTPUT
SwitchCool.value = False

Switch5 = digitalio.DigitalInOut(board.D5)
Switch5.direction = digitalio.Direction.OUTPUT
Switch5.value = False

Switch12 = digitalio.DigitalInOut(board.D6)
Switch12.direction = digitalio.Direction.OUTPUT
Switch12.value = False

print("ready")
# main loop
while True:

    # wait for input command

    if supervisor.runtime.serial_bytes_available:
        # block to CR/LF (don't know which)
        value = input().strip()

        # check for * as high level command
        if value[0] == '*':
            # check if known
            if value[1:5] == 'IDN?':
                print("QCC 1")
            else:
                print("Error: unknown *command")

        else:
            # only accept SCPI style with two semicolons, 4 characters at beginning
            ok = 0
            if value.count(':') == 2 and value[4] == ':':
                print(value[12])
                if value[0:4] == "MEAS":
                    if value[5:9] == "TEMP":
                        print("temp is ")
                        ok=1

                # Source
                elif value[0:4] == "SOUR":
                    # Digital in/out
                    if value[5:9] == "DIGI":
                        # 
                        if value[10:13] == "LAS":
                            channel = LASER
                        elif value[10:13] == "AMP":
                            channel = AMP
                        elif value[10:13] == "COO":
                            channel = COOL
                        elif value[10:13] == "APD":
                            channel = APD
                        elif value[10:13] == "TWE":
                            channel = TWELVE
                        else:
                            channel = -1
        
                        if value[13] == '?':
                            read = 1
                        else:
                            read = 0
                            value = value[14]
    
                        if channel >0:
                            ok=1
                            print(DoSwitch(channel, read, value))

            if ok == 0:
                print("Error: unknown command: " + value)
