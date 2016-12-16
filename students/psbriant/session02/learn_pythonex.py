"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
Exercises: Learn Python the Hard Way problems 11-14, 18, 19, 21, 28-33

Description:
Answers to exercises from Learn Python the Hard Way.
"""
# -------------------------------Import-----------------------------------------
from sys import argv
# -------------------------------Functions--------------------------------------


def exercise_11():
    """
    Answer for exercise 11.
    """
    print("How old are you?"),
    age = input()
    print("How tall are you?"),
    height = input()
    print("How much do you weigh?"),
    weight = input()

    print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))


def exercise_12():
    """
    Answer for exercise 12.
    """
    age = input("How old are you? ")
    height = input("How tall are you? ")
    weight = input("How much do you weigh? ")

    print("So, you're %r old, %r tall and %r heavy.") % (age, height, weight)


def exercise_13():
    """

    """
    script, first, second, third = argv

    print("The script is called:", script)
    print("Your first variable is:", first)
    print("Your second variable is:", second)
    print("Your third variable is:", third)

# ==============================================================================


def main():
    """
    Test each method to verify specified parameters return expected output.
    """
    exercise_11()
    exercise_12()

if __name__ == '__main__':
    main()
