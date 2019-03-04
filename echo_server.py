import socketserver
import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_addres = ('127.0.0.1',1024)


server.bind(server_addres)
#server.settimeout(25)
server.listen(5)

print ("Serv addr:", server_addres)

#inputs = [server]
#outputs = []
#messege_queues = {}

connection, addr = server.accept()

while True:
    data = connection.recv(1024)
    print (data.decode())
    if not data:
        break
    connection.sendall(data)
connection.close()
print ("Connection ended")
