# Created By Theo Gonzales <solgonsol@protonmail.com>
#
SRV_ADDR =  input('Server address(ip): ')
SRV_PORT = input('Server port: ')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
print('Server has started successfully')
connection, address = s.accept()
print('You are connected to ', address)
while 1:
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b'--You Message has been Released successfuly--\n')
    print(data.decode('utf-8'))
connection.close()

