# # An example script to connect to localhost using socket 
# # programming in Python 
import socket # for socket 
import sys 

try: 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	print ("Socket successfully created")
except socket.error as err: 
	print ("socket creation failed with error %s" %(err))

# default port for socket 
port = 3000
host_ip = "127.0.0.1"

# connecting to the server 

print ("the socket is serving on localhost") 

# s.bind(('', port))
# s.listen(5)
# c, addr = s.accept()
# print ("Socket Up and running with a connection from",addr)
# while True:
#     rcvdData = c.recv(1024).decode()
#     print ("S:",rcvdData)

# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8089))
s.listen(5) # become a server socket, maximum 5 connections

connection, address = s.accept()
while True:
    buf = connection.recv(64)
    if len(buf) > 0:
        print (buf)
        break