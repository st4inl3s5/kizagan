import pyaudio
import wave
import threading
import os

ses_dosya = os.environ["appdata"]+"\\windowssounds.wav"

class Kayit():
    def __init__(self, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100, py=pyaudio.PyAudio()):
        self.CHUNK = chunk
        self.FORMAT = frmat
        self.CHANNELS = channels
        self.RATE = rate
        self.p = py
        self.frames = []
        self.st = 1
        self.stream = self.p.open(format=self.FORMAT, channels=self.CHANNELS, rate=self.RATE, input=True,frames_per_buffer=self.CHUNK)
    def startRecord(self):
        self.st = 1
        self.frames = []
        self.streaming = self.p.open(format=self.FORMAT,channels=self.CHANNELS,rate=self.RATE,input=True,frames_per_buffer=self.CHUNK)
        #print("Recording...")
        while self.st == 1:
            data = self.streaming.read(self.CHUNK)
            self.frames.append(data)

        self.streaming.close()

    def stopRecord(self):
        self.st = 0
        wf = wave.open(ses_dosya, "wb")
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        #print("Kaydedildi.")
        mythread3 = threading.Thread(target=self.startRecord)
        mythread3.start()

"""
    def kayitBasla(self):
        while True:
            a = int(input("Secim"))
            try:
                if a == 1:
                    mythread = threading.Thread(target=self.startRecord)
                    mythread.start()
                else:
                    self.stopRecord()
            except Exception:
                print("Bilinmeyen bir hata.")

"""


