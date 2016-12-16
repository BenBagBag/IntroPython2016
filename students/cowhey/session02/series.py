def fibonacci(n):
    '''return the nth value in a Fibonacci sequence, where n is zero-indexed'''
    if n < 0:
        return "No, look, Fibonacci numbers don't go into negatives. Stop being an asshole."
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


def lucas(n):
    '''return the nth value in a Lucas sequence, where n is zero-indexed'''
    if n < 0:
        return "Nope."
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 2) + lucas(n - 1)


def sum_series(n, first=0, second=1):
    '''Return the nth value in a series.
    Defaults to returning the Fibonacci number.
    first = first value in the sequence
    second = second value in the sequence'''
    if n < 0:
        return "Nope."
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 2, first, second) + sum_series(n - 1, first, second)

# --------------------------------- #
# test the series functions
# should exit without error if everything is okay

# test the fibonacci function
assert fibonacci(3) == 2

# test the lucas function
assert lucas(5) == 11

# test the sum_series function works for fibonacci sequences (default)
assert sum_series(3) == 2

# test the sum_series function works for lucas sequences
assert sum_series(3, 2, 1) == 4
