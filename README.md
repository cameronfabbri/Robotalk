# smartTalk
smartTalk is a framework for implementing human-robot interaction through natural 
language. smartTalk is aimed 
towards developers whose focus is primarily towards the actions and functionality of a 
robot, while still 
needing communication. smartTalk provides bi-directional communication through natural 
language - sending and 
receiving commands by text or voice. Feedback to the user is provided for risk assesment 
and learning.
A simple android application is included (soon) to send voice commands.

smartTalk has the ability to learn new commands, as well as expand its vocabulary for 
already known commands.
A smart training set is included in config.py, which can be expanded upon through the 
process of using
smartTalk. smartTalk uses TextBlob to build a multiclass classifier based on the 
different commands you need.

This research originated from my undergraduate research at Clarkson University. My
research was focused on Intuitive Information Exchange in Human-Robot Dialog. I was
supervised by Dr. Junaed Sattar. I developed several prototypes of a similar application
for use on indoor and outdoor robots operated using speech over Google Glass. This 
framework extends that research.

## Requirements

smartTalk is written in Python and requires [TextBlob](https://textblob.readthedocs.org/
en/dev/)

1. pip install -U textblob
2. python -m textblob.download_corpora

## Usage

The first thing to be done is to train the classifier. This can be done by running
`python setup.py`

`setup.py` uses `config.py` for the original training data, so edit it to fit your needs.
The classifier is saved to a file by pickling it. You have the ability to re-train the 
classifier, or simply save another one. You can choose which classifier to use in `config.py.`

This runs on TCP sockets. Start the server by running `python server.py`.
To connect and start sending and receiving messages run `python connect.py`.

#### Built in commands
There are a few built in commands available. You can of course write your own as well. 

`train`

This command allows the user to add more knowledge to the classifier. Simply specify a
new or existing label (type of command) and a new command. 

`test command`

This command allows you to test what a command will be classified as. This is useful for
testing a new command that may not have a lot of training data yet. This will not update
the classifier in any way, whereas normal commands (if the threshold is passed) will. 

To write your own built in command, simply write the function in `parser.py` and catch 
it in `server.py`

### Usage in robotics

To use this framework in controlling robots, you will need to implement your own `connect
.py`. The hook exists in linking the return label to your functions. The parser will 
return to `connect.py` an array containing `[command, label, risk]`. All that needs to 
be done on the developers end is to trigger an action based on the return label (and 
associated risk). The command is returned as well in case the user wants to do any more 
NLP with it.
