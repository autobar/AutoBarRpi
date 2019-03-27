# importing the requests library 
import requests
from PumpController import PumpController 
ingredients = {
    'vodka'  :  3,
    "jack daniels": 5,
    'rum'    :  7,
    'ginger beer'  : 11,
    'orange juice'  : 13,
    'sprite'  : 15
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

#r = requests.get(url = URL) 
#data = r.json()
data =  {
            "name": "Screwdriver",
            "liquors": {
                "vodka": 2
            },
            "mixers": {
                "orange juice": 5
            }
        }

print("PC instance")
PC = PumpController(ingredients)
print("liquors:");
for key, value in data["liquors"].items():
    PC.pump_oz(key,value)
print("mixers:");
for key, value in data["mixers"].items():
    PC.pump_oz(key,value)
'''
while true:
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    #using a call back function here in the future to speed up the process
    for key, value in data["ingredients"].items():
        PC.pump_mL(key,value)
'''