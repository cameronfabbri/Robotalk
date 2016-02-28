from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from sklearn.metrics import confusion_matrix
import sys

"""

Cameron Fabbri
2/19/2016

General testing file. This takes in one or more python files
containing a test name, training set, and testing set. This 
computes their accuracy and confusion matrix and writes the 
output to a file.

"""

def run_test(train, test, name):
   print "Training..."
   cll = NaiveBayesClassifier(train)
   print "Done training\n"
   accuracy = cll.accuracy(test)
   print "Accuracy: " + str(accuracy)

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

   cm = confusion_matrix(true_label_nums, pred_label_nums)
   print cm
   print "\n"

   with open("test_results.txt", "a") as tr:
      tr.write(str(name) + "\n")
      tr.write(str(accuracy) + "\n")
      tr.write(str(cm))
      tr.write("\n\n")

   plt.imwrite("file.png", conf, cmap='binary', interploation='None')

   #import matplotlib as mpl
   #mpl.use('Agg')
   #import matplotlib.pyplot as plt
   #fig = plt.figure(cm, cmap='binary', interpolation='None')
   #fig.savefig("butler.png")

if __name__ == '__main__':
   with open("test_results.txt", "w") as tr:
      tr.write("")
      tr.close()
   for i in range(1, len(sys.argv)):
      f = sys.argv[i].split(".")[0]
      module = __import__(f)
      name   = module.name
      train  = module.train
      test   = module.test

      print "Testing " + str(name)
      run_test(train, test, name)
