import RPi.GPIO as io
import time

class PumpController(object):

    ''' Constants: '''
    SECS_PER_OZ = 2 # this needs to be calculated experimentally
    # TODO: fix ^

    '''
    Attributes:
        pin_map: the list of the pin numbers that send the signals
                 to each of the relays controlling the pumps.
                 This data structure is simply a hash that will be
                 used to get the pin number based pump number as a
                 string. For example pin_map['2'], etc.,
                 will return the pin number for pump #2.
    '''

    def __init__(self, pin_dict={}):
        if not pin_dict:
            raise Exception('pin_dict cannot be an empty dict')
        self.pin_map = pin_dict

        # set up the RPi.GPIO stuff
        io.setmode(io.BOARD)
        io.setwarnings(False)

        # initialize GPIO pins
        for name, pin in self.pin_map.iteritems():
            io.setup(pin, io.OUT, io.PUD_DOWN, io.LOW)

    def pump_oz(self, pump_name, amount_of_liquid):
        # make sure that parameters are correct types
        pump_name = str(pump_name)
        amount_of_liquid = int(amount_of_liquid)

        # make sure that the pump_name is actually in the range of valid 
        # pump numbers
        if self.pin_map.get(pump_name) == None:
            raise Exception('invalid pump name accessed: ' + str(pump_name))

        io.output(self.pin_map[pump_name], io.HIGH)
        time.sleep(amount_of_liquid * self.SECS_PER_OZ)
        io.output(self.pin_map[pump_name], io.LOW)


'''
NOTE: THIS CLASS ASSUMES THAT YOU HAVE ALREADY IMPORTED THE RPi.GPIO
      LIBRARY AS io AND THE time LIBRARY
NOTE: THIS CLASS ASSUMES THAT THE PINMODE OF THE RPi. GPIO LIBRARY
      HAS ALREADY BEEN SET TO BOARD
NOTE: THIS CLASS DOES NOT CHECK THAT THE SPECIFIED PINS HAVE NOT BEEN
      USED FOR ANY OTHER FUNCTION
'''
class MotorController(object):
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
        io.setup(self.tx_pin, io.OUT, io.PUD_DOWN, io.LOW)
        io.setup(self.rx_pin, io.IN)

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

    # tell the motor to stop turning
    def stop(self):
        if self.tx_pin is None:
            raise Exception("No valid TX pin has been set")
        
        io.output(self.tx_pin, io.LOW)
        return True
