import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_addres = ('127.0.0.1', 1024)

print (sys.stderr, 'connecting to %s port %s' % server_addres)
sock.connect(server_addres)
print("Connected to:", server_addres)



#data = sock.recv(1024)
#print ("Received message: {}".format(data.decode()))

while True:
    msg = (input("Input message: ")).encode()
    sock.send(msg)
    data = sock.recv(1024)
    print ("Received message: {}".format(data.decode()))
    if not msg:
        break
        sock.close()
print ("Connection closed")
