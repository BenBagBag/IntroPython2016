#! /usr/bin/env python3

# from http://www.upriss.org.uk/python/session5.html

# Create a list that contains the names of 5 students of this class.
student_list = ["Bob Smith", "Patty Joe", "Harry Potter", "Joe Schmoe", "George Foreman"]
print(student_list)
# Ask the user to input one more name and append it to the list.
student_list.append(input("Give me one more name to add: "))
print(student_list)
# Ask a user to input a number. Print the name that has that number as index.
student_index = input("Give me an index on the list: ")
if int(student_index) < len(student_list):
    print(student_list[int(student_index)])
else:
    print("Pay more attention next time, that student doesn't exist.")
# Add "John Smith" and "Mary Miller" at the beginning of the list (by using "+")
student_list = ["John Smith", "Mary Miller"] + student_list
print(student_list)
# Remove the last name from the list.
student_list.pop()
print(student_list)
# Ask a user to type a name.
remove_student = input("Give me a name on the list.")
standardized_names = [name.lower() for name in student_list]
# Check whether that name is in the list: if it is then delete it from the list.
if remove_student.lower() in standardized_names:
    student_index = standardized_names.index(remove_student.lower())
    student_list.pop(student_index)
# Otherwise add it at the end.
else:
    student_list.append(remove_student)
# Create a copy of the list in reverse order.
reversed_students = student_list[::-1]
print(reversed_students)
print(student_list)


# Create a for loop that prints for each student "hello student_name, how are you?"
for name in student_list:
    print("Hello {}, how are you?".format(name))

# alice.txt
file = open("alice.txt", "r")
text = file.readlines()

# Modify the program so that the lines are printed in reverse order.
for line in text[::-1]:
    print(line)

# Output to another file instead of the screen.
with open('alice_copy.txt', 'w') as new_file:
    new_file.writelines(text)
new_file.close()

# change the script so that it appends the output to an existing file
with open("alice_copy.txt", "a") as new_file:
    new_file.writelines(text)
new_file.close()

new_file = open("alice_copy.txt", "w")
for x in range len(text):
    new_file.write(str(x + 1) + ": " + text[x])
new_file.close()
