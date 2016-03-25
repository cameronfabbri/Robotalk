import sockets
import cPickle as pickle
import config

BUFFER_SIZE = config.BUFFER_SIZE

classifier_file = config.classifier_file
"""
   Tests out a command
"""
def test_command(cll):
   sockets.send("What command would you like to test?")
   command = sockets.recv(BUFFER_SIZE)
   labels = cll.labels()
   mpl = labels[0]
   prob_dist = cll.prob_classify(command)
   for label in labels:
      if prob_dist.prob(label) > prob_dist.prob(mpl):
         mpl = label
   per = prob_dist.prob(mpl)
   per = "{0:.4f}".format(per)
   per = int(float(per)*100.0)
   sockets.send("I am %s percent certain this is a %s command" %(str(per), str(mpl)))

"""
   Allows the user to input a label and command to better
   train the robot if it is having difficulty understanding

   This can also be used to learn a new command
"""
def train(cll, collection):
   sockets.send("What's the label?")
   label    = sockets.recv(BUFFER_SIZE)
   sockets.send("What's the command?")
   command  = sockets.recv(BUFFER_SIZE)
   new_data = [(command, label)]
   cll.update(new_data)
   post = {"label":label, "command":command}
   collection.insert(post)
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)
   sockets.send("Got it!")

