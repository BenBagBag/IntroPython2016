"""
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
"""

def not_string(str):
	prepended_text = "not"
	if len(str) >= 3 and str[0:3] == prepended_text:
		new_string = str
		print(new_string)
		return new_string
	else:
		new_string = prepended_text + " " + str
		print(new_string)
		return new_string




not_string('candy') # 'not candy'
not_string('x') # 'not x'
not_string('not bad') # 'not bad'
not_string('not') # 'not bad'
not_string('candyland')
not_string('notwithstanding')
not_string('note takers')
not_string('not bad bro') 
not_string("I don't understand this yet")