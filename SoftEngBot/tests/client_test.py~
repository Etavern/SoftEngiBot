import socket


# This code snippet sends TCP to an open listener

send_host = "127.0.0.1"
send_port = 9990

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((send_host, send_port))

# send some data
client.send('file')

# receive some data
response = client.recv(4096)
print (response)
