import socket
import select
import queue

server_address = ('127.0.0.1', 1024)
print ("Serv addr:", server_address)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen(5)
server.setblocking(0)

inputs = [server]
outputs = []
message_queues = {}

#storage = open('history', 'r+')

while inputs:
    rlist, wlist, elist = select.select(inputs, outputs, inputs)
    for c in rlist:
        if c is server:
            connection, addr = c.accept()
            print("Connected to", addr[1])
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = queue.Queue()
            #if os.stat("history").st_size > 0:
            #    c.send(storage.read().encode())
        else:
            data = c.recv(1024)
            print("Message: ", data.decode())
            #c.send(data)
            if data:
                message_queues[c].put(data)
                if c not in outputs:
                    outputs.append(c)

            else:
                if c in outputs:
                    outputs.remove(c)
                inputs.remove(c)
                c.close()
                print("Disconnect")
                del message_queues[c]

    for c in wlist:
        try:
            next_msg = message_queues[c].get_nowait()
        except queue.Empty:
            outputs.remove(c)
        else:
            c.send(next_msg)
#            storage.write(next_msg.decode())

    for c in elist:
        inputs.remove(c)
        if c in outputs:
            outputs.remove(c)
        c.close()
        del message_queues[c]
    if len(inputs) == 1 and len(outputs) == 0:
        print("Server closed")
        server.close()
        break



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
