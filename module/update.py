import json
from urllib.request import urlopen
import os
from shutil import move, rmtree
from colorama import init, Fore

version_link = "https://raw.githubusercontent.com/st4inl3s5/kizagan/main/json/version.json"

def get_latest_ver():
    url = urlopen(version_link)
    latest_ver = json.loads(url.read().decode())
    latest_ver = latest_ver["version"]
    return float(latest_ver)

def get_current_ver():
    try:
        if os.name == "nt":
            ver_file = open("json\\version.json", "r")
        else:
            ver_file = open("json/version.json", "r")
        current_ver = json.loads(ver_file.read())
        current_ver = current_ver["version"]
        ver_file.close()
        return float(current_ver)
    except FileNotFoundError:
        return -1
    
def check_version():
    global latest_ver, current_ver
    latest_ver = get_latest_ver()
    current_ver = get_current_ver()
    return latest_ver != current_ver #True = update, False = no update.

def make_update():
    if os.name == "nt":
        print(f"{Fore.RED}[-]Use it on unix systems or download manually from https://github.com/st4inl3s5/kizagan.")
        return 0
    update_available = check_version()
    if update_available:
        print(f"{Fore.LIGHTBLUE_EX}[!]v{latest_ver} is available.Update starting...")
        os.system("git clone https://github.com/st4inl3s5/kizagan")
        curr_path = os.getcwd()
        downloaded_path = curr_path+"/kizagan"
        to_be_moved_path = curr_path+"/../updated_kizagan"
        move(downloaded_path, to_be_moved_path)
        os.chdir("../updated_kizagan")
        rmtree(curr_path+"/../kizagan")
        os.rename("../updated_kizagan", "../kizagan")
        print(f"{Fore.LIGHTGREEN_EX}[+]Update completed.")
        os.system("python3 kizagan.py -h")
    else:
        print(f"{Fore.LIGHTGREEN_EX}[+]Your version up to date.")