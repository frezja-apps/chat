import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_addres = ('127.0.0.1', 1024)

print (sys.stderr, 'connecting to %s port %s' % server_addres)
sock.connect(server_addres)
print("Connected to:", server_addres)

while True:
    msg = input("Input message or type /quit to disconnect: ")
    if msg != "/quit":
        sock.send(msg.encode())
        data = sock.recv(1024)
        print ("Received message: {}".format(data.decode()))
    else:
        print ("Quitting...")
        break

sock.close()
print ("Connection closed")
