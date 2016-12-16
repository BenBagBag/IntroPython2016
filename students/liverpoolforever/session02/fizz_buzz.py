"""
This file prints the fizz buzz pattern
"""

# Declare the constants
FIZZ = "FIZZ"
BUZZ = "BUZZ"
ITERATIONS = 21

for i in range(1,ITERATIONS):
    if i % 3 == 0 and i % 5 == 0 :
        print(FIZZ,BUZZ)
    elif i % 5 == 0:
        print(BUZZ)
    elif i % 3 == 0:
        print(FIZZ)
    else:
        print(i)
