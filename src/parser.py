from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import numpy as np
import cpickle as pickle
import time

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

"""

class Parser(object):

   # Load in config parameters
   # TODO change this so it can be sent in as a parameter, allow multiple classifiers
   try:
      with open('classifier.pickle', 'rb') as handle:
         train = pickle.load(handle)
         cll = NaiveBayesClassifier(train)
      print "Loaded classifier"
   except:
      print "No classifier found! Run setup.py first to train a base classifier"
      exit(1)

   def __init__(self, command):
      self.command = command

   """
      Parses the command given, returns a json blob of possible location, object, subject, etc
   """
   def parseCommand(command, cll):
      prob_dist = cll.prob_classify(command)
      most_probable_label = 0
      for num in range(0, config.num_labels):
         if prob_dist.prob(num) > prob_dist.prob(most_probable_label):
            most_probable_label = num
         print "Probability for label " + str(num) + ": " + str(prob_dist.prob(num))
      print "Most probable label: " + str(most_probable_label)

   while True:
      command = raw_input("> ")
      s = time.time()
      parseCommand(command, cll)
