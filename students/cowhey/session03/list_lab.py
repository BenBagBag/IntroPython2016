#! /usr/bin/env python3

# Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruits = ["Apples", "Pears", "Oranges", "Peaches"]

# Display the list.
print(fruits)

# Ask the user for another fruit and add it to the end of the list.
fruits.append(input("Add a fruit: "))

# Display the list.
print(fruits)

# Ask the user for a number
# display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
fruit_index = input("Give me a number of a fruit: ")

if int(fruit_index) < len(fruits):
    print(fruits[(int(fruit_index) - 1)])
else:
    print("Not a fruit. Have a marshmallow.")

# Add another fruit to the beginning of the list using “+”
fruits = ["Kiwi"] + fruits
print(fruits)

# Add another fruit to the beginning of the list using insert()
fruits.insert(0, "Pineapple")
print(fruits)

# Display all the fruits that begin with “P”, using a for loop.
for fruit in fruits:
    if fruit[0].lower() == "p":
        print(fruit)

# Display the list.
print(fruits)

# Remove the last fruit from the list.
del fruits[-1]

# Display the list.
print(fruits)

# Ask the user for a fruit to delete and find it and delete it.
delete_fruit = input("Choose a fruit to delete: ")
if delete_fruit in fruits:
    fruits.remove(delete_fruit)
else:
    print("That fruit wasn't there in the first place.")
print(fruits)


# Ask the user for input displaying a line like “Do you like apples?”
# for each fruit in the list (making the fruit all lowercase).
fruits_copy = fruits[:]
for fruit in fruits_copy:
    like = input("Do you like {}?".format(fruit.lower()))
    acceptable_answers = ["yes", "y", "no", "n"]
    # For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values (a while loop is good here):
    while like.lower() not in acceptable_answers:
        like = input("Please give a yes or no answer: ")
    # For each “no”, delete that fruit from the list.
    if like.lower() in acceptable_answers[2:]:
        fruits.remove(fruit)

# Display the list.
print(fruits)

# Make a copy of the list and reverse the letters in each fruit in the copy.
# use copy from above
reversed_fruits = [fruit[::-1] for fruit in fruits_copy]
print(reversed_fruits)

# Delete the last item of the original list. Display the original list and the copy.
del fruits[-1]
print(fruits)
print(fruits_copy)
