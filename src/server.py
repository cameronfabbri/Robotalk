import sockets
import parser
import time

cll = parser.cll
classifier_file = parser.classifier_file

def get_return():
   while True:
      command = sockets.recv(1024)
      if not command: break
      return_label, risk = parser.parseCommand(command, cll, classifier_file)
      print "return_label: " + str(return_label)
      print "risk: " + str(risk)
      if return_label == "greeting":
   	     # function here that keeps track of what the user uses as a greeting
   	     # then takes a random sample of one from the top. Maybe a gausian distro
         sockets.send("Hello!")
         continue
      if return_label == "test command":
         parser.test_command(cll)
         continue
      if return_label == "train":
         parser.train(cll)
         continue
      if return_label == "bye":
   		sockets.conn.close()
   		exit()
      else:
         command_label_risk = [command, return_label, risk]
         sockets.send(str(command_label_risk))
         return str(command_label_risk)
         # return to the user here in their script

get_return()