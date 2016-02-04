"""
Cameron Fabbri
2/4/2016
config.py
sets up configuration for learning.

You can add anything you want the robot to learn in here, 
just add the functionality in Parser.py

Maybe we can put in some ground truth commands here, then
when the user wants to give a command, it'll analyze and 
classify whether or not it was correct.


Should have these just be json maybe in a file, or in the database.
Database might be too slow. Try both and test times.  But I should
get the exact numbers (not just 0 and 1) and set a threshold.  If
the threshold is passed, then don't ask for user confirmation. If
it isn't passed, asked for confirmation, then learn from it.
	Use cl.accuracy() for that

"""



coffee_train = [
	('go get me some coffee', 1),
	('I need some coffee'   , 1),
	('Go to the other room' , 0),
	('Give this to'         , 0),
	('I want some ice cream', 0)
]


# Greeting training data for intro and outro
greeting_train = [
	('bye',     1),
	('cya',     1),
	('goodbye', 1),
	('exit',    1),
	('hi',      0),
	('hello',   0),
	('hey',     0)
]

