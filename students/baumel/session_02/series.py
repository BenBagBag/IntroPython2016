def fibonacci(n):
    """This program will return out the Nth value in the Fibonacci series"""
    a, b = 1, 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


def main():
    """This is the main function, it will prompt the
    user for the fib number that they would like then it will provide it to them"""
    n = eval(input("What term # to compute? "))
    print('The {0}th fibonacci number is {1}.'.format(n, fibonacci(n)))


main()
