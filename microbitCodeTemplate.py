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

# Frequency of main loop executing, in milliseconds
EXECUTION_INTERVAL = 10 

# Array to hold the serial data
last_parsed_data = None

# time main loop was last executed
last_executed = 0

# Initializes serial to 9600 baud rate
uart.init(baudrate=9600)  


#=============================================================================#
#---------------The Code Below Here is for Excel Communication----------------#
#=============================================================================#


def retrieve_columns_from_uart():
    ''' returns array of columns from serial
        or None if nothing available
    '''
    if uart.any():
        bytesIn = uart.readline() 
        stringIn = str(bytesIn, "utf-8")
        return stringIn.split(',\n')
    return None       



while True:
    ''' main program loop '''
    if (last_executed + EXECUTION_INTERVAL <= running_time()):
        last_executed = running_time() 

        # retreive array of data from serial
        retrieved_data = retrieve_columns_from_uart()

        # update last seen data, if we've retrieved any.
        if retrieved_data:
            last_parsed_data = retrieved_data

        # check our sensor (it's the left button)
        button_state = button_a.is_pressed() 

        # Create comma delimited and newline (\n) terminated string to send to serial
        # In this examples we return current button state and  we echo the first 
        # element last received from serial
        data_to_send = "{},{}\n".format(button_state, last_parsed_data[0])

        uart.write(data_to_send)