#exercize 5 - more variables and printing things

name = "Sheree Pennah" # my name => Sheree
age = 35 # my age => 35
height = (12 * 5) + 7 # my height in inches => 5 foot 7 inch
weight = 175 # weight in lbs => 175 probably
eyes = "brown" 
teeth = "yellowish"
hair = "brown"

print("Let's talk about %s.") % name
print("She's about %d inches tall.") % height
print("She's about %d lbs heavy") % weight
print("Actually maybe she needs a diet")
print("She's got %s eyse and %s hair") % (eyes, hair)
print("Her teeth are pretty %s depending on the wine") % teeth

# uh oh

print("If I add, %d, %d, and %d I get %d.") % (age, height, weight, age + height + weight)

# the next part of the lesson

print("Age is set to %d as a number but we can use %r to print the string, I THINK") % (age, age)

kilo_to_lbs = 0.453592
weight_in_kilos = weight * kilo_to_lbs 
stone_to_kilos = 6.35029
weight_in_stones = weight_in_kilos / stone_to_kilos

print("Your weight in kilos should be about %d") % weight_in_kilos
print("Your weight in stones should be about %d") % weight_in_stones