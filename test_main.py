from PumpController import PumpController

def main():
  # first create the dictionary of the ingredients/pins
  ingredients = {
    'vodka'  :  3,
    'rum'    :  5,
    'tequila':  7,
    'water'  : 11,
    'juice'  : 13,
    'other'  : 15
  }

  # instantiate the PumpController
  pump = PumpController(ingredients)

  # try pumping 20 mL worth of vodka
  pump.pump_mL('vodka', 20)
  print 'pumping complete'



if __name__ == "__main__":
  main()