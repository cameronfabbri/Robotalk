"""
Cameron Fabbri
2/18/2016

simple script to connect to server for testing

"""
import socket
import os

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
except:
    print "Could not connect to client. Check that it is running"
    exit()
while True:
   command = raw_input("> ")
   s.sendall(command)
   response = s.recv(BUFFER_SIZE)
   print "response: " + str(response)
print "closed"
s.close()
