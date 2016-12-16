#!/usr/bin/python

def parrot_trouble(talking, hour):
	# talking ok hour 7AM to 19PM 
	if talking and (hour < 7 or hour > 20):
		print("True the bird is talking, and it is ", hour, "o clock")
		return True
	else:
		print(talking, "and", hour)
		return False
	
	
parrot_trouble(True, 6)
parrot_trouble(True, 7)
parrot_trouble(False, 6)
parrot_trouble(False, 20)
parrot_trouble(True, 21)