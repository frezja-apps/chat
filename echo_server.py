import socketserver
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('127.0.0.1',1024)


server.bind(server_address)
#server.settimeout(25)
server.listen(5)

print ("Serv addr:", server_address)

#inputs = [server]
#outputs = []
#messege_queues = {}

connection, addr = server.accept()
print("Connection from:",addr)

while True:
    data = connection.recv(1024)
    print ("Received message:",data.decode())
    if not data:
        break
    connection.sendall(data)
connection.close()
print ("Connection ended")
