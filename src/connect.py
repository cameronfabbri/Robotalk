"""
Cameron Fabbri
2/18/2016

simple script to connect to server for testing

"""
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024


while True:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((TCP_IP, TCP_PORT))
   
   print " < " + str(data)
   response = raw_input("Reply: ")
   s.sendall(response)
s.close()
