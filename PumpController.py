import RPi.GPIO as io
import time

class PumpController(object):

    ''' Constants: '''
    SECS_PER_OZ = 10 # this needs to be calculated experimentally

    '''
    Attributes:
        pin_map: the list of the pin numbers that send the signals
                 to each of the relays controlling the pumps.
                 This data structure is simply a hash that will be
                 used to get the pin number based on the name of 
                 the ingedient. For example pin_map['vodka'], etc.,
                 will return the pin number for the vodka pump.
    '''

    def __init__(self, pin_dict={}):
        if not pin_dict:
            raise Exception('pin_dict cannot be an empty dict')
        self.pin_map = pin_dict

        # set up the RPi.GPIO stuff
        io.setmode(io.BOARD)
        io.setwarnings(False)

        # initialize GPIO pins
        for name, pin in pin_map.iteritems():
            io.setup(pin, io.OUT)
            io.output(pin, io.LOW)

    def pump_mL(self, pump_name, amount_of_liquid):
        # make sure that parameters are correct types
        pump_name = str(pump_name)
        amount_of_liquid = int(amount_of_liquid)

        # make sure that the pump_name is actually in the range of valid 
        # pump numbers
        if pin_map.get(pump_name) == None:
            raise Exception('invalid pump name accessed')

        io.output(pin_map[pump_name], io.HIGH)
        time.sleep(amount_of_liquid * SECS_PER_OZ)
        io.output(pin_map[pump_name], io.LOW)

