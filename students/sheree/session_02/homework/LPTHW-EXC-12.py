#exercise 12 - prompting people 
answer = raw_input("Yes or No? "),
print(answer)

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print("So you are %r old and you are %r tall and you are %r lbs heavy!") % (
	age, height, weight)

