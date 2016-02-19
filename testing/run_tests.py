import cPickle as pickle
import sys


"""
Cameron Fabbri
2/19/2016

Testing script to run tests on the classifier

We want to see how the classifier performs based on
the amount of training it has had.

Need to tests a few labels and also a lot of labels

"""

# amount of labels to give the classifier

import imp
config = imp.load_source('module.name', '../src/config.py')

train = config.train
test = config.test

classifier_file = sys.argv[1]

try:
   cll = pickle.load(open(classifier_file, 'rb'))
   print "Loaded classifier"
except:
   raise

print "Testing base classifier..."
print cll.accuracy(test)
