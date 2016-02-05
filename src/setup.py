from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import numpy as np
import time
import pickle

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

print "Training classifier..."
s = time.time()
train = config.train
cll = NaiveBayesClassifier(train)
print "Training complete " + str(time.time()-s)
s = time.time()
print "Saving classifier..."
with open('classifier.pickle', 'wb') as handle:
   pickle.dump(train, handle)
