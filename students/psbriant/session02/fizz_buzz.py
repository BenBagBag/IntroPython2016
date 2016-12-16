"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: FIZZBUZZ

Description:
This program iterates through a range of numbers and prints each number. The
string 'Fizz' is printed for all numbers devisible by three. The string 'Buzz'
is printed for all numbers devisible by five. The string 'FizzBuzz' is printed
for all numbers devisible by both three and five.
"""
# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------

# ==============================================================================


def main():
    """
    Iterates through a range of numbers from 1 to 100 inclusive and prints out
    each number unless they are devisible by three or five. For multiples of
    three, the sting 'Fizz' is printed while the string 'Buzz' is printed for
    multiples of five. For numbers that are divisible by both three and five,
    the string 'FizzBuzz' is printed.
    """
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    main()
