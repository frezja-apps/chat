import socketserver
import socket, select, queue

server_addres = ('127.0.0.1',1024)
print ("Serv addr:", server_addres)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(server_addres)
server.listen(5)
server.setblocking(0)

inputs = [server]
outputs = []
message_queues = {}

while inputs:
    rlist, wlist, elist = select.select(inputs, outputs, inputs)
    for c in rlist:
        if c is server:
            connection, addr = c.accept()
            print ("Connected to", addr)
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = queue.Queue()
            #print ("Inp:", inputs)
        else:
            data = c.recv(1024)
            print ("Message: ", data.decode())
            #c.send(data)
            if data:
                message_queues[c].put(data)
                if c not in outputs:
                    outputs.append(c)
                    #print ("Out:", outputs)
            else:
                if c in outputs:
                    outputs.remove(c)
                inputs.remove(c)
                c.close()
                print ("Disconnect")
                del message_queues[c]

    for c in wlist:
        try:
            next_msg = message_queues[c].get_nowait()
        except queue.Empty:
            outputs.remove(c)
        else:
            c.send(next_msg)

    for c in elist:
        inputs.remove(c)
        if c in outputs:
            outputs.remove(c)
        c.close()
        del message_queues[c]
    

#connection, addr = server.accept()
#print("Connected to:",addr)

#    while True:
#        data = connection.recv(1024)
#        print ("Message:",data.decode())
#        if not data:
#            break
#       connection.sendall(data)
#server.close()
#print ("Connection close")
