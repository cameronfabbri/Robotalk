from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

"""
Cameron Fabbri
2/19/2016

hospital test

This test simulates the case where a robot is to be 
used in a hospital. The classifier is trained on hospital
specific commands

TODO: Write a test script that combines the three into one classifier
could have it start with one, then update using another's train data,
then test again on everything, then update again, etc

"""
train = [
   ('bring the medicine to the patient in room 110'               ,'deliver'),
   ('give these papers to a nurse on floor 3'                     ,'deliver'),
   ('take these papers and bring them back to my office'          ,'deliver'),
   ('bring this tray to room 366'                                 ,'deliver'),
   ('bring these flowers to the front desk on floor 4'            ,'deliver'),
   ('go to the operating room and give the doctor the scissors'   ,'deliver'),
   ('go to the front desk and ask for patient number 45\'s papers','get'),
   ('go to room number 32 and bring back the food trays'          ,'get'),
   ('get me my glasses from my office'                            ,'get'),
   ('bring me the stethoscope from the room next door'            ,'get'),
   ('find Mary and tell her to come here'                         ,'get'),
   ('go get the mop and bucket from the janitor\'s closet'        ,'get'),
   ('take vital signs from the patient in room 132'               ,'get'),
   ('remember this'                                               ,'note'),
   ('okay take a note'                                            ,'note'),
   ('listen up'                                                   ,'note'),
   ('sweep the hallway pleane'                                    ,'clean'),
   ('mop up the blood on the floor'                               ,'clean'),
   ('make all of the beds'                                        ,'clean'),
   ('go to room 341 and mop the floor'                            ,'clean'),
   ('don\'t let anybody else in the door'                         ,'secure'),
   ('make sure all the doors are locked on this floor'            ,'secure'),
   ('stop the people coming from the floor below'                 ,'secure')
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
   ('stop that man from running away'                           ,'secure')
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
plt.savefig("hostpital_test_plot.png")
print "Plot saved as 'hospital_test_plot.png'"