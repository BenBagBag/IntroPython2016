""""Oct 9th, 2016: Class 2: Fibonacci Series exercise."""


# Fibonacci series


def fib(n):
    """Return the nth value in the fibonacci series."""
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        result = fib(n - 1) + fib(n - 2)
        return result
    # print("The ", n, "th value in the fibonacci series is:", result)


# Lucas series


def lucas(n):
    """Return the nth value in Lucas series."""
    if (n == 0):
        return 2
    elif (n == 1):
        return 1
    else:
        result = lucas(n - 1) + lucas(n - 2)
        return result
    # print("result = ", result)


# def other(n, x, y):
#     """Return the value in any other series."""
#     def sub_other(n):
#         if (n == 0):
#             return x
#         elif (n == 1):
#             return y
#         else:
#             result = sub_other(n - 1) + sub_other(n - 2)
#             return result


def other(n):
    """Return the value in series starting with 3, 2."""
    # TODO: Calculate the Fibonacci series for any given first two numbers.
    if (n == 0):
        return 3
    elif (n == 1):
        return 2
    else:
        result = other(n - 1) + other(n - 2)
        return result


def sum_series(n, x=0, y=1):
    """Print Lucas series or Fibonacci series or other based on input."""
    if (x == 2 and y == 1):
        result = lucas(n)
        return result
        print("The ", n, "th value in the Lucas series is:", result)
    elif (x == 0 and y == 1):
        result = fib(n)
        return result
        print("The ", n, "th value in the Fibonacci series is:", result)
    else:
        if (n == 0):
            return x
        elif (n == 1):
            return y
        else:
            result = other(n)
            return result
        print("Not a fibonacci or Lucas series!")

# verifying fibonacci series
assert fib(6) == 8
assert fib(8) == 21
# verifying lucas series
assert lucas(6) == 18
assert lucas(8) == 47
# verifying either fibonacci or lucas series
assert sum_series(6) == 8
assert sum_series(6, 2, 1) == 18
assert sum_series(0, 3, 2) == 3
assert sum_series(6, 3, 2) == 31
# *******************************************************
# *******************End of Program**********************
