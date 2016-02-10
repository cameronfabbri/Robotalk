"""
Cameron Fabbri
2/4/2016
config.py
sets up configuration for learning.

You can add anything you want the robot to learn in here, 
just add the functionality in Parser.py

Supports multiclassification

"""

entrance_label = 0
exit_label     = 1
learn_label    = 2

confidence_threshold = 0.85

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
   ('i want to teach you something', 2),
   ('time to learn', 2),
   ('want to learn something new?', 2),
   ('new command', 2),
   ('learn new command', 2),
   ('new command to learn', 2)

]

