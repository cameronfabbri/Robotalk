"""
Cameron Fabbri
2/4/2016
config.py
sets up configuration for learning.

You can add anything you want the robot to learn in here, 
just add the functionality in Parser.py

Supports multiclassification

"""
confidence_threshold = 0.85
try:
   classifier_file = "classifier.pickle"
except:
   print "No classifier found. run `setup.py` and enter the classifier filename in config.py"
   exit()

TCP_IP = '127.0.0.1'
TCP_PORT = 5556
BUFFER_SIZE = 1024

built_in = ['test command', 'train', '']

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
   ('can you grab my glasses for me?', 'get'),
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
