import sockets
import cPickle as pickle
import config

BUFFER_SIZE = config.BUFFER_SIZE

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
   sockets.send("I think this is a %s command" %(str(mpl)))

"""
   Allows the user to input a label and command to better
   train the robot if it is having difficulty understanding

   This can also be used to learn a new command
"""
def train(cll):
   sockets.send("What's the label?")
   label    = sockets.recv(BUFFER_SIZE)
   sockets.send("What's the command?")
   command  = sockets.recv(BUFFER_SIZE)
   new_data = [(command, label)]
   cll.update(new_data)
   f = open(classifier_file, 'wb')
   pickle.dump(cll, f)
   sockets.send("Got it!")

