#this program counts from 1 to 100 and prints phrases if the number
#is multiple of specific numbers.
for i in range(1,101,1):
	if i % 3 == 0:
		print ('Fizz')
	elif i % 5 == 0:
		print ('Buzz')
	elif i % 3  == 0 and  i % 5 == 0:
		print ('FizzBuzz')

	else:
		print (i)
