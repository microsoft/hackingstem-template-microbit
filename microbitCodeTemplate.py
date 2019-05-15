# ------------__ Hacking STEM astro_socks.py micro:bit __-----------
#  For use with the TODO:[Add lesson title] 
#  lesson plan available from Microsoft Education Workshop at 
#  http://aka.ms/hackingSTEM
#
#  Overview: [One to two sentence project description]
# 
#  Pins:
#    [Description of pin connections]
#  
#  This project uses a BBC micro:bit microcontroller, information at:
#  https://microbit.org/
#
#  Comments, contributions, suggestions, bug reports, and feature
#  requests are welcome! For source code and bug reports see:
#  http://github.com/[TODO github path to Hacking STEM]
#
#  Copyright 2019, [Primary Engineer Name]
#  Microsoft EDU Workshop - HackingSTEM
#  MIT License terms detailed in LICENSE.txt
# ===---------------------------------------------------------------===

from microbit import *

# Setup & Config
display.off()  # Turns off LEDs to free up additional input pins
uart.init(baudrate=9600)  # Sets serial baud rate
DATA_RATE = 10 # Frequency of code looping
EOL = '\n' # End of Line Character
chan = 0 # Defualt channel number for radio

# These constants are the pins used on the micro:bit for the sensors
SENSOR_ONE = pin0
SENSOR_TWO = pin1


def process_sensors():
    # TO DO: Describe what this function does 
    global sensor_one_reading, sensor_two_reading
    sensor_one_reading = SENSOR_ONE.read_analog()
    sensor_two_reading = SENSOR_TWO.read_analog()
   

#=============================================================================#
#---------------The Code Below Here is for Excel Communication----------------#
#=============================================================================#

# Array to hold the serial data
parsedData = [0] * 5

def getData():
    #   This function gets data from serial and builds it into a string
    global parsedData, builtString
    builtString = ""
    while uart.any() is True:
        byteIn = uart.read(1)
        if byteIn == b'\n':
            continue
        byteIn = str(byteIn)
        splitByte = byteIn.split("'")
        builtString += splitByte[1]
    parseData(builtString)
    return (parsedData)


def parseData(s):
    #   This function seperates the string into an array
    global parsedData
    if s != "":
        parsedData = s.split(",")

#=============================================================================#
#------------------------------Main Program Loop------------------------------#
#=============================================================================#
while (True):
    process_sensors()
    serial_in_data = getData()

    # Create a string of the data to be sent
    data_to_send = ",{},{}".format(sensor_one_reading, sensor_two_reading)

    if (serial_in_data[0] != "#pause"):
        # uart is the micro:bit command for serial
        uart.write(data_to_send + EOL)

    sleep(DATA_RATE)
