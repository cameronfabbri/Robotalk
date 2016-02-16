from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import numpy as np
import operator
import cPickle as pickle
import time
import sys
# Your configuration file(s)
import config

"""

Cameron Fabbri
1/31/2016
Parser.py

Main file for the framework.  This will control the flow and call functions
from other classes.

We want to parse each command given. We will only be able to support a 
limited number of functions, then the developer using this will be able
to write their own algorithms.


TODO when adding a new command, need to have a few more similar commands
be put in. Also don't add it automatically, check for confirmation and
loop through the possible commands

"""

if len(sys.argv) < 2:
   print "Usage: python parser.py [classifier.file]"
   exit(-1)
classifier_file = sys.argv[1]

try:
   cll = pickle.load(open(classifier_file, 'rb'))  
   print "Loaded classifier"
except:
   print "No classifier found or file corrupted! Run setup.py first to train a base classifier"
   exit(-1)

def learn_new_command(command):
   print "Okay learning a new command...\n"
   new_label = raw_input("What type of command is this? (The label for the command, one word only)\n")
   if new_label = "no command":
      return -1
   print "new label: " + str(new_label)
   new_command = raw_input("New Command: ")
   new_data = [(new_command, new_label)]
   cll.update(new_data)
   print "Saving new classifier..."
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)
   return -1

def update_classifier(cll, prob_label_dict):
   l = raw_input("Please give me an example command for which this falls into\n")
   # This is if you actually don't want to update the classifier
   if l == "no command":
      return -1
   # This returns a label
   ll = TextBlob(l, classifier=cll).classify()

   # find the probabilities of the commands, sort them, then ask in descending order
   prob_label_dict = sorted(prob_label_dict.items(), key=operator.itemgetter(1))[::-1]
   prob_label_list = list(prob_label_dict)
   
   new_label = prob_label_list[0][0]
   print "Adding command " + str(command) + " with label " + str(new_label)

   new_data = [(command, new_label)]
   cll.update(new_data)
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)
   return -1


"""
   Method for handling built in commands. Built in commands should only
   be one word commands that are hard to classify or are used frequently
   e.g "exit", "hello", "stop", etc

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
   Parses the command given, returns a json blob of possible location, object, subject, etc
"""
def parseCommand(command, cll, classifier_file):
   confidence_threshold = config.confidence_threshold
   prob_dist            = cll.prob_classify(command)
   labels               = cll.labels()
   prob_label_dict      = dict()

   # most probable label.
   mpl  = -1

   # before using the classifier, check if it is a built in command
   if isBuiltIn(command):
      return command

   for label in labels:
      if prob_dist.prob(label) > prob_dist.prob(mpl):
         mpl = label
      print "Probability for label " + str(label) + ": " + str(prob_dist.prob(label))
      prob_label_dict[label] = prob_dist.prob(label)
   print "Most probable label: " + str(mpl)          

   # This is for learning a brand new command / label
   #if mpl == learn_label and prob_dist.prob(mpl) > confidence_threshold:
   #   return learn_new_command(command, labels)

   # this is if the threshold wasn't passed. Add more to knowledge
   if prob_dist.prob(mpl) < confidence_threshold:
      a = raw_input("Is this a " + mpl + " command?\n")
      if a == "yes":
         return mpl
      else:
         ans = raw_input("Want to add this to something I already know?\n")
         if ans == "yes":
            return update_classifier(cll, prob_label_dict)
   return mpl

while True:
   command = raw_input("> ")
   s = time.time()

   # This return label is what is sent to the robot
   # The developer has to link this label with their functions
   return_label = parseCommand(command, cll, classifier_file)
   print "return label: " + str(return_label)

   if return_label == "new command":
      learn_new_command(command)