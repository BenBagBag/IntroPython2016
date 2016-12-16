"""
Write a function that computes the Fibonacci Series
"""

def Fibonacci(n):
    """
    The Fibonacci sequence starts with 0 and 1 and adds them together.
    From there, it adds the result to the previous two integers.
    The sequence is 0, 1, 1, 2, 3, 5, 8, 13..
    The formula is fib(n) = fib(n-2) + fib(n-1)
    """
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else: return Fibonacci(n-2) + Fibonacci(n-1)
