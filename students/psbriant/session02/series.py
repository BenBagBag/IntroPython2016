"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: Fibonacci

Description:

"""
# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------


def fibonacci(n):
    """
    Return the nth value in the Fibonacci series based on integer argument n.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    Return the nth value in the Lucas series based on integer argument n.
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)


def sum_series(n, first=0, second=1):
    """
    Return the nth value in either the Fibonacci series or the Lucas series
    based on the values of integer arguments first and second.
    """
    if n == 0:
        return first
    if n == 1:
        return second
    return sum_series(n-1) + sum_series(n-2)


# ==============================================================================


def main():
    """

    """
    # print(fibonacci(3))
    # print(fibonacci(2))
    # print(fibonacci(0))
    # print(fibonacci(7))
    print(lucas(0))
    print(lucas(1))
    print(lucas(2))
    print(lucas(3))
    print(lucas(4))
    print(lucas(10))


if __name__ == '__main__':
    main()
