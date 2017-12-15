import socket

server = socket.socket()

target_host = '0.0.0.0'
target_port = 9990

server.bind((target_host, target_port))
target_file = open('text-rec2.txt', 'wb')
server.listen(5)

while True:
    client, addr = server.accept()
    print ('Got connection from', addr)
    print ("Receiving...")
    l = client.recv(1024)

    while l:
        print ("Receiving...")
        target_file.write(l)
        l = c.recv(1024)

    target_file.close()
    print ("Done Receiving")
    client.send('Thank you for connecting')
    client.close()
