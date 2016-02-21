# smallTalk
smallTalk is a framework for implementing human-robot interaction through natural 
language. smallTalk is aimed 
towards developers whose focus is primarily towards the actions and functionality of a 
robot, while still 
needing communication. smallTalk provides bi-directional communication through natural 
language - sending and 
receiving commands by text or voice. Feedback to the user is provided for risk assesment 
and learning.
A simple android application is included (soon) to send voice commands.

smallTalk has the ability to learn new commands, as well as expand its vocabulary for 
already known commands.
A small training set is included in config.py, which can be expanded upon through the 
process of using
smallTalk. smallTalk uses TextBlob to build a multiclass classifier based on the 
different commands you need.

## Requirements

smallTalk is written in Python and requires [TextBlob](https://textblob.readthedocs.org/
en/dev/)

1. pip install -U textblob
2. python -m textblob.download_corpora

## Usage

The first thing to be done is to train the classifier. This can be done by running
`python setup.py`

setup.py uses config.py for the original training data, so edit it to fit your needs.
The classifier is saved to a file by pickling it. You have the ability to re-train the 
classifier, or simply save another one. You can choose which classifier to use in config.
py.

This runs on TCP sockets. Start the server by running `python server.py`.
To connect and start sending and receiving messages run `python connect.py`.

### Built in commands
There are a few built in commands available. You can of course write your own as well. 

`train`

This command allows the user to add more knowledge to the classifier. Simply specify a \
new or existing label (type of command) and a new command. 

`test command`

This command allows you to test what a command will be classified as. This is useful for
testing a new command that may not have a lot of training data yet. This will not update
the classifier in any way, whereas normal commands (if the threshold is passed) will. 

To write your own built in command, simply write the function in `parser.py` and catch 
it in `server.py`

The parser will return the label that it classifies your command. Simply use this label 
for the functionality you need. 
