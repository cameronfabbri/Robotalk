from random import randint
import sockets
import parser
import time
from pymongo import MongoClient 
import built_in

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
      post = {"label":return_label, "command":command}
      collection.insert(post)
      n = collection.find({"label":"greeting"}).count()
      rand_n = randint(0,n)
      random_greeting = collection.find({"label":"greeting"}).limit(1).skip(rand_n)
      for r in random_greeting:
         response = r['command']
      sockets.send(str(response))
      continue
   elif return_label == "test command":
      built_in.test_command(cll)
      continue
   elif return_label == "train":
      built_in.train(cll)
      continue
   # elif return_label = "your label here"
   # call_algorithm
   else:
      print "Adding " + command + " to database with label " + return_label
      post = {"label":return_label, "command":command}
      collection.insert(post)
      command_label_risk = [command, return_label, risk]
      response = "Got it!"
      sockets.send(response)
      continue
