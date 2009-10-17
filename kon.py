#!/usr/bin/env python
import sys, random

desired_id = 0;

def show_usage():
	print "Usage: " + sys.argv[0] + " [game id]"
	print "\twhere id needs to have a value between 0 and 959;"
	print "\tif id is omitted, a random game will be choosen"
	sys.exit(1)

if len(sys.argv) > 2: # too many arguments?
	show_usage()
elif len(sys.argv) == 2: # id has been supplied by user?
	try:
		desired_id = int(sys.argv[1]);
		if (desired_id < 0) or (desired_id > 959): # check range
			show_usage();
	except ValueError:
		show_usage()
else: # no id supplied, generate number by random
	random.seed()
	desired_id = random.randint(0, 959)

print "yes, desired id is", desired_id

