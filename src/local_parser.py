from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import numpy as np
import operator
import cPickle as pickle
import time
import sys
import socket
import os

# Your configuration file(s)
import config

"""

Cameron Fabbri
1/31/2016
Parser.py

This will be a local parser if the user does not want to use a seperate interface to 
communicate with the robot. It will use Google speech recognition, and the robot must
have a mic obviously

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

def train():
   os.system("espeak 'What is the label'")
   label = raw_input("> ")
   command = raw_input("What is the command:\n")
   new_data = [(command, label)]
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)
   os.system("espeak 'Alright'")
   return -1

def test_command(cll):
   os.system("espeak 'What command would you like to test?'")
   command = raw_input("> ")
   mpl = -1
   labels = cll.labels()
   prob_dist = cll.prob_classify(command)
   for label in labels:
      if prob_dist.prob(label) > prob_dist.prob(mpl):
         mpl = label
   os.system("espeak 'I think this is a %s command'" %(str(mpl)))
   
def learn_new_command(command):
   os.system("espeak 'What type of command is this?'")
   new_label = raw_input("> ")
   if new_label == "no command":
      return -1
   os.system("espeak 'What is the command?'")
   new_command = raw_input("> ")
   new_data = [(new_command, new_label)]
   cll.update(new_data)
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)
   os.system("espeak 'Got it'")
   return -1

# Should probably add a check if the highest probability isn't passed the threshold
# for this make a checker function
def update_classifier(cll, prob_label_dict):
   os.system("espeak 'Please give me an example command for which this falls into'")
   l = raw_input("> ")
   # This is if you actually don't want to update the classifier
   if l == "no command":
      return -1
   # This returns a label
   ll = TextBlob(l, classifier=cll).classify()

   # find the probabilities of the commands, sort them, then ask in descending order
   prob_label_dict = sorted(prob_label_dict.items(), key=operator.itemgetter(1))[::-1]
   prob_label_list = list(prob_label_dict)
   new_label = prob_label_list[0][0]
   os.system("espeak 'Adding command %s with label %s'" %(str(command), str(new_label)))
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
   This is updating the classifier when we know what label it should be
"""
def addKnowledge(new_data, cll):
   cll.update(new_data)
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)

def show_labels(cll):
   labels = cll.labels()
   

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
   os.system("espeak 'Most probable label %s'" %(str(mpl)))
   print "Most probable label: " + str(mpl)

   # this is if the threshold wasn't passed. Add more to knowledge
   if prob_dist.prob(mpl) < confidence_threshold:
      os.system("espeak 'Is this a %s command?'" %mpl)
      a = raw_input("> ")
      if a == "yes":
         new_data = [(command, mpl)]
         addKnowledge(new_data, cll)
         return mpl
      else:
         os.system("espeak 'Want to add this to something I already know?'")
         ans = raw_input("> ")
         if ans == "yes":
            return update_classifier(cll, prob_label_dict)
         else:
            os.system("espeak 'Okay then!'")
            return -1

   # add what was just said to the classifier if it passed the threshold
   if prob_dist.prob(mpl) > confidence_threshold:
      new_data = [(command, mpl)]
      addKnowledge(new_data, cll)
   return mpl

while True:
   command = raw_input("> ")
   return_label = parseCommand(command, cll, classifier_file)         

   # This return label is what is sent to the robot
   # The developer has to link this label with their functions
   
   # I think I should change this...
   if return_label == "new command":
      learn_new_command(command)

   if return_label == "train":
      train()

   if return_label == "test command":
      test_command(cll)

   if return_label == "show labels":
      show_labels(cll)

