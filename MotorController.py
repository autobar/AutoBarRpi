'''
NOTE: THIS CLASS ASSUMES THAT YOU HAVE ALREADY IMPORTED THE RPi.GPIO
      LIBRARY AS io AND THE time LIBRARY
NOTE: THIS CLASS ASSUMES THAT THE PINMODE OF THE RPi. GPIO LIBRARY
      HAS ALREADY BEEN SET TO BOARD
NOTE: THIS CLASS DOES NOT CHECK THAT THE SPECIFIED PINS HAVE NOT BEEN
      USED FOR ANY OTHER FUNCTION
'''
class MotorController(object):
    global io
    global time

    '''
    Attributes:
        tx_pin: the pin number for the line on which the Pi
                sends the signal to the PiC (transmitter)
        tx_pin: the pin number for the line on which the Pi
                receives the signal from the PiC (receiver)
    '''

    # constructor
    def __init__(self, _tx_pin, _rx_pin):
        self.tx_pin = int(_tx_pin)
        self.rx_pin = int(_rx_pin)

        if self.tx_pin < 0 or self.tx_pin > 40:
            raise Exception('Invalid TX pin supplied')
        if self.rx_pin < 0 or self.rx_pin > 40:
            raise Exception('Invalid RX pin supplied')
        if self.tx_pin == self.rx_pin:
            raise Exception('TX and RX pins cannot be the same')

        # set up the pins
        io.setup(self.tx_pin, io.OUT)
        io.setup(self.rx_pin, io.IN)

        # initialize the pins
        io.output(self.tx_pin, io.LOW)

    # sends a signal to the PiC to let it know that it needs
    # to turn the rotating platter. then it waits until it
    # gets the all clear signal
    def turn(self):
        if self.tx_pin is None or self.rx_pin is None:
            raise Exception("No valid TX or RX pin has been set")
        
        # send the PiC the signal to turn the platter
        io.output(self.tx_pin, io.HIGH)
        time.sleep(0.5)
        io.output(self.tx_pin, io.LOW)

        # do not return until the PiC says we can
        while (io.input(self.rx_pin) == io.LOW):
            pass
        return True
