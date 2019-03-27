# importing the requests library 
import requests
from PumpController import PumpController 
ingredients = {
    'vodka'  :  7,
    "jack daniels": 11,
    'rum'    :  13,
    'tequila':  15,
    "gin"    :  17,
    'water'  : 19,
    'lime_juice'  : 21,
    'tonic_water'  : 23,
    'ginger_beer'  : 27,
    'orange_juice'  : 29,
    'sprite'  : 31
  }
'''
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
PC = PumpController(ingredients)

while true:
    r = requests.get(url = URL) 
    data = r.json()
    #using a call back function here in the future to speed up the process
    for key, value in data["liquors"].items():
        PC.pump_oz(key,value)    
    for key, value in data["mixers"].items():
        PC.pump_oz(key,value)
    
