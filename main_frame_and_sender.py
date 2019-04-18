#!/usr/bin/python
#from readDL import readDL
import requests
import json
from PumpController import PumpController 
ingredients = {
    'vodka'  :  33,
    "jack daniels": 35,
    'rum'    :  37,
    'lime_juice'  : 36,
    'tonic_water'  : 38,
    'ginger_beer'  : 40,
  }
URL = "https://auto-bar.herokuapp.com/orders.json"
PC = PumpController(ingredients)
#signal.signal(signal.SIGALRM, handler)

while True:
    r = requests.get(url = URL)
    print(r.content)
    datas = json.loads(r.content)
    #while true:
        #a = readDL()
        #if a["ID"] == r[0]["drivers_license"]:
            #if a["BirthDay"] >= 19980417:
                #break
        #continue
    for data in datas[1:]:
        for key, value in data["liquors"].items():
            PC.pump_oz(key,value)    
        for key, value in data["mixers"].items():
            PC.pump_oz(key,value)

'''
datas = [{'mixers': {'tonic_water': 1},
          'liquors': {'vodka': 2,
                      'rum': 2}}]

for data in datas:
        for key, value in data["liquors"].items():
            PC.pump_oz(key,value)    
        for key, value in data["mixers"].items():
            PC.pump_oz(key,value)
            
'''