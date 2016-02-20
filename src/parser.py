from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import numpy as np
import operator
import cPickle as pickle
import time
import sys
import socket

# Your configuration file(s)
import config
#import server

#BUFFER_SIZE = server.BUFFER_SIZE

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

def train():
   server.send("Tell me the label:\n")
   label = server.recv(BUFFER_SIZE)
   command = raw_input("Tell me the command:\n")
   new_data = [(command, label)]
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)

def test_command(cll):
   server.send("What command would you like to test?\n")
   command = server.recv(BUFFER_SIZE)
   mpl = -1
   labels = cll.labels()
   prob_dist = cll.prob_classify(command)
   for label in labels:
      if prob_dist.prob(label) > prob_dist.prob(mpl):
         mpl = label
   server.send("I think this is a " + str(mpl) + " command")
   
def learn_new_command(command):
   print "in learn new command"
   server.send("What type of command is this? (The label for the command, one word only)")
   new_label = server.recv(BUFFER_SIZE)
   print new_label
   print "Here..."
   if new_label == "no command":
      return -1
   #conn.send("new label: " + str(new_label))
   server.send("got new label")
   print "Sent label..."
   new_command = server.recv(BUFFER_SIZE)
   server.send("Got it")
   print "Asked for new label"
   #new_command = raw_input("New Command: ")
   new_data = [(new_command, new_label)]
   cll.update(new_data)
   
   #conn.send("Saving new classifier...")
   #conn.send("It is suggested you give me more than one example for this new command!")
   #conn.send("Tell me to train so you can give me more to learn!")
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)
   return -1

def update_classifier(cll, prob_label_dict):
   server.send("Please give me an example command for which this falls into\n")
   l = server.recv(BUFFER_SIZE)
   # This is if you actually don't want to update the classifier
   if l == "no command":
      return -1
   # This returns a label
   ll = TextBlob(l, classifier=cll).classify()

   # find the probabilities of the commands, sort them, then ask in descending order
   prob_label_dict = sorted(prob_label_dict.items(), key=operator.itemgetter(1))[::-1]
   prob_label_list = list(prob_label_dict)
   
   new_label = prob_label_list[0][0]
   server.send("Adding command " + str(command) + " with label " + str(new_label))

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
         print "Built in.."
         return True
   return False
"""
   This is updating the classifier when we know what label it should be
"""
def addKnowledge(new_data, cll):
   cll.update(new_data)
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)

def show_labels(cll):
   labels = cll.labels()
   
   server.send("a")

"""
   Parses the command given, returns a json blob of possible location, object, subject, etc
"""
def parseCommand(command, cll, classifier_file):
   print "Here"
   confidence_threshold = config.confidence_threshold
   prob_dist            = cll.prob_classify(command)
   labels               = cll.labels()
   prob_label_dict      = dict()

   # most probable label.
   mpl  = -1

   # before using the classifier, check if it is a built in command
   if isBuiltIn(command):
      return command

   test_list = list()
   for label in labels:
      if prob_dist.prob(label) > prob_dist.prob(mpl):
         mpl = label
      # Uncomment if you want to see the server print out each prob
      #print "Probability for label " + str(label) + ": " + str(prob_dist.prob(label))
      test_list.append("Probability for label " + str(label) + ": " + str(prob_dist.prob(label)))
      prob_label_dict[label] = prob_dist.prob(label)
   # Uncomment if you want to send back the entire list of probs
   #conn.send(str(test_list))
   server.send("Most probable label: " + str(mpl) + ", prob: " + str(prob_dist.prob(mpl)))

   # this is if the threshold wasn't passed. Add more to knowledge
   if prob_dist.prob(mpl) < confidence_threshold:
      server.send("Is this a " + mpl + " command?\n")
      a = server.recv(BUFFER_SIZE)
      if a == "yes":
         new_data = [(command, mpl)]
         addKnowledge(new_data, cll)
         return mpl
      else:
         server.send("Want to add this to something I already know?\n")
         ans = server.recv(BUFFER_SIZE)
         if ans == "yes":
            return update_classifier(cll, prob_label_dict)
         else:
            server.send("Okay then!")
            return -1

   # add what was just said to the classifier if it passed the threshold
   if prob_dist.prob(mpl) > confidence_threshold:
      new_data = [(command, mpl)]
      addKnowledge(new_data, cll)
      server.send("Adding " + str(new_data) + " to classifier")
   return mpl


         #return_label = parseCommand(command, cll, classifier_file)         
# This return label is what is sent to the robot
# The developer has to link this label with their functions


"""
# I think I should change this...


if return_label == "train":
   train()

if return_label == "test command":
   test_command(cll)

if return_label == "show labels":
   show_labels(cll)
"""

