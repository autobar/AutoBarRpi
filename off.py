#!/usr/bin/python

import RPi.GPIO as io

io.setmode(io.BOARD)
io.setwarnings(False)

for i in [33,35,37,36,38,40]:
    io.setup(i, io.OUT)
    io.output(i, io.LOW)

io.setup(13, io.OUT)
io.output(13, io.HIGH)