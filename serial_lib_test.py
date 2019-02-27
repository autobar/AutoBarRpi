#by running ls /dev/tty* after connection
#arduino with the ras pi, we will be able
#to see something alone the line of 
#/dev/ttyACM0. This is the port that we 
#will be use for connect to the arduino

import serial
#python -m pip install pyserial
#will need to be run first

port = "dev/ttyACM0"
#this is depend on the port we found

rate = 9600

s_arduino = serial.Serial(port,rate)

//handle user input...

s_arduino.write(userinput)
