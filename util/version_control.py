import json
from urllib.request import urlopen
import os

version_link = "https://raw.githubusercontent.com/st4inl3s5/kizagan/main/util/version.json"

def Get_Latest_Info():
    url = urlopen(version_link)
    latest_info = json.loads(url.read().decode())
    return latest_info

def Get_Current_Info():
    try:
        with open("version.json","r") as file:
            current_info = json.loads(file.read())
        return current_info
    except FileNotFoundError:
        return {"version" : ""}

def Is_Update_Avaliable():
    return Get_Current_Info()["version"] == Get_Latest_Info()["version"]

def Update():
    os.system("git clone https://github.com/st4inl3s5/kizagan")
    os.rename("kizagan","updated_kizagan")
