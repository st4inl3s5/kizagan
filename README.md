# KIZAGAN

KIZAGAN is a remote access trojan built with python.It can take victim's camera snapshots, microphone sounds, screenshots... Also it has keylogger inside and it is undetectable.

Antivirus scan result : (btw, scan it on non-distrubuted online antivirus scanners please.)

![scan-result](https://user-images.githubusercontent.com/68844502/232308126-a7756b05-6d6f-4a4f-abac-10a87d0514f1.PNG)

## EDUCATIONAL PURPOSES ONLY.

##### I am not responsible in bad uses of kizagan.


# SETUP

1. In linux (Your server that listening connections from clients.)

+ python setupLinux.py

2. In windows (Theese libraries are needed when converting python file to exe file.)

+ python setupWindows.py

# USAGE

1. Open the kizaganEN.py with a text editor and change the ip and port according to yourself. (You can set for port forward services ngrok etc.)

![a1](https://user-images.githubusercontent.com/68844502/232308824-5bacce15-50b6-44b4-9df2-eb343b345b6b.PNG)

2. Get an icon file and a merge file from the internet etc.

![a3](https://user-images.githubusercontent.com/68844502/232310059-bbc0475a-1f8e-41f5-9b2e-bd98b97d245f.jpg)

2. Change the value of Open_Added_File function then save it.

![a4](https://user-images.githubusercontent.com/68844502/232310658-07c4b9c0-68e9-40e4-9852-a5f9d3217d64.PNG)

3. Use the pyinstaller to convert this python file to exe file.(Make it on windows.)
+ pyinstaller --onefile --noconsole --icon <your icon file with .ico extension> --add-data "<example.pdf>;." -w kizaganEN.py

![a5](https://user-images.githubusercontent.com/68844502/232311188-9ad74a61-307e-4741-ae10-48491904d701.PNG)

4. When the execute is finished,our trojan file with .exe extension found in dist file.

![a5](https://user-images.githubusercontent.com/68844502/232312235-7b3a0501-bdb1-4719-9f14-d293949e1b64.PNG)

![a6](https://user-images.githubusercontent.com/68844502/232312242-81ca1282-b956-4f4e-bd0b-9d9c83664392.PNG)

5. Now, we are ready.Send this .exe file to a victim and wait for the executing the trojan.

6. When the trojan executes, the trojan will send a connection to you in every 5 seconds.

7. Let's say, the victim executed the trojan.We can get this connection by following command in linux :

+ python kizagan_listener.py -ip ip -p port

![a8](https://user-images.githubusercontent.com/68844502/232312631-5850918b-f8b3-4a4d-b66e-9f2e0a809dc4.PNG)

8. When the trojan executed our merge file will opened and a connection will come to us.

![a9](https://user-images.githubusercontent.com/68844502/232312825-7f919b2d-1689-4a6f-a0cb-d772308bd9c3.PNG)

![a10](https://user-images.githubusercontent.com/68844502/232312831-307e8bd1-049a-4a75-a815-c4b7191756e7.PNG)

9. If you want to record microphone of victim, say 'Y' for it.

![a10](https://user-images.githubusercontent.com/68844502/232313290-a627eea5-84cd-4a5d-873c-6488996e2dc4.PNG)

10. You can set default by saying 'N' for it.Or you can change the chat port.

![a11](https://user-images.githubusercontent.com/68844502/232313292-cec56a06-42a3-4176-941c-afeaa03d944d.PNG)

11. And we are rocking now! You can view the commands by using 'help' command.

![a15](https://user-images.githubusercontent.com/68844502/232313369-a0d41ad8-2b03-4490-a7da-37c850b8e4d6.PNG)

![a16](https://user-images.githubusercontent.com/68844502/232313370-011f79e1-b650-4b54-8425-ff498603cc05.PNG)

![a12](https://user-images.githubusercontent.com/68844502/232313371-bf3ba723-d6d7-40e3-9723-82cd14dd9390.PNG)

![a13](https://user-images.githubusercontent.com/68844502/232313373-2d75ce01-9b89-4b21-82cc-7686b2b4961b.PNG)

![a14](https://user-images.githubusercontent.com/68844502/232313374-64955604-ed82-4382-acb8-687742936928.PNG)

12. Getting microphone sounds, camera snapshots, screenshots etc.

![a17](https://user-images.githubusercontent.com/68844502/232313411-cf03dc49-6a6f-4915-b788-d53bc7d135e5.PNG)

![a18](https://user-images.githubusercontent.com/68844502/232313414-692772de-9983-480e-bc3a-eeb6041e9907.PNG)


### You can contact me here or in instagram : 

+ https://www.instagram.com/arduinocum.py/
