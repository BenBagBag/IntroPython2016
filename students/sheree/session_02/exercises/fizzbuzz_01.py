# scratchpad

testone = 1
testtwo = 2
testthree = 3
testfour = 4
testfive = 5
testfifteen = 15
testthirty = 30
testthirtyone = 31

def test_modulo(num):
	if num % 3 == 0 or num % 5 == 0:
		if num % 3 == 0 and not num % 5 == 0:
			print("fizz")
		elif num % 3 == 0 and num % 5 == 0:
			print("fizzbuzz")
		elif num % 3 != 0 and num % 5 == 0:
			print("buzz")
		else:
			print(num)
	else:
		print(num)

test_modulo(testone)
test_modulo(testtwo)
test_modulo(testthree)
test_modulo(testfour)
test_modulo(testfive)
test_modulo(testfifteen)
test_modulo(testthirty)
test_modulo(testthirtyone)
