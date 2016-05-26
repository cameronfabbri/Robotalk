import sockets
import parser
import time
#from pymongo import MongoClient 
import built_in
import algorithms

cll = parser.cll
classifier_file = parser.classifier_file

client = MongoClient('localhost', 27000)
db = client.smartTalk_db
collection = db.responses

while True:
   command = sockets.recv(1024)
   if not command: 
      break
   return_label, risk = parser.parseCommand(command, cll, classifier_file)
   print "return_label: " + str(return_label)
   print "risk: " + str(risk)
   if return_label == "greeting":
      response = algorithms.greet(return_label, command, collection) 
      sockets.send(str(response))
      continue
   elif return_label == "test command":
      built_in.test_command(cll)
      continue
   elif return_label == "train":
      built_in.train(cll, collection)
      continue
   # elif return_label = "your label here"
   # call_algorithm
   else:
      #post = {"label":return_label, "command":command}
      #collection.insert_one(post)
      command_label_risk = [command, return_label, risk]
      response = "Got it!"
      sockets.send(response)
      continue
