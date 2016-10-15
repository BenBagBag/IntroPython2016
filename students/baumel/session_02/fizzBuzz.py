def fizzbuzz():
    """ Write a program that prints the numbers from 1 to 100 inclusive.
        But for multiples of three print “Fizz” instead of the number
        For the multiples of five print “Buzz”.
        For numbers which are multiples of both three and five print “FizzBuzz” instead"""

    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
            x += 1
        elif x % 3 == 0:
            print('Fizz')
            x += 1
        elif x % 5 == 0:
            print('Buzz')
            x += 1
        else:
            print(x)
            x += 1


fizzbuzz()
