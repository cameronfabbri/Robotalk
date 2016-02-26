from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

"""

Cameron Fabbri
2/19/2016

personal assistant robot testing

This test simulates the case where a robot is to be a personal
assistant perhaps for an ederly person or someone who is just
lazy and has a lot of money

"""

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
   ('get the vacuum out of the closet and vacuum the hallway'      ,'clean'),
   ('can you pick up all this junk on the ground'                  , 'clean')
]

test = [
   ('take my plate and glass back to the kitchen please'   ,'deliver'),
   ('put this shirt on my bed please'                      ,'deliver'),
   ('can you put all of the dishes into the dishwasher'    ,'deliver'),
   ('get my car keys from the drawer'                      ,'get'),
   ('go to the fridge and grab me a beer please'           ,'get'),
   ('go get me another pair of socks from my dresser'      ,'get'),
   ('sweep up all of these crumbs on the floor'            ,'clean'),
   ('can you vacuum all of the bedrooms?'                 ,'clean'),
   ('pick all of this garbage off of the ground'           ,'clean')
]

print "Training..."
cll = NaiveBayesClassifier(train)
print "Done training\n"
labels = cll.labels()

x = range(0,len(test))
y = list()
mpl = labels[0]
x_ticks = list()

for command in test:
   c = command[0]
   prob_dist = cll.prob_classify(c)
   for label in labels:
      if prob_dist.prob(label) > prob_dist.prob(mpl):
         mpl = label
   x_ticks.append(mpl)
   y.append(prob_dist.prob(mpl))

sum_ = 0.0
for prob in y:
   sum_ = prob + sum_
accuracy = sum_/float(len(test))
print "Average Accuracy: " + str(accuracy)

axes = plt.gca()
axes.set_ylim([0,1])
plt.figure()
plt.xticks(x, x_ticks)
plt.plot(x,y, 'ro')
plt.savefig("butler_test_plot.png")
print "Plot saved as 'butler_test_plot.png'"