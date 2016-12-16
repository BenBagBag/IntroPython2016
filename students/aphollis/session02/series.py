"""Fibonacci series exercises
    this took forever.
    i don't understand the purpose of "assert" or it's syntax.
"""



def fibonacci(n):
    sum_series(n)

def lucas(n):
    sum_series(n, [2, 1])

def sum_series(n, list=[0, 1]):
    """add the last two items in a list, and append their sum. repeat until length = n and return the nth item in the series"""
    next_up = (list[-2]) + (list[-1])

    if len(list) == n:
        return(list[n-1])
    else:
        list.append(next_up)
        sum_series(n, list)


fibonacci(6)
lucas(6)
