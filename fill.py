#!/usr/bin/python

import RPi.GPIO as io
import time

# configure GPIO
io.setmode(io.BOARD)
io.setwarnings(False)

# set up the pumps
pumps = [33, 35, 37, 36, 38, 40]
for pump in pumps:
    io.setup(pump, io.OUT)
    io.output(pump, io.LOW)

# pump the liquid until the enter button is pressed
for pump in pumps:
    io.output(pump, io.HIGH)
    input('Press <RETURN> while filled')
    io.output(pump, io.LOW)
    time.sleep(1)
