import RPi.GPIO as io
import time

class PumpController:

    ''' Constants: '''
    SECS_PER_OZ = 10 # this needs to be calculated experimentally

    '''
    Attributes:
        pin_map: the list of the pin numbers that send the signals
                 to each of the relays controlling the pumps
    '''

    def __init__(self, pin_list={}):
        if not pin_list:
            raise Exception('pin_list cannot be an empty list')
        self.pin_map = pin_list

    def pump_mL(self, pump_no, amount_of_liquid):
        # make sure that parameters are actually integers
        pump_no = int(pump_no)
        amount_of_liquid = int(amount_of_liquid)

        # make sure that the pump_no is actually in the range of valid 
        # pump numbers
        if pump_no >= pin_map.size:
            raise Exception('invalid pump number accessed')

        io.output(pin_map[pump_no], io.HIGH)
        time.sleep(amount_of_liquid * SECS_PER_OZ)
        io.output(pin_map[pump_no], io.LOW)

