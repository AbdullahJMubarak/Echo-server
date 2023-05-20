import socket
import sys
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("127.0.0.1",50000)
server.bind(server_address)
server.listen(1)
print('Ready for any connection')
connection, client_address=server.accept()
print('connection established with: ',client_address)
while True :
    data=connection.recv(1000).decode("utf-8")
    print('The messsage recieved ',data)
    
    # print("type: ",type(data))
    # data= str(data)
   
    
    if data[0] == 'A' :
        print("type: ",data[0])
        data=data[1:]
        data=sorted(data)
        data= str(data)

        connection.sendall(data.encode("utf-8"))
    elif data[0] == 'C' :
        print("type: ",data[0])
        data=data[1:]
        data= str(data)
        data=data.upper()
        print(data)
        connection.sendall(data.encode("utf-8"))
    elif data[0] == 'D' :
        print("type: ",data[0])
        data=data[1:]
        data=sorted(data,reverse=True)
        data= str(data)
        connection.sendall(data.encode("utf-8"))
    else:
        print("No type ")
        connection.sendall(data.encode("utf-8"))
        if data=="quit" :
            break


connection.close()
server.close()
