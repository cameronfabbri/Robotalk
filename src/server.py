import sockets
import sys
import parser
import sockets
import cPickle as pickle

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
      continue
   if return_label == "test command":
      parser.test_command(cll)
      continue
   if return_label == "train":
      parser.train(cll)
      continue
   else:
      label_risk = [command, return_label, risk]
      sockets.send(str(label_risk))
conn.close()