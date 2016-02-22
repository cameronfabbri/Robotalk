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
   ('bring my plates to the kitchen and put them on the counter'   ,'deliver'),
   ('put my clothes in the hamper'                                 ,'deliver'),
   ('put my mug into the dishwasher please'                        ,'deliver'),
   ('bring my trash outside and put it in the barrel'              ,'deliver'),
   ('throw my shoes in the closet'                                 ,'deliver'),
   ('take this glass to the kitchen'                               ,'deliver'),
   ('get me my shoes from the closet'                              ,'get'),
   ('bring me the remote'                                          ,'get'),
   ('go grab my clothes from the dryer'                            ,'get'),
   ('can you go get the mail please'                               ,'get'),
   ('can you go to the cellar and get me a bottle of soda'         ,'get'),
   ('hurry up and get me my keys, we\'re late.'                    ,'get'),
   ('clean up this mess'                                           ,'clean'),
   ('sweep up the kitchen'                                         ,'clean'),
   ('pick up all of my clothes off of the ground and put them away','clean'),
   ('get the vaccuum out and vaccuum the hallway'                  ,'clean'),
   ('can you pick up all this junk on the ground'                  , 'clean')
]

test = [
   ('take my plate and glass back to the kitchen please'   ,'deliver'),
   ('put this shirt on my bed please'                      ,'deliver'),
   ('can you put all of the dishes in the dishwasher away' ,'deliver'),
   ('get my car keys from the drawer'                      ,'get'),
   ('go to the fridge and grab me a beer please'           ,'get'),
   ('go get me another pair of socks from my dresser'      ,'get'),
   ('sweep up all of these crumbs on the floor'            ,'clean'),
   ('can you vaccumm all of the bedrooms?'                 ,'clean'),
   ('pick all of this garbage off of the ground'           ,'clean')
]

nbayes = NaiveBayesClassifier(train)
n_acc = nbayes.accuracy(test)

decision = DecisionTreeClassifier(train)
d_acc = decision.accuracy(test)

#max_ent = MaxEntClassifier(train)
#m_acc = max_ent.accuracy(test)

print "\nNaive Bayes accuracy: " + str(n_acc)
print "Decision Tree accuracy: " + str(d_acc)
#print "MaxEnt accuracy: " + str(m_acc)
