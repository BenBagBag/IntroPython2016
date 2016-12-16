# Fibonacci Exercise
# Session02 - Oct. 5, 2016

"""
This is a little chart I made to help me understand how to compute the answer.
Hopefully it helps others.

               f1 + f2 = fn
          f1 + f2 = fn
     f1 + f2 = fn
f1 + f2 = fn
0,   1,   1,   2,   3,   5, ...
"""

def fibonacci(n):
    """ Fibonacci Series Exercise """
    
    if n == 0:
        return 0
    if n == 1:
        return 1

    f1 = 0
    f2 = 1
    
    for i in range(0,n-1):
        fn = f1 + f2
        f1 = f2
        f2 = fn

    return fn

# print("Fibonacci: " + str(fibonacci(3)))


def lucas(n):
    """ 
        Lucas Numbers Exercise 
        Starting numbers sequence: 2, 1, 3, 4, 7, 11, 18, 29, ...
    """

    if n == 0:
        return 2
    if n == 1:
        return 1

    l1 = 2
    l2 = 1
    
    for i in range(0,n-1):
        ln = l1 + l2
        l1 = l2
        l2 = ln

    return ln

# print("Lucas: " + str(lucas(3)))


def sum_series(x, y=0, z=1):
    """
    Optional parameters determine whether Fibonacci or Lucas values will be returned.
    If optional parameters are 0 and 1, return Fibonacci
    If optional parameters are 2 and 1, return Lucas
    """
    if y == 0 and z == 1:
        return fibonacci(x)
        #print("Fibonacci: " + str(fibonacci(x)))
    elif y == 2 and z == 1:
        return lucas(x)
        #print("Lucas: " + str(lucas(x)))
    else:
        return "Optional parameters are not valid."

print(sum_series(15, 0, 1))


# Tests the fibonacci function returns the correct value.
assert fibonacci(25) == 75025

# Tests the lucas function returns the correct value.
assert lucas(25) == 167761

# Tests the sum_series function returns the formula for fibonacci.
assert sum_series(10, 0, 1) == 55

# Tests the sum_series function returns the formula for lucas.
assert sum_series(10, 2, 1) == 123

# Tests the sum_series function returns invalid parameters.
assert sum_series(10, 5, 10) == "Optional parameters are not valid."