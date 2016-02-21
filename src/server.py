import socket
import sys
import parser
import cPickle as pickle

if len(sys.argv) < 2:
   print "Usage: python server.py [classifier.file]"
   exit(-1)
classifier_file = sys.argv[1]

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
print "Server ready"
s.listen(1)
conn, addr = s.accept()

try:
   cll = pickle.load(open(classifier_file, 'rb'))  
   print "Loaded classifier"
except:
   raise
   exit(-1)

def send(message):
   print "Sending..."
   for m in message:
      conn.send(m)
      #recv(m)

def recv(message):
   return conn.recv(message)

"""
   I think I should make it so return_label returns 1 or more strings to send 
   back to the user. Don't want any server shit in there.

   That's where we have the array. so like ['What is the command?', 'What is the label?']

   this will go through the array, send one string, wait for a response, then send another
"""

while True:  
   command = recv(1024)
   if not command: break
   return_label = parser.parseCommand(command, cll, classifier_file)
   if return_label == "new command":
      parser.learn_new_command(command)
conn.close()

#receive array seeing if there is a new 
# data structures for sending and receiving
# thread for each

'''
send back message and bool and check if there's something 
else coming as well

server sends boolean

server waits for a message then sends his responses - he could send 4 or 1 or none
how many times does the client read from this connection -> if false don't read again

have tuple of string and bool, serialize it and send 

'''