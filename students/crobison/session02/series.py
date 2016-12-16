# Charles Robison
# 2016.10.08
# Fibanacci and Lucas series

def fibonacci(n):
    """Return a fibonacci value in relation to n."""
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """Return a lucas value in relation to n."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(x, y=0, z=1):
    """Return a lucas value if optional parameters given as 0 and 1
        else return fibonacci value in relation to x."""
    if y==2 and z==1:
        return lucas(x)
    else:
        return fibonacci(x)


# Test to ensure that functions are working correctly:
assert fibonacci(5-1) + fibonacci(5-2) == 3
assert lucas(5-1) + lucas(5-2) == 7