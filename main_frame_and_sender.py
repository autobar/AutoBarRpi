# importing the requests library 
import requests 
import PumpController
  
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
URL = "i.am.a.AWS.server.for.auto.bar"

# defining a params dict for the parameters to be sent to the API 
PARAMS = "/"
# assume request all
  
# sending get request and saving the response as response object 
# then extracting data in json format 

PC = PumpController()
PC.pin_list["vodka"] = vodka_pin
PC.pin_list["jack daniels"] = jack_daniels_pin
PC.pin_list["rum"] = rum_pin
PC.pin_list["gin"] = gin_pin

PumpController vodka
PumpController jack_daniels
PumpController rum
PumpController gin

PumpController sprite
PumpController lime_juice
PumpController tonic_water
PumpController ginger_beer
PumpController orange_juice

while true:
	r = requests.get(url = URL, params = PARAMS) 
	data = r.json() 
