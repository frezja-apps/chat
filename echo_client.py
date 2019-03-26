import socket
import configparser


parser = configparser.ConfigParser()
parser.read('conf.ini')



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (parser.get('config', 'address'), int(parser.get('config', 'port')))
#print (sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
print("Connected to:", server_address)



#data = sock.recv(1024)
#print ("Received message: {}".format(data.decode()))


while True:
    msg = input("Input message or type /quit to disconnect: ")
    if msg != "/quit":
        sock.send(msg.encode())
        data = sock.recv(1024)
        print("Received message: {}".format(data.decode()))
    else:
        print("Quitting...")
        break

sock.close()
print("Connection closed")
