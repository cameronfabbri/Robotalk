from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import MaxEntClassifier
import numpy as np
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


If it doesn't understand something, say 'I didn't understand that, what 
would you like me to learn?'' Say the category, or have it list categories.
Create new category if it doesn't have it.

Look at word2vec for possible multiclassification

"""

class Parser(object):

	# Load in config parameters
	greeting_train = config.greeting_train
	coffee_train   = config.coffee_train

	def __init__(self, command):
		self.command = command

	"""
		Determines whether or not the command given is safe to
		execute.  
	"""
	def computeSafety(command):
		print "Computing safety"

	"""
		Returns the command
	"""
	def getCommand(command):
		return command

	def go(command, location):
		print 

	"""
		Parses the command given, returns a json blob of possible location, object, subject, etc
	"""
	def parseCommand(command, cll):
		if command == "bye":
			exit()
		# First check if we have a matching command. If not, try and figure it out.
		#command_analyzed = cl.classify(command)
		prob_dist = cll.prob_classify(command)
		print prob_dist.max()
		#prob_dist.max()
		#prob_dist = prob_dist.prob("positive")
		#print 'Command: ' + command
		#print 'Probability: ' + str(prob_dist)
		#blob = TextBlob(command)
		#tags = blob.tags


	while True:
		# TODO put this trainer in the setup file, and pickle it and put it in the db, then grab it
		cll = NaiveBayesClassifier(coffee_train)
		#cll = MaxEntClassifier(coffee_train)
		command = raw_input("> ")
		s = time.time()
		parseCommand(command, cll)
		print "Parse command took " + str(time.time() - s) + " seconds..."
