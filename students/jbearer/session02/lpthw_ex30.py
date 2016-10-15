people = 20
cars = 10
trucks = 25

# Check to see if cars are greater than people
if cars > people:
# If True, prints statement
    print ("We should take the cars.")
# Check to see if car is less than people or trucks is greater than cars
elif cars < people or trucks > cars:
# If True, prints statement
    print ("We should not take the cars.")
# If False runs the following block of code
else:
# Prints to the screen
    print ("We can't decide.")
# Check to see if trucks is greater than cars
if trucks > cars:
# If True, prints statement
    print ("That's too many trucks.")
# If first conditional is False, test if trucks are less than cars and people are greater than trucks
elif trucks < cars and people > trucks:
# If True, prints statement
    print ("Maybe we could take the trucks.")
# Executes if previous conditions are False
else:
# Prints to the screen
    print ("We still can't decide.")
# Checks if people is greater than trucks
if people > trucks:
# If True, prints statement to screen
    print ("Alright, let's just take the trucks.")
# If False
else:
# Prints statement to the screen
    print ("Fine, let's stay home then.")

"""
#1: If one condition is not True it tests for another
    condition.

#2: Completed

#3: Completed

#4: Completed