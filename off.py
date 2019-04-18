#!/usr/bin/python

import RPi.GPIO as io

io.setmode(io.BOARD)
io.setwarnings(False)

for i in [11,33,35,37,36,38,40]:
    io.setup(i, io.OUT)
    io.output(i, io.LOW)
