import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print "done"

def send(message):
	conn.send(message)

def recv(message):
	return conn.recv(message)


#receive array seeing if there is a new 
# data structures for sending and receiving
# thread for each