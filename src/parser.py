from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import MaxEntClassifier
import numpy as np
import pickle
#tb = Blobber(analyzer=NaiveBayesClassifier())


import json
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
   with open('classifier.pickle', 'rb') as handle:
      train = pickle.load(handle)
   print "Loaded classifier"

   def __init__(self, command):
      self.command = command

   """
      Parses the command given, returns a json blob of possible location, object, subject, etc
   """
   def parseCommand(command, cll):
      if command == "bye":
         exit()
      # First check if we have a matching command. If not, try and figure it out.
      #command_analyzed = cl.classify(command)
      prob_dist = cll.prob_classify(command)
      # Use this to find what label is the highest
      for num in range(0, config.num_labels):
         print "Probability for label " + str(num) + ": " + str(prob_dist.prob(num))


   while True:
      # TODO put this trainer in the setup file, and pickle it and put it in the db, then grab it
      cll = NaiveBayesClassifier(train)
      command = raw_input("> ")
      s = time.time()
      parseCommand(command, cll)
#      print "Parse command took " + str(time.time() - s) + " seconds..."
