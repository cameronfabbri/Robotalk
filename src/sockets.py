import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
print "Server ready"
s.listen(1)
conn, addr = s.accept()

def send(message):
   conn.send(message)


def recv(message):
   return conn.recv(message)