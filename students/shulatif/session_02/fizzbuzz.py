

""" Print every number 1 - 100. But for multiples of 3, print Fizz. For multiples of 5 print Buzz. And for multiples
of 3 AND 5 print FizzBuzz.
"""


def fizzbuzz(n):
    count = 0
    while count <= n:
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")
        else:
            print(count)
        count += 1
fizzbuzz(100)
