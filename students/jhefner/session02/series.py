"""
fibonacci series
"""

def fibonacci(n):
    """This function returns the nth value in the fibonacci series,
     derived from the functions input variable."""
    if n<=1:
        print(n)
    else:
        fib = (n-2)+(n-1)
        print(fib)

def lucas(n):
    if n==0:
        print(int(2))
    elif n==1:
        print(int(1))
    else:
        luc = (n-1)+(n-2)
        print(luc)

def sum_series(x, y=0, z=1):
    print(":(")


fibonacci(5)
lucas(5)
sum_series(5)

a=1
b=2
c=3

assert a+b==c, "a+b equals c"
print(locals())
print(__file__)