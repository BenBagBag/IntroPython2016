"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: Fibonacci

Description:
This program run methods for the fibonacci series, the lucas series and a
general method that simulates either based on specified input.
"""

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
    return sum_series(n-1, first, second) + sum_series(n-2, first, second)


# ==============================================================================


def main():
    """
    Tests each method to verify specified parameters return expected output.
    """

    # Tests for fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(6) == 8
    # Tests for lucas
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(6) == 18
    # Tests for sum_series with default values for first and second
    assert sum_series(0) == 0
    assert sum_series(1) == 1
    assert sum_series(2) == 1
    assert sum_series(6) == 8
    # Tests for sum_series with non default values for first and second
    assert sum_series(0, 2, 1) == 2
    assert sum_series(1, 2, 1) == 1
    assert sum_series(2, 2, 1) == 3
    assert sum_series(6, 2, 1) == 18

if __name__ == '__main__':
    main()
