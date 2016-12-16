# boolean practice, exc 28, page 96

def query():
	tf = input("Will This Evalate to True? ")
	guess = tf
	return guess
	pass

def guesses(guess, result):
#	print "Your recorded answer was:\n ", guess, "\n",
	if guess == result:
		print "CORRECT, this evaluates to:", result, "\n"
	else:
		print "UH-OH, this evaluates to:", result, "\n"
	pass

def function01():
	print("\nPlease evaluate the following:\n\n\tTrue and True\n")
	# query()
	result = True and True
	guess = query()
	guesses(guess, result)
#	print "Function 1 evaluates to:", result, "\n"
	pass

function01()

#def function02():
#	print("Please evaluate the following:\n\tFalse and True")
#	result = False and True
#	guess = query()
#	guesses(guess, result)
#	print "Function 2 evaluates to:", result, "\n"
#	pass
#
#function02()
#
#def function03():
#	print "Please evaluate the following:\n\t1 == 1 and 2 == 1"
#	result = 1 == 1 and 2 == 1
#	guess = query()
#	guesses(guess, result)
#	print "Function 3 evaluates to:", result, "\n"
#	pass
#
#function03()
#
#def function04():
#	print "Please evaluate the following:\n\t\"test\" == \"test\""
#	result = "test" == "test"
#	guess = query()
#	guesses(guess, result)
#	print "Function 4 evaluates to:", result, "\n"
#	pass
#
#function04()
#
#def function05():
#	print "Please evaluate the following: \n\t1 == 1 or 2 != 1"
#	result = 1 == 1 or 2 != 1
#	guess = query()
#	guesses(guess, result)
#	print "Function 5 evaluates to:", result, "\n"
#	pass
#
#function05()
#
#def function06():
#	print "Please evaluate the following: True and 1 == 1"
#	result = True and 1 == 1
#	guess = query()
#	guesses(guess, result)
#	print "Function 6 evaluates to:", result, "\n"
#	pass
#
#function06()
#
#def function07():
#	print "Please evaluate the following: False and 0 != 0"
#	result = False and 0 != 0
#	guess = query()
#	guesses(guess, result)
#	print "Function 7 evaluates to:", result, "\n"
#	pass
#
#function07()
#
#def function08():
#	print "Please evaluate the following: True or 1 == 1"
#	result = True or 1 == 1
#	guess = query()
#	guesses(guess, result)
#	print "Function 8 evaluates to:", result, "\n"
#	pass
#
#function08()
#
#def function09():
#	print "Please evaluate the following: \"test\" == \"testing\""
#	result = "test" == "testing"
#	guess = query()
#	guesses(guess, result)
#	print "Function 9 evaluates to:", result, "\n"
#	pass
#
#function09()
#
#def function10():
#	print "Please evaluate the following: 1 != 0 and 2 == 1"
#	result = 1 != 0 and 2 == 1
#	guess = query()
#	guesses(guess, result)
#	print "Function 10 evaluates to:", result, "\n"
#	pass
#
#function10()
#
#def function11():
#	print "Please evaluate the following: \"test\" != \"testing\""
#	result = "test" != "testing"
#	guess = query()
#	guesses(guess, result)
#	print "Function 11 evaluates to:", result, "\n"
#	pass
#
#function11()
#
#def function12():
#	print "Please evaluate the following: \"test\" == 1"
#	result = "test" == 1
#	guess = query()
#	guesses(guess, result)
#	print "Function 12 evaluates to:", result, "\n"
#	pass
#
#function12()
#
#def function13():
#	print "Please evaluate the following: not (True and False)"
#	result = not (True and False)
#	guess = query()
#	guesses(guess, result)
#	print "Function 13 evaluates to:", result, "\n"
#	pass
#
#function13()
#
#def function14():
#	print "Please evaluate the following: not (1 == 1 and 0 != 1)"
#	result = not (1 == 1 and 0 != 1)
#	guess = query()
#	guesses(guess, result)
#	print "Function 14 evaluates to:", result, "\n"
#	pass
#
#function14()
#
#def function15():
#	print "Please evaluate the following: not (10 == 1 or 1000 == 1000)"
#	result = not (10 == 1 or 1000 == 1000)
#	guess = query()
#	guesses(guess, result)
#	print ">>>Function 15 evaluated to:", result, "\n__________"
#	pass
#
#function15()
#
#def function16():
#	print "Please evaluate the following: not (1 != 10 or 3 == 4)"
#	result = not (1 != 10 or 3 == 4)
#	guess = query()
#	guesses(guess, result)
#	print ">>>Function 16 evaluated to:", result, "\n__________"
#	pass
#
#function16()
#
#
#def function17():
#	print "Please evaluate the following: not (\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\")"
#	result = not ("testing" == "testing" and "Zed" == "Cool Guy")
#	guess = query()
#	guesses(guess, result)
#	print ">>>Function 17 evaluated to:", result, "\n__________"
#	pass
#
#function17()
#
#
#def function18():
#	print "Please evaluate the following: 1 == 1 and not (\"testing\" == 1 or 1 == 0)"
#	result = 1 == 1 and not ("testing" == 1 or 1 == 0)
#	guess = query()
#	guesses(guess, result)
#	print ">>>Function 18 evaluated to:", result, "\n__________"
#	pass
#
#function18()
#
#def function19():
#	print "Please evaluate the following: \"chunky\" == \"bacon\" and not (3 == 4 or 3 == 3)"
#	result = "chunky" == "bacon" and not (3 == 4 or 3 == 3)
#	guess = query()
#	guesses(guess, result)
#	print ">>>Function 19 evaluated to:", result, "\n__________"
#	pass
#
#function19()
#
#def function20():
#	print "Please evaluate the following: 3 == 3 and not (\"testing\" == \"testing\" or \"Python\" == \"Fun\")"
#	result = 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
#	guess = query()
#	guesses(guess, result)
#	print ">>>Function 20 evaluated to:", result, "\n__________"
#	pass
#
#function20()
#

