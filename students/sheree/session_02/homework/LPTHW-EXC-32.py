the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#this for loop goes through a list

for number in the_count:
	print("this is the count %d") % number
	pass

for fruit in fruits:
	print("a fruit of type %s") % fruit
	pass

#mixed lists

for i in change:
	print("I got %r") % i

elements = []

for i in range(0,6):
	print("Adding %d to the list") % i
	#append is a function that lists understand
	elements.append(i)

# now we can print them out too

for i in elements:
	print("Element was: %d") % i
	pass