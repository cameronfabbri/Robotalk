"""

Cameron Fabbri
3/24/2016

File to keep all algorithms

"""

from pymongo import MongoClient 
from random import randint

def greet(return_label, command, collection):
   post = {"label":return_label, "command":command}
   collection.insert(post)
   n = collection.find({"label":"greeting"}).count()
   rand_n = randint(0,n)
   random_greeting = collection.find({"label":"greeting"}).limit(1).skip(rand_n)
   for r in random_greeting:
      response = r['command']
   return response

"""
   Function programmable by the robotics researcher for their definition
   of what risk association they want
"""
def getRisk(command):
   return 0

