# importing the requests library 
import requests
from PumpController import PumpController 
from readDL import readDL
ingredients = {
    'vodka'  :  7,
    "jack daniels": 11,
    'rum'    :  13,
    'tequila':  15,
    "gin"    :  19,
    'water'  : 21,
    'lime_juice'  : 23,
    'tonic_water'  : 29,
    'ginger_beer'  : 31,
    'orange_juice'  : 33,
    'sprite'  : 35
  }
'''
this is a set version(assuming each pump will only be using to pump single drink)

future adaption will add more functionality to the GET json
which allow replace pump's corresponding drink

'''
def handler(signum, frame):
     raise Exception("TIMEOUT")
signal.signal(signal.SIGALRM, handler)

# api-endpoint 
URL = "https://auto-bar.herokuapp.com/orders.json"
# defining a params dict for the parameters to be sent to the API

# assume request all
  
# sending get request and saving the response as response object 
# then extracting data in json format 
PC = PumpController(ingredients)
signal.signal(signal.SIGALRM, handler)
while true:
    r = requests.get(url = URL) 
    datas = r.json()
    signal.alarm(10)
    try:
        while true:
            a = readDL()
            if a["ID"] == r[0]["drivers_license"]
                if a["BirthDay"] >= 19980417
                    break
    except Exception, exc:
        continue
    for data in datas[1:]
        for key, value in data["liquors"].items():
            PC.pump_oz(key,value)    
        for key, value in data["mixers"].items():
            PC.pump_oz(key,value)
    
