# SERVER 
# Created By: Theo Gonzales
# Project Name: PenTest Basic Programming | ine.com
# Description: Internal program that binds itself to a specific address
#               and port and will listen for incoming TCP Communications.
# Vector: The SolGon Network

import socket

SRV_ADDR = input("Server IP Address: ")
SRV_PORT = int(input("Server Port: "))
#Create a new socket that uses TCP; AF_INET, SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
# Start of communication loop to the client
s.listen(1)
print("SGN Server Started. Waiting For Connections")
# Function to collect client address bound to the socket
connection, address = s.accept()
print("Client Connected With Address", address)
# Maximum Queued Connections: 1
while 1:
        data = connection.recv(1024)
        if not data: break
        connection.sendall(b'-- Message Recieved --\n')
        print(data.decode('utf-8'))
connection.close()
# Optional Connection Client(s): netcat
