# CLIENT SIDE
# Created By: Theo Gonzales
# Description: 
# Vector: The SolGon Network

import socket

SRV_ADDR = input("Server IP Address: ")
SRV_PORT = int(input("Server Port: "))



my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if my_sock.connect((SRV_ADDR, SRV_PORT)) == ConnectionRefusedError:
    print("Connection Refused!")
else:
    print("Connection Established")
    print("WARNING: Connection is not secured. All traffic is unencrypted!")


message = input("Message To Send: ")
my_sock.sendall(message.encode())
my_sock.close()
