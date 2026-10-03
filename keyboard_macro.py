#! /bin/usr/python
#from pynput import keyboard
import os
import keyboard
from time import sleep

class MacroKey:
    def __init__(self,key:str):
        self.key = key

    def update_key(self,new_key:str):
        self.key = new_key

current_pressed_key = MacroKey(None)
interval = 1

def update_last_keypress(keypress:keyboard.KeyboardEvent):
    global current_pressed_key
    current_pressed_key.update_key(keypress.name)

def get_last_keypress():
    """
    Gets the last keypress not counting null values.
    returns previous keypress
    """
    global current_pressed_key
    return current_pressed_key.key

def toggle_macro():
    try:
        os.environ["CHEESE"]
    except KeyError:
        os.environ["CHEESE"] = "On"

    if os.environ.get("CHEESE") != "On":
        os.environ["CHEESE"] = "On"

    elif os.environ.get("CHEESE") == "On":
        os.environ["CHEESE"] = "Off"

    print(os.environ.get("CHEESE"))


def increase_speed():
    global interval
    if interval > 1.5:
        interval -= 0.5
    elif interval > 0.1:
        interval -= 0.1

def decrease_speed():
    global interval
    if interval < 5:
        interval += 0.5
    elif interval < 10:
        interval += 1

def main():
    # Possibly add record macro?
    global interval
    keyboard.hook(update_last_keypress)
    keyboard.add_hotkey("alt+l",toggle_macro)
    keyboard.add_hotkey("alt+=",increase_speed)
    keyboard.add_hotkey("alt+|",decrease_speed)

    while True:
        if os.environ.get("CHEESE") == "On":
            sleep(interval)
            print("Chosen Key: " + get_last_keypress())
            keyboard.send(get_last_keypress())


if __name__ == "__main__":
    main()

