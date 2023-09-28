import json
from urllib.request import urlopen
import os

version_link = "https://raw.githubusercontent.com/st4inl3s5/kizagan/main/modules/version.json"


def get_latest_info():
    url = urlopen(version_link)
    latest_info = json.loads(url.read().decode())
    return latest_info


def get_current_info():
    try:
        with open("modules/version.json", "r") as file:
            current_info = json.loads(file.read())
        return current_info
    except FileNotFoundError:
        return {"version": ""}


def is_update_avaliable():
    return get_current_info()["version"] == get_latest_info()["version"]


def update():
    os.system("git clone https://github.com/st4inl3s5/kizagan")
    os.rename("kizagan", "updated_kizagan")
