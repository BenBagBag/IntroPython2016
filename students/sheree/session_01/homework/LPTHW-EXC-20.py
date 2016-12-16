# exercise 20 - functions and files - page 74
# importing the argv from the system
from sys import argv
#  setting a input_file var for the arg
script, input_file = argv
# func to print the read file - i think? F stands for file, we are reading the file?
def print_all(f):
	# print(f.read()) 
	print f.read()
	pass
# func to seek set to 0 which is the absolute position, 1 means relative, 2 means the end
def rewind(f):
	f.seek(0)
	pass
#  func that prints the linecount of the file from the readline???? 
def print_a_line(line_count, f):
	# print(line_count, f.readline())
	print line_count, f.readline()
	pass

# we are setting the file to the file we will input in the arg
current_file = open(input_file)
#  we are letting the user know we are about to print the whole file using the print all func
print("First, let us print the whole file:\n")
#  we call the print all func using the current file which is passed via the argv
print_all(current_file)
#  we are letting the user know that we are about to do the rewind func, whatever that is
print("Now let us rewind, kind of like a tape.")
#  we call the rewind func with the current file we got from the argv
rewind(current_file)
# user info to explain what we're doing next
print("Let's print three lines:")
# set a new var to track the line we are on
# call the print a line function with the current line arg and the current file arg 
# the print a line func prints the read line count that the file read from the readline
current_line = 1
print_a_line(current_line, current_file)
# set current line var to plus 1, as a next nav
#  call the print a line with our new current line state
#  the func prints to the stdout
current_line += 1
print_a_line(current_line, current_file)
# this does the same things but navigates to the next line
current_line += 1
print_a_line(current_line, current_file)

