i = 0 
numbers = []

def query():
	goal = int(raw_input("Give me an integer for building the list "))
	return goal
	pass

def add_amount():
	increment_by = int(raw_input("How much should we increment by? "))
	return increment_by
	pass

def list_build_and_print(i, numbers):
	goal = query()
	increment_by = add_amount()
	while i < goal:
		print(">>>>>At the top, i is %d") % i 
		numbers.append(i)

		i = i + increment_by 
		print("Numbers now: "), numbers 
		print(" At the bottom i is %d<<<<<") % i

list_build_and_print(i, numbers)

print("The numbers: ")

for num in numbers:
	print num
