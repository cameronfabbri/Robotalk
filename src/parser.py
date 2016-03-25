from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import operator
import cPickle as pickle
import time
import sys

# Your configuration file(s)
import sockets
import config
import built_in
import algorithms

BUFFER_SIZE = config.BUFFER_SIZE

"""

Cameron Fabbri
1/31/2016
parser.py

Main file for the framework.  This will control the flow and call functions
from other classes.

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
   This is updating the classifier when we know what label it should be
"""
def addKnowledge(new_data, cll):
   cll.update(new_data)
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)

"""
   Updates the classifier when it is confused on a command
"""
def update_classifier(command, cll):
   sockets.send("Ok what type of command is this?")
   new_label = sockets.recv(BUFFER_SIZE)
   if new_label != "no command":
      sockets.send("Okay, let's try that again then!")
      new_data = [(command, new_label)]
      cll.update(new_data)
      f = open(classifier_file, 'wb')
      pickle.dump(cll, f)

"""
   Function for handling built in commands.
"""
def isBuiltIn(command):
   return command in config.built_in

"""
   Parses the given command. Returns a tuple of the most probable label and the
   associated risk. 
"""
def parseCommand(command, cll, classifier_file):
   confidence_threshold = config.confidence_threshold
   prob_dist            = cll.prob_classify(command)
   labels               = cll.labels()
   prob_label_dict      = dict()
   risk = algorithms.getRisk(command)
   mpl  = labels[0]

   # for correcting spelling mistakes, don't think i'll use this
   #command = str(TextBlob(command).correct())
   #print "Corrected command " + command
   
   # before using the classifier, check if it is a built in command
   if isBuiltIn(command):
      return command, algorithms.getRisk(command)

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
         return mpl, risk
      else:
         sockets.send("Want to add this to something I already know?")
         ans = sockets.recv(BUFFER_SIZE)
         if ans == "yes" or ans == "yeah":
            update_classifier(command, cll)
            return -1, 0
         else:
            sockets.send("Okay then!")
            return -1, 0

   # add what was just said to the classifier if it passed the threshold
   if prob_dist.prob(mpl) > confidence_threshold:
      new_data = [(command, mpl)]
      addKnowledge(new_data, cll)
   return mpl, risk
