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

def learn_new_command(command, labels):
   print "Okay learning a new command...\n"
   # get last label used
   last_label = labels[::-1]
   ll = last_label[0]         
   new_label = ll + 1
   print "new label: " + str(new_label)
   new_command = raw_input("New Command: ")
   new_data = [(new_command, new_label)]
   cll.update(new_data)
   print "Saving new classifier..."
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)
   return -1

def update_classifier(cll, prob_label_dict):
   print "I'm not sure what you mean...\n"
   l = raw_input("Please give me an example command for which this falls into\n")

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

def isBuiltIn(command):
   built_in = config.built_in
   print built_in
   for b_command in built_in:
      if b_command == command:
         print "Built in command " + str(command)
         exit()

"""
   Parses the command given, returns a json blob of possible location, object, subject, etc
"""
def parseCommand(command, cll, classifier_file):
   confidence_threshold = config.confidence_threshold
   entrance_label       = config.entrance_label
   learn_label          = config.learn_label
   exit_label           = config.exit_label
   prob_dist            = cll.prob_classify(command)
   labels               = cll.labels()
   prob_label_dict      = dict()

   # most probable label.
   mpl  = 0 
   # This will print out the label it thinks it is
   #blob = TextBlob(command, classifier=cll)
   #print blob.classify()

   # before using the classifier, check if it is a built in command
   isBuiltIn(command)

   for label in labels:
      if prob_dist.prob(label) > prob_dist.prob(mpl):
         mpl = label
      print "Probability for label " + str(label) + ": " + str(prob_dist.prob(label))
      prob_label_dict[label] = prob_dist.prob(label)
   print "Most probable label: " + str(mpl)          

   # Maybe for short commands just have them built in
   if mpl == exit_label and prob_dist.prob(mpl) > confidence_threshold:
      print "Goodbye!"

   # This is for learning a brand new command / label
   if mpl == learn_label and prob_dist.prob(mpl) > confidence_threshold:
      learn_new_command(command, labels)

   # this is if the threshold wasn't passed. Add more to knowledge
   if prob_dist.prob(mpl) < confidence_threshold:
      update_classifier(cll, prob_label_dict)

   return mpl

while True:
   command = raw_input("> ")
   s = time.time()

   # This return label is what is sent to the robot
   # The developer has to link this label with their functions
   return_label = parseCommand(command, cll, classifier_file)
   print "return label: " + str(return_label)