

"""

Cameron Fabbri
3/18/2016

Simple test to show how this can be used with algorithms for robots

"""

import sys
sys.path.insert(0, '/home/pi/projects/smartTalk/src/')

import server

if __name__ == "__main__":
	print "Getting label and risk"
	label, risk = server.get_return()

	print "Label: " + label
	print "Risk: " + risk