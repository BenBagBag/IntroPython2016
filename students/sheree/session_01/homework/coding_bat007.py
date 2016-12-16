'''
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
'''

def front3(str):
	if len(str) < 3:
		#print(str)
		return str
	new_string = str[0:3] * 3
	#print(new_string)
	return new_string
	

front3('Java') 
front3('Chocolate') 
front3('abc') 
front3('aa') 
front3('az') 
front3('a') 
front3('a') 