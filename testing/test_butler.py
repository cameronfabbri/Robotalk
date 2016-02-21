from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import DecisionTreeClassifier
from textblob.classifiers import MaxEntClassifier

"""

Cameron Fabbri
2/19/2016

personal assistant robot testing

This test simulates the case where a robot is to be a personal
assistant perhaps for an ederly person or someone who is just
lazy and has a lot of money

"""

# labels: deliver, get, note, clean, secure
train = [
   ('bring my plates to the kitchen and put them on the counter','deliver'),
   ('put my clothes in the hamper'                              ,'deliver'),
   ('put my mug into the dishwasher please'                     ,'deliver'),
   ('bring my trash outside and put it in the barrel'           ,'deliver'),
   ('throw my shoes in the closet'                              ,'deliver'),
   ('','deliver'),
   ('','get'),
   (''          ,'get'),
   (''                            ,'get'),
   (''            ,'get'),
   (''                         ,'get'),
   (''        ,'get'),
   (''               ,'get')
]

test = [
   ('bring these bottles of percocet back to the lab'           ,'deliver'),
   ('take these pills and bring them to the patient in room 124','deliver'),
   ('go get the scissors from the nurse'                        ,'get'),
   ('can you bring me the medicine from the lab'                ,'get'),
   ('listen to me'                                              ,'note'),
   ('alright take a note'                                       ,'note'),
   ('go to the operating room and mop up the floor'             ,'clean'),
   ('clean up the OR'                                           ,'clean'),
   ('pick up the trash in the hallway'                          ,'clean'),
   ('make sure the doors are locked'                            ,'secure'),
   ('alert the nurses we have intruders'                        ,'secure')
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
