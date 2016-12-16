'''Write a program that prints the numbers from 1 to 100 inclusive.
But for multiples of three print "Fizz" instead of the number
For the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz"
instead.'''


def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)


# bonus round
def custom_fizzbuzz(start, finish):
    '''Do fizzbuzz for any range you like!
    Including negatives!'''
    if start > finish:
        step = -1
        if finish < 0:
            finish_index = finish - 1
        else:
            finish_index = finish
    else:
        step = 1
        finish_index = finish + 1
    for x in range(start, finish_index, step):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
