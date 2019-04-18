#!/usr/bin/python

import requests
import json
#from PumpController import PumpController
#from MotorController import MotorController
from Controller import PumpController
from Controller import MotorController

def main():
  # first create the dictionary of the ingredients/pins
  ingredients = {
    '1': 33,
    '2': 35,
    '3': 37,
    '4': 36,
    '5': 38,
    '6': 40
  }

  # and decide which pins are used for the motor control
  tx_pin = 11
  rx_pin = 13

  # instantiate the controllers
  pump = PumpController(ingredients)
  motor = MotorController(tx_pin, rx_pin)

  # set up the connection to the web app
  URL = 'https://auto-bar.herokuapp.com/orders.json'

  while True:
    response = requests.get(url=URL)
    data = json.loads(response.content)

    # validate that the user is overage
    user = data[0]
    # TODO: validate

    # for each drink in the response
    for drink in data[1:]:
      # pump each of the liquors
      for pump_no, amount in drink.items():
        pump.pump_oz(pump_no, amount)
      
    # finally, rotate the platter
    motor.turn()

if __name__ == "__main__":
  main()