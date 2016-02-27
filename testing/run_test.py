from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from sklearn.metrics import confusion_matrix
import sys

"""
Cameron Fabbri
2/19/2016

hospital test

This test simulates the case where a robot is to be 
used in a hospital. The classifier is trained on hospital
specific commands

"""
"""

Cameron Fabbri
2/19/2016

personal assistant robot testing

This test simulates the case where a robot is to be a personal
assistant perhaps for an ederly person or someone who is just
lazy and has a lot of money

"""

def run_test(train, test):
   print "Training..."
   cll = NaiveBayesClassifier(train)
   print "Done training\n"
   print "Accuracy: " + str(cll.accuracy(test))

   # get matching lists of predicted and true labels
   pred_labels = list()
   true_labels = list()
   for obj in test:
      prob_label = cll.prob_classify(obj[0]).max()
      true_label = obj[1]
      true_labels.append(true_label)
      pred_labels.append(prob_label)

   # transform our labels to numbers
   labels = cll.labels()
   i = 0
   label_num = dict()
   for label in labels:
      label_num[label] = i
      i = i + 1

   # match our predicted and true labels with the number representations
   true_label_nums = list()
   pred_label_nums = list()
   for true_l, pred_l in zip(true_labels, pred_labels):
      true_label_nums.append(label_num[true_l])
      pred_label_nums.append(label_num[pred_l])

   #print true_label_nums
   #print pred_label_nums
   #print "\n"

   print confusion_matrix(true_label_nums, pred_label_nums)
   print "\n"

if __name__ == '__main__':
   for i in range(1, len(sys.argv)):
      f = sys.argv[i].split(".")[0]
      module = __import__(f)
      name = module.name
      train = module.train
      test = module.test

      print "Testing " + str(name)
      run_test(train, test)