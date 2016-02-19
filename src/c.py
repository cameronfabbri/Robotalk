import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print "Connecting to " + str(server_address)
sock.connect(server_address)

try:
    command = raw_input("> ")
    sock.sendall(command)
    response = sock.recv(1024)
    print response
finally:
    sock.close()
