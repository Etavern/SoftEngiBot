import socket

client = socket.socket()

target_host = '0.0.0.0'
target_port = 6660

client.bind((target_host, target_port))
target_file = open('text-rec.txt', 'wb')
client.listen(5)

while True:
    c, addr = client.accept()
    print (('Got connection from', addr))
    print ("Receiving...")
    l = c.recv(1024)

    while l:
        print ("Receiving...")
        target_file.write(l)
        l = c.recv(1024)

    target_file.close()
    print ("Done Receiving")
    c.send('Thank you for connecting')
    c.close()