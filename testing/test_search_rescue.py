from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import DecisionTreeClassifier
from textblob.classifiers import MaxEntClassifier

"""

Cameron Fabbri
2/19/2016

search and rescue team test

This test simulates the case where a robot is working on a search and
rescue team, so is trained on specific commands

"""

# labels: deliver, get, note, clean, secure
train = [
   
]

test = [

]

nbayes = NaiveBayesClassifier(train)
n_acc = nbayes.accuracy(test)

decision = DecisionTreeClassifier(train)
d_acc = decision.accuracy(test)

max_ent = MaxEntClassifier(train)
m_acc = max_ent.accuracy(test)

print "\nNaive Bayes accuracy: " + str(n_acc)
print "Decision Tree accuracy: " + str(d_acc)
print "MaxEnt accuracy: " + str(m_acc)
