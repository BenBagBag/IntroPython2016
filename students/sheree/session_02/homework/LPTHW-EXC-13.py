#!/usr/local/bin/python 
#exercise 13 - parameters, unpacking, variables

"""
	LPTHW-EXC-13.py: working file for the Learn Python The Hard Way Exc # 3
"""

__author__	= "Sheree Pennah"

from sys import argv



print "Hello this is argument variable 1: ",
variable1 = raw_input()

print "Hello this is argument variable 2: ",
variable2 = raw_input()

print "Hello this is argument variable 3: ",
variable3 = raw_input()

script, variable1, variable2, variable3 = argv

print "the script is called:", script
print "your first variable is:", variable1
print "your second variable is:", variable2
print "your third variable is:", variable3

#i thought this might work but it did not