import socketserver
import socket

server_addres = ('127.0.0.1',1024)


fst_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 1024
fst_socket.bind(server_addres)
fst_socket.listen(5)

print ("serv addr:", server_addres)

while True:
    (clientsocket, addres) = fst_socket.accept()
    ct = client_thread(clientsocket)
    ct.run()
    try:
        while True:
            data = connection.recv(16)
            print ("received:", data)
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
