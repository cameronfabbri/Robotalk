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

confidence_threshold = 0.75

built_in = [
   ('new command'),
   ('goodbye')
]

train = [
   ('hello how are you today', 'greeting'),
   ('what\'s up', 'greeting'),
   ('how\'s it going?', 'greeting'),
   ('hey how is your day', 'greeting'),
   ('good morning', 'greeting'),
   ('good night', 'exit'),
   ('i\'m going home', 'exit'),
   ('have a good day', 'exit'),
   ('see you later', 'exit'),
   ('go and get me some coffee', 'get'),
   ('go and get me a pencil', 'get'),
   ('go to the break room and get my coffee', 'get'),
   ('go down the hall and deliver this to the mail room', 'deliver'),
   ('go to my office and drop off this paper', 'deliver'),
   ('bring this cup of coffee down the hall to my office', 'deliver'),
   ('bring this letter to the mail room down the hall', 'deliver'),
   ('deliver this letter to room 365', 'deliver'),
   ('go over to the break room', 'go'),
   ('go down the hall', 'go'),
   ('go into the room next door', 'go')
]
