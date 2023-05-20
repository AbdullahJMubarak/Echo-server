import socket
import sys
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=("127.0.0.1",50000)

client.connect(server_address)
while True :
    msg=input("Enter The Message wanted to be sent: ")
    print("THe message which is sent: ",msg)
    client.sendall(msg.encode("utf-8"))


    data=client.recv(1000).decode("utf-8")
    print("The echo:" ,data)
    if data=="quit":
        break
client.close()
