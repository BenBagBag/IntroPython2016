def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b


print ("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 3))))

print("That becomes: ", what, "Can you do it by hand?")

#1
def box1_box2(a, b):
    print("We have %d widgets in box 1 and %d widgets in box 2." % (a, b))
    return a + b

total_widgets = box1_box2(5, 7)
print("There are %d wigets total." % (total_widgets))

#2
def long_answer(num):
    answer = (35 + (74 - (180 * (50 / num))))
    print(answer)
long_answer(3)

#3
# Changed the starting value from 2 to 3. Returned the same value for both formula's.

#4 - Fahrenheit to Celsius
simp_answer = (10 - 32) * 5 / 9
print(simp_answer)

def F_to_C(num):
    answer = (num - 32) * 5 / 9
    print(answer)
F_to_C(10)




