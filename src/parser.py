from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import operator
import cPickle as pickle
import time
import sys

# Your configuration file(s)
import sockets
import config

BUFFER_SIZE = config.BUFFER_SIZE

"""
Cameron Fabbri
1/31/2016
Parser.py

Main file for the framework.  This will control the flow and call functions
from other classes.

We want to parse each command given. We will only be able to support a 
limited number of functions, then the developer using this will be able
to write their own algorithms.
"""

# classifier file defined in config.py
classifier_file = config.classifier_file
try:
   cll = pickle.load(open(classifier_file, 'rb'))  
   print "Loaded classifier"
except:
   print "No classifier found. run `setup.py` and enter the classifier filename in config.py"
   exit(-1)

"""
   Allows the user to input a label and command to better
   train the robot if it is having difficulty understanding

   This can also be used to learn a new command
"""
def train(cll):
   sockets.send("What's the label?")
   label    = sockets.recv(BUFFER_SIZE)
   sockets.send("What's the command?")
   command  = sockets.recv(BUFFER_SIZE)
   new_data = [(command, label)]
   cll.update(new_data)
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)
   sockets.send("Got it!")

"""
   Tests out a command
"""
def test_command(cll):
   sockets.send("What command would you like to test?")
   command = sockets.recv(BUFFER_SIZE)
   labels = cll.labels()
   mpl = labels[0]
   prob_dist = cll.prob_classify(command)
   for label in labels:
      if prob_dist.prob(label) > prob_dist.prob(mpl):
         mpl = label
   sockets.send("I think this is a %s command" %(str(mpl)))

"""
   This is updating the classifier when we know what label it should be
"""
def addKnowledge(new_data, cll):
   cll.update(new_data)
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)

def update_classifier(command, cll):
   #sockets.send("Please give me an example command for which this falls into\n")
   sockets.send("Ok what type of command is this?")
   new_label = sockets.recv(BUFFER_SIZE)
   if new_label != "no command":
      sockets.send("Okay, let's try that again then!")
      new_data = [(command, new_label)]
      cll.update(new_data)
      f = open(classifier_file, 'wb')
      pickle.dump(cll, f)

"""
   Method for handling built in commands.

   If the command is built in, the parser will simply return the command
   instead of the label, so make sure you handle that on the robot side.
"""
def isBuiltIn(command):
   built_in = config.built_in
   for b_command in built_in:
      if b_command == command:
         return True
   return False

"""
   Function programmable by the robotics researcher for their definition
   of what risk association they want
"""
def getRisk(command):
   return 0

"""
   Parses the command given, returns a json blob of possible location, object, subject, etc
"""
def parseCommand(command, cll, classifier_file):
   confidence_threshold = config.confidence_threshold
   prob_dist            = cll.prob_classify(command)
   labels               = cll.labels()
   prob_label_dict      = dict()
   risk = getRisk(command)
   mpl  = labels[0]

   # before using the classifier, check if it is a built in command
   if isBuiltIn(command):
      return command, getRisk(command)

   for label in labels:
      if prob_dist.prob(label) > prob_dist.prob(mpl):
         mpl = label
      prob_label_dict[label] = prob_dist.prob(label)
   print "Most probable label: " + str(mpl) + ", prob: " + str(prob_dist.prob(mpl))

   # this is if the threshold wasn't passed. Add more to knowledge
   if prob_dist.prob(mpl) < confidence_threshold:
      sockets.send("Is this a " + mpl + " command?")
      a = sockets.recv(BUFFER_SIZE)
      if a == "yes" or a == "yeah":
         new_data = [(command, mpl)]
         addKnowledge(new_data, cll)
         return mpl
      else:
         sockets.send("Want to add this to something I already know?")
         ans = sockets.recv(BUFFER_SIZE)
         if ans == "yes" or ans == "yeah":
            return update_classifier(command, cll)
         else:
            sockets.send("Okay then!")
            return -1

   # add what was just said to the classifier if it passed the threshold
   if prob_dist.prob(mpl) > confidence_threshold:
      new_data = [(command, mpl)]
      addKnowledge(new_data, cll)
   return mpl, risk
