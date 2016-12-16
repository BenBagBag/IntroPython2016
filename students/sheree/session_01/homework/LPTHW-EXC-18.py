# exercise 18 - names, variables, code, functions - pag 66

def print_two(*args):
	arg1, arg2 = args
	print("arg1: %r, arg2: %r") % (arg1, arg2)
	pass

def print_two_again(arg1, arg2):
	print("arg1: %r, arg2: %r") % (arg1, arg2)
	pass

def print_one(arg1):
	print("arg1: %r") % arg1
	pass

def print_none():
	print("I got nuthin!")
	pass

print_two("Sheree", "Pennah")
print_two_again("Sheree", "Pennah")
print_one("First!")
print_none()

