'''Fibonacci Series Exercise
Goal:
The Fibonacci Series is a numeric series starting with the integers 0 and 1.

In this series, the next integer is determined by summing the previous two.

This gives us:

0, 1, 1, 2, 3, 5, 8, 13, ...
We will write a function that computes this series – then generalize it.'''


def fibonacci(n):
    '''Compute Fibonacci series to nth value and return'''
    fib1 = 0
    fib2 = 1
    for x in range(0, n):
        fibn = fib1+fib2
        fib1 = fib2
        fib2 = fibn
    return fibn


def lucas(n):
    '''Compute Lucas series to nth value and return'''
    luc1 = 2
    luc2 = 1
    for x in range(0, n):
        lucn = luc1+luc2
        luc1 = luc2
        luc2 = lucn
    return lucn


def sum_series(n, s1=0, s2=1):
    '''Compute series to nth value and return

    By default computes Fibonacci series

    Keyword arguments:
    n -- how far in the series to compute
    s1 -- series first starting value (default 0)
    s2 -- series second starting value (default 1)'''

    ser1 = s1
    ser2 = s2
    for x in range(0, n):
        sern = ser1+ser2
        ser1 = ser2
        ser2 = sern
    return sern

# Check fibonacci function (6th value in fib series is 13)
assert fibonacci(6) == 13
# Check lucas function (6th value in luc series is 29)
assert lucas(6) == 29

# Check sum_series func (6th val in fib series=13, 6th val in luc series=29)
assert sum_series(6) == 13
assert sum_series(6, 2, 1) == 29
