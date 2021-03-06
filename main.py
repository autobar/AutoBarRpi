#!/usr/bin/python

import requests
import json
import re
from dateutil.relativedelta import relativedelta
import datetime
from Controllers import PumpController
from Controllers import MotorController

# returns a Boolean of whether the user is over 21 or not
def is_overage(dob):
  # calculate the minimum DOB that a user must have to work
  min_date = datetime.datetime.now() - relativedelta(years=21)
  return dob < min_date

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
      # try up to 6 times to reach the web app
      # if it is unreachable after that, then just terminate
      tries = 0
      try:
        response = requests.get(url=URL)
        tries += 1
      except:
        print('Unable to connect to the web app, check internet connection')
        print('Trying again in 3 seconds...')
        time.sleep(3)
      while response.content is '':
        #if tries > 5:
        #  print('No internet connection: terminating program')
        #  return 0
        try:
          response = requests.get(url=URL)
          tries += 1
        except:
          print('Unable to connect to the web app, check internet connection')
          print('Trying again in 3 seconds...')
          time.sleep(3)
      data = json.loads(response.content)

      # used in loop to find correct drivers license
      user = data[0]
      regex = re.compile(r'(?P<ID>\d{8})=\d{4}(?P<Birth_day>\d{8})')

      # use a flag
      # => 0 means incorrect license number
      # => 1 means success
      # => 2 means underage user
      flag = 0
      while flag is 0:
        # wait for the user to slide their drivers license
        user_input = str(raw_input('Enter DL: '))
        
        # the below throws exceptions a lot, so be careful
        # this is only needed because the card reader is not always reliable
        try:
          user_id, user_dob = regex.findall(user_input)[0]
        except:
          print('Invalid read of DL, try again')
          continue
        
        # extract the user's date of birth
        user_dob = datetime.datetime.strptime(user_dob, '%Y%m%d')

        # validate that the user is overage
        if not is_overage(user_dob):
          print('Drink order canceled: underage user')
          flag = 2
          break
        # validate that the user has the correct drivers license
        elif user_id != user['drivers_license']:
          print('Incorrect DL: this drivers license was not used to order this drink')
        else:
          flag = 1
        
      # if underage user, do not fill the order and move on to the next one
      if flag is 2:
        continue

      # for each drink in the response
      print('Correct DL: making ' + str(len(data[1:])) + ' drinks!')
      for drink in data[1:]:
        # pump each of the liquids
        for pump_no, amount in drink.items():
          pump.pump_oz(pump_no, amount)
        
        # finally, rotate the platter
        motor.turn()

      # reset the platter position
      for _ in range(5 - len(data[1:])):
        motor.turn()

if __name__ == "__main__":
  main()