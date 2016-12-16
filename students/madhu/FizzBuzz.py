def number():
   for i in range(1,101):
       mod3 = i % 3
       mod5 = i % 5
       mod15 = i % 15

       if mod3 == 0 and mod15 != 0:
           print ("Fizz")
       elif mod5 == 0 and mod15 != 0:
           print ("Buzz")
       elif mod15 == 0:
           print ("FizzBuzz")
       else:
           print i


if __name__ == "__main__":
    number()

