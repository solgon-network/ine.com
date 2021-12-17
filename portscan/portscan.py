# Internal Port Scanner
# Created By: Theo Gonzales
# Project Name: CogTerm
# Description: 
# Vector: The SolGon Network

import socket
# Gather host & port range to scan
target = input("IP of host: ")
portrange = input("Port Range: ")
# Functions for port range
lowport = int(portrange.split('_') [0])
highport = int(portrange.split('_' [1]))

print("Scanning Host ", target, "From Port", lowport, "To Port", highport)

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print("*** Port", port, "- OPEN ***")
    else:
        print("*** Port", port, "- CLOSED ***")
    s.close()

