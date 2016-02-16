# smallTalk
smallTalk is a framework for implementing human-robot interaction through natural language. smallTalk is aimed 
towards developers whose focus is primarily towards the actions and functionality of a robot, while still 
needing communication. smallTalk provides bi-directional communication through natural language - sending and 
receiving commands by text or voice. Feedback to the user is provided for risk assesment and learning.
A simple android application is included (soon) to send voice commands.

smallTalk has the ability to learn new commands, as well as expand its vocabulary for already known commands.
A small training set is included in config.py, which can be expanded upon through the process of using
smallTalk. smallTalk uses TextBlob to build a multiclass classifier based on the different commands you need.

## Requirements

smallTalk is written in Python and requires [TextBlob](https://textblob.readthedocs.org/en/dev/) and numpy

1. pip install -U textblob
2. python -m textblob.download_corpora
3. sudo apt-get install python-numpy

## Usage

The first thing to be done is to train the classifier. This can be done by running
`python setup.py`

setup.py uses config.py for the original training data, so edit it to fit your needs.
The classifier has state by pickling it. You have the ability to retrain the classifier, or simply
save another one, and choosing which classifier to use at runtime.

To learn a new command, simply say "new command". You will be prompted to specify a label
for the type of command, and the command itself. It is a good idea when learning a new
command to learn more than just one for the specific label. 

The parser will return the label that it classifies your command. Simply use this label for
the functionality you need. 
