# Function that accepts 2 variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# Takes the cheese_count variable and places it within a string
    print("You have %d cheeses!" % cheese_count)
# Takes the box_of_crackers variable and places it within a string
    print("You have %d boxes of crackers!" % boxes_of_crackers)
# Print a string to the console
    print("Man that's enough for a party!")
# Prints a string to the console and adding a carriage return at the end
    print("Get a blanket.\n")

# Prints a string to the console
print("We can just give the function numbers directly:")
# Calls a function and passes 2 variables
cheese_and_crackers(20, 30)

# Prints a string to the console
print("OR, we can use variables from our script:")
# Assigns a value to a variable
amount_of_cheese = 10
# Assigns a value to a variable
amount_of_crackers = 50
# Calls a function and passes the previous to variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Prints a string to the console
print("We can even do math inside too:")
# Calls a function and passes 2 variables with addition
cheese_and_crackers(10 + 20, 5 + 6)

# Prints a string to the console
print("And we can combine the two, variables and math:")
# Calls a function, adds variables to values
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print()

import random

def car_truck(car, truck):
    print("There are %d cars and %d trucks in the lot." % (car, truck))
#1
car_truck(5, 12)
#2
car_truck(12+5, 4+7)
#3
car = 6
truck = 34
car_truck(car, truck)
#4
result = car_truck(7, 6)
#5
car_truck(car+12, truck-4)
#6
car = 0
truck = 0
car = int(input("How many cars? "))
truck = int(input("How many trucks? "))
car_truck(car, truck)
#7
def rand_car_truck():
    car = random.randrange(1,51)
    truck = random.randrange(1,51)
    car_truck(car, truck)
rand_car_truck()
#8

