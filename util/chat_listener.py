import socket
import threading
import tkinter
import argparse
import colorama

colorama.init(autoreset=True)

ap = argparse.ArgumentParser()
ap.add_argument("-ip", "--ip_address", required=True,help="Set the ip address to listen chat./Chat'i dinlemek icin ip adresi giriniz.")
ap.add_argument("-p", "--port", required=True,help="Set the port to listen chat./Chat'i dinlemek icin port numarasi giriniz.")
args = vars(ap.parse_args())



class Chat():
    def __init__(self,ip,port):
        self.chat_listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.chat_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.chat_listener.bind((ip,port))
        self.chat_listener.listen(0)
        print(colorama.Fore.GREEN+"Chat initializing...")
        (self.connection,address) = self.chat_listener.accept()
        print(colorama.Fore.RED+"Chat connection came.Opening the GUI...")
        self.chat_gui = tkinter.Tk()
        self.chat_gui.resizable(False, False)
        self.chat_gui.config(bg="#D9D8D7")
        self.chat_gui.geometry("750x400")
        self.chat_gui.title("You are chatting with victim.")
        self.messages = tkinter.Text(self.chat_gui, width=75, height=10, fg="#0E6B0E", bg="#000000")
        self.messages.place(x=0, y=0)
        self.messages.insert("1.0","For send to message to victim,write the message 'your message' part and click the button.If you want to exit,print 'exit' or 'cikis' and send message.")
        self.your_message_label = tkinter.Label(self.chat_gui, width=20, text="Your Message :", fg="#0D1C6E")
        self.your_message_label.place(x=-40, y=250)
        self.message_input = tkinter.Entry(self.chat_gui, width=50)
        self.message_input.place(x=100, y=250)
        self.Send_Button = tkinter.Button(self.chat_gui, width=20, text="Send Message", command=self.Send_Messages, bg="#000000",fg="#0E6B0E")
        self.Send_Button.place(x=560, y=245)
        get_messages_thread = threading.Thread(target=self.Get_Messages)
        get_messages_thread.daemon = True
        get_messages_thread.start()
        self.chat_gui.mainloop()

    def Send_Messages(self):
        message = self.message_input.get()
        self.messages.insert(tkinter.END, "\n" + "You:" + message)
        self.connection.send(message.encode())
        if message == "exit" or message=="cikis":
            exit()
        self.messages.see("end")

    def Get_Messages(self):
        while True:
            message = self.connection.recv(1024).decode()
            self.messages.insert(tkinter.END, "\n" + "Victim:" + message)
            self.messages.see("end")


Chat(args["ip_address"],int(args["port"]))
