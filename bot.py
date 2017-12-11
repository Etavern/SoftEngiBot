import socket
import platform
from uuid import getnode as get_mac


class Bot:

    id = 0
    ip = socket.gethostbyname(socket.gethostname())
    mac = hex(get_mac())
    os = platform.platform()

    def handleFile(self, ip):
        print("test")

    def executeCMD(self, test):
        print("test")

    def pushFile(self, test):
        print("test")

    def screenshot(self):
        print("screenshot")

    def scan(self):
        print("scan")

    def sleep(self):
        print("sleep")


bot1 = Bot()

print("IP: ", bot1.ip)
print("MAC: ", bot1.mac)
print("OS: ", bot1.os)
