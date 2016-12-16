__author__ = 'panderson'

i = 1
fizz = 'fizz'
buzz = 'buzz'
linout = ''

def is3(i):
	if i%3 == 0:
		return True
	else:
		return False	

def is5(i):
	if i%5 == 0:
		return True
	else:
		return False	


while i<=100:
	if is3(i):
		linout = fizz
	else:
		pass
		
	if is5(i):
		linout = linout+buzz
	else:
		pass
	
	if linout == '':
		print (i)
	else:
		print (linout)
	linout=''	

	i+=1	

print ('finished')	

	
		

