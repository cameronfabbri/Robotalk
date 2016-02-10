from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import numpy as np
import time
import cPickle as pickle

# Your config file with training sets
import config


"""

Cameron Fabbri
1/31/2016
setup.py

A setup file where the user can define their application parameters.
This setup file trains the classifiers and puts the 'cl' object into
the database

"""

def train(filename):
   print "Training classifier..."
   s = time.time()
   train = config.train
   cll = NaiveBayesClassifier(train)
   print "Training complete " + str(time.time()-s)
   s = time.time()
   print "Saving classifier..."
   f = open(filename, 'wb')
   pickle.dump(cll, f)
   #with open(filename, 'wb') as handle:
      #pickle.dump(train, handle)
   #   pickle.dump(cll, handle)

try:
   with open('classifier.pickle', 'r'):
      inp = raw_input("A classifier has already been trained! Enter in a new filename or simply enter 'o' to overwrite the current classifier\n")
      if inp == "o":
         train("classifier.pickle")
      else:
         train(inp)
except:
   train("classifier.pickle")
