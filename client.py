# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 

# default port for socket 
port = 3000
host_ip = "127.0.0.1"	

# connect to the server on local computer 
s.connect((host_ip, port)) 

while True:
    str = "its 1:53pm on Thursday."
    s.send(str.encode())
    # if(str == "Bye" or str == "bye"):
    #     break
    # print "N:",s.recv(1024).decode()
s.close() #close connection

# # receive data from the server and decoding to get the string.
# # print (s.recv(1024).decode())
# # close the connection 
# # s.close()	 

# clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientsocket.connect(('localhost', 8089))
# clientsocket.send(bytes('its the afternoon', "UTF-8"))