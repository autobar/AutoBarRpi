# importing the requests library 
import requests
#import PumpController
  
'''

define all pin map here

in formate of 
vodka_pin
rum_pin
etc.

or not

this is a set version(assuming each pump will only be using to pump single drink)

future adaption will add more functionality to the GET json
which allow replace pump's corresponding drink

'''

# api-endpoint 
URL = "https://auto-bar.herokuapp.com/orders.json"
# defining a params dict for the parameters to be sent to the API

# assume request all
  
# sending get request and saving the response as response object 
# then extracting data in json format 

r = requests.get(url = URL) 
data = r.json()
print(data)

'''
PC = PumpController()
PC.pin_map ["vodka"] = vodka_pin
PC.pin_map ["jack daniels"] = jack_daniels_pin
PC.pin_map ["rum"] = rum_pin
PC.pin_map ["gin"] = gin_pin

PC.pin_map ["sprite"] = sprite_pin
PC.pin_map ["lime_juice"] = lime_juice_pin
PC.pin_map ["tonic_water"] = tonic_water_pin
PC.pin_map ["ginger_beer"] = ginger_beer_pin
PC.pin_map ["orange_juice"] = orange_juice_pin


while true:
	r = requests.get(url = URL, params = PARAMS) 
	data = r.json()
	#using a call back function here in the future to speed up the process
	for key, value in data["ingredients"].items():
		PC.pump_mL(key,value)
'''