import sockets
import sys
import parser
import sockets
import cPickle as pickle

"""
   I think I should make it so return_label returns 1 or more strings to send 
   back to the user. Don't want any server shit in there.

   That's where we have the array. so like ['What is the command?', 'What is the label?']

   this will go through the array, send one string, wait for a response, then send another
"""

cll = parser.cll
classifier_file = parser.classifier_file

while True:  
   command = sockets.recv(1024)
   if not command: break
   return_label, risk = parser.parseCommand(command, cll, classifier_file)
   print "return_label: " + str(return_label)
   print "risk: " + str(risk)
   if return_label == "greeting":
      sockets.send("Hello!")
   if return_label == "new command":
      parser.learn_new_command(command)
   if return_label == "test command":
      parser.test_command(cll)
   if return_label == "train":
      parser.train()
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