from flask import Flask
from flask_ask import Ask, statement
 
app = Flask(__name__)
ask = Ask(app, '/')
 
@ask.intent('LedIntent')
def led(color, status):
  if color.lower() not in pins.keys():
    print("I don't have {} light".format(color))
    return statement("I don't have {} light".format(color)) 
  print('Turning the {} light {}'.format(color, status))
  return statement('Turning the {} light {}'.format(color, status))
 
if __name__ == '__main__':
  try:
    pins = {'red':9, 'yellow':10, 'green':11}
    app.run(debug=True)
  finally:
    print("done.")