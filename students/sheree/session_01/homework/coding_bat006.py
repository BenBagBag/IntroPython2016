'''
Given a string, return a new string where the first and last chars have been exchanged.
'''

def front_back(str):
	first_char = str[0]
	last_char = str[-1]
	string_length = len(str)
	middle_string = str[1:-1]
	if string_length <= 1:
		print(str)
		return str
	result_foo = last_char + middle_string + first_char
	print("RESULT: ", result_foo)
	return result_foo

#def front_back(str):
#	first_char = str[0]
#	last_char = str[-1]
#	string_length = len(str)
#	middle_string = str[1:-2]
#	if string_length <= 1:
#		return str
#	result = last_char + middle_string + first_char
#	return result

front_back("a")
front_back("apple")
front_back("michelle obama")
front_back("shereepena")
front_back("athroughz")
front_back("no scrubs")
front_back("bill clinton")