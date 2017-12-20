""" Python3 code - Banner Grabbing using Socket programming """

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host_tar = input("Enter the host name: ")
port_tar = int(input("Enter Port: "))

s.connect((host_tar,port_tar))

s.send(('GET HTTP/1.1 \r\n').encode())

ret = s.recv(1024)

print(str(ret))