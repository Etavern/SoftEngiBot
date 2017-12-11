import socket
import platform
from uuid import getnode as get_mac

class Bot:

    id = 0
    ip = socket.gethostbyname(socket.gethostname())
    mac = hex(get_mac())
    os = platform.platform()
    
    
    def handleFile(test):
        print("test")

    def executeCMD(test):
        print("test")

    def pushFile(test):
        print("test")

    def screenshot():
        print("screenshot")

    def scan():
        print("scan")

    def sleep():
        print("sleep")
        
bot1 = Bot()

print("IP: ", bot1.ip)
print("MAC: ", bot1.mac)
print("OS: ", bot1.os)
