__author__ = 'panderson'

n=1


def fibonacci(n):

	first = 0
	last = 1
	i=3

	while i<=n:
		if n==1:
			print (n,0)
			return
		elif n==2:
			print (n,1)
			return
		else:
			pass		
		fib = first+last
		first = last
		last = fib
		i+=1
	return fib

def lucas(n):
	first = 2
	last = 1
	i=3
	if n==1:
		return first
	elif n==2:
		return last
	else:
		while i<=n:
			lucas = first+last
			first, last = last, lucas
			i+=1
		return lucas



#fibonacci(n)
print ('the lucas number for %s is:' % (n))
print (lucas(n))
print ('finished')	

	
		

