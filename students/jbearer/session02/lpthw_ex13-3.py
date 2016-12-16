from sys import argv

script, name, age = argv

print("The script is called:", script)
print("Your first name is:", name)
print("Your age is:", age)
weight = input("Weight: ")
height = input("Height: ")
print("Weight: %r \n Height: %r " % (weight, height))