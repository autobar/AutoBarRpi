# AutoBarRpi
An automated cocktail-making machine controlled through the web.

## Summary
There are only 3 files that you need to know about in this repository: `Controllers.py`, 
`main.py`, and `off.py`.

### Controllers
The file `Controllers.py` contains the code that abstracts away the inner mechanism of the 
system. The goal of this is to make it so that the main logic programmer does not need to
deal with setting pins high and low and handling timing and signal debouncing. Here is how:

#### PumpController
The PumpController has only 1 static data member and 2 real functions: the constructor and 
the `pump_oz` method.
* The static data member `SECS_PER_OZ` is a constant that is determined experimentally. It
  represents the number of seconds that it takes for the pump to pump 1 ounce of water. We
  calculated this value to be around 3 and a half seconds, but you might need something
  different. This value is hard-coded and cannot be changed through the interface.
* The constructor takes in a dictionary of the pump numbers as strings and the pins to that
  correspond to the pump as integers. The constructor may through exceptions if the provided
  dictionary is empty or there was no constructor parameter specified.
* The `pump_oz` function takes 2 parameters: `pump_name` and `amount_of_liquid`. The first 
  parameter is expected to be a `string` such as '3' and the second is a `float` representing
  the number of ounces to be pumped.

#### MotorController
The MotorController has only 3 functions: the constructor, the `turn` method, and the `stop`
method.
* The constructor takes in the two pins that are used for communication with the PiC32 board.
  These two pins are the transmitter pin (`tx_pin`) and the receiver pin (`rx_pin`). As 
  expected, the transmitter pin sends data to the PiC32 and the receiver pin receives data 
  from the PiC32.
* The `turn` method sends a signal to the PiC32 to turn the motor one space, in the direction
  determined by the PiC32 and not the Raspberry Pi. To do this, it sets the transmitter pin
  to HIGH for half a second and then sets the pin back to low. The Raspberry Pi will not 
  return from this method until the PiC32 indicates that it has completed the action, indicated
  by the receiver pin going HIGH for half a second. This is to prevent the main Raspberry Pi 
  logic from pumping liquid while the platter is spinning, which would result in liquid being
  spilled everywhere. This method takes no parameters.
* The `stop` method is mainly for debugging and will likely not be used in an actual system. 
  This method simply sets the transmitter pin to LOW in order to stop sending the turn signal 
  to the PiC32. This should not be necessary unless the Raspberry Pi somehow is interrupted 
  before it is able to complete a call to the `turn` method.
