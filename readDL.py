from pynput import keyboard
import logging
import re

string = "" 
def readDL():

    def get_key_name(key):
        if isinstance(key, keyboard.KeyCode):
            return key.char
        else:
            return ''

    def on_press(key):
        key_name = get_key_name(key)
        global string
        string += key_name
        #print('Key {} pressed.'.format(key))

    def on_release(key):
        #print('Key {} released.'.format(key))
        if str(key) == 'Key.enter':
            global string
            print('Exiting...')
            return False

    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()
        reg = re.compile(r'(?P<ID>\d{8})=\d{4}(?P<Birth_day>\d{8})')
        
        data = reg.findall(string)[0]
        return {"ID":       data[0],
                "birthday": data[1]}
