import socketserver
import socket
import threading
import _thread

server_addres = ('127.0.0.1',1024)

thr_lock = threading.Lock()

def threads(co):
    while True:
        data = connection.recv(1024)
        print ("Message:",data.decode())
        if not data:
            thr_lock.release()
            break

        connection.sendall(data)
    connection.close()
    print ("Connection close")


print ("Serv addr:", server_addres)

#inputs = [server]
#outputs = []
#messege_queues = {}

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(server_addres)
server.listen(5)

while True:
    connection, addr = server.accept()
    thr_lock.acquire()
    print("Connected to:",addr)
    start_new_thread(threads,(co,))
    #while True:
    #    data = connection.recv(1024)
    #    print ("Message:",data.decode())
    #    if not data:
    #        thr_lock.release()
    #        break
    #    connection.sendall(data)
connection.close()
print ("Connection close")
