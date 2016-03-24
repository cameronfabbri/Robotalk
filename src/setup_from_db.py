from pymongo import MongoClient 
from textblob.classifiers import NaiveBayesClassifier
import cPickle as pickle

"""

Cameron Fabbri

This trains a classifier from commands in a database

"""

client = MongoClient('localhost', 27000)
db = client.smartTalk_db
collection = db.responses

filename = "classifier.pickle"

train_list = list()
for row in collection.find({}):
   command = row['command']
   label = row['label']
   train_list.append([command,label])   

cll = NaiveBayesClassifier(train_list)
f = open(filename, 'wb')
pickle.dump(cll, f)

print "Wrote classifier to " + filename
