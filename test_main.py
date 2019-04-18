#!/usr/bin/python

import requests
import json
from readDL import readDL
from Controllers import PumpController
from Controllers import MotorController

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
  tx_pin = 29
  rx_pin = 13

  test_order = {'1': 1,
                '2': 1,
                '3': 1}
  test = False

  # instantiate the controllers
  pump = PumpController(ingredients)
  motor = MotorController(tx_pin, rx_pin)

  # define the connection to the web app
  URL = 'https://auto-bar.herokuapp.com/orders.json'

  while True:
    if test:
      # make the same drink 3 times
      for _ in range(3):
        for pump_no, amount in test_order.items():
          pump.pump_oz(pump_no, amount)
        motor.turn()
      break
    else:
      # get the drink orders from the web app
      response = requests.get(url=URL)
      while response.content is '':
        response = requests.get(url=URL)
      data = json.loads(response.content)

      # validate that the user is overage
      user = data[0]
      keylogger = readDL()
      if keylogger["ID"] == user["drivers_license"]:
        # NOTE: this currently uses a hard-coded date for today
        if not keylogger["BirthDay"] >= 19980418:
          print('Underaged user: drink order canceled')
          continue

      # for each drink in the response
      for drink in data[1:]:
        # pump each of the liquids
        for pump_no, amount in drink.items():
          pump.pump_oz(pump_no, amount)
        
        # finally, rotate the platter
        motor.turn()

if __name__ == "__main__":
  main()