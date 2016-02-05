"""
Cameron Fabbri
2/4/2016
config.py
sets up configuration for learning.

You can add anything you want the robot to learn in here, 
just add the functionality in Parser.py

Supports multiclassification

"""

# The number of labels you have
num_labels = 3

train = [
   ('hey', 0),
   ('hello', 0),
   ('hi', 0),
   ('what\'s up', 0),
   ('yo', 0),
   ('how\'s it going?', 0),
   ('what\'s new?', 0),
   ('hey how is your day', 0),
   ('good morning', 0),
   ('good evening', 0),
   ('howdy', 0),
   ('good night', 1),
   ('cya', 1),
   ('goodbye', 1),
   ('bye', 1),
   ('later', 1),
   ('have a good day', 1),
   ('farewell', 1),
   ('take care', 1),
   ('bye bye', 1),
   ('see you later', 1),
   ('have a good one', 1),
   ('so long', 1),
   ('i\'m out', 1),
   ('bring me some', 2),
   ('go get me some', 2),
   ('i\'d like you to bring me', 2),
   ('get me', 2),
   ('i want my', 2),
   ('please get me', 2),
   ('i need', 2)
]

