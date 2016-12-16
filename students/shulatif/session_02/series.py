def fibonacci(n):
    """
        This will take two numbers in a series and add them together to get the next number, starting with 0 and 1.
        We don't want this to go on for infinity. Using the if/else statements, since it starts at 0 and 1, I just
        used the value of the counter to start off. Then it cycles through adding the numbers to each other and
        raising the counter number to stop the while loop once it reaches the initial Fn.
    """
    count = 0
    fib0, fib1 = 0, 1
    while count < n:
        if count <= 1:
            fibo = count
        else:
            fibo = fib0 + fib1
            fib0 = fib1
            fib1 = fibo
        print(fibo)
        count += 1


def lucas(n):
    """
        This will take two numbers in a series and add them together to get the next number, starting with 2 and 1.
        Using the if/elif statements with a counter, we can tell the assignments to pass the initial assignments and
        then print through additions and raising the counter number to stop the while loop once it reaches the
        initial Fn.
    """
    count = 0
    luc2, luc1 = 2, 1
    while count < n:
        if count == 0:
            lucas = luc2
        elif count == 1:
            lucas = luc1
        else:
            lucas = luc2 + luc1
            luc2 = luc1
            luc1 = lucas
        print(lucas)
        count += 1


def sum_series(y, n=0, x=1):
    """
        This requires one parameter and the other two are optional. The default will produce the fibonacci numbers.
        But if 2 and 1 are used, it will produce the lucas numbers. If all the parameters are used, it will use the
        second and third value as a starting point with the initial parameter for the iterations.
    """
    if not n and not x:
        fibonacci(y)
    elif n == 2 and x == 1:
        lucas(y)
    else:
        count = 0
        while count < y:
            if count == 0:
                randos = n
            elif count == 1:
                randos = x
            else:
                randos = n + x
                n = x
                x = randos
            print(randos)
            count += 1


class TestOfMathFunctions:

    def test_fibonacci(self):
        pass

    def test_lucas(self):
        pass

    def test_sum_series(self):
        pass
