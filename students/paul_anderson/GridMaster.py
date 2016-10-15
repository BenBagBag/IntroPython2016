__author__ = 'panderson'
plus = '+'
minus = '-'
bang = '|'
space = '    '
grid = 2
wgrid = grid
grid_counter = 1
linout = ''

def border():
	linout = (plus+minus*4)
	return linout 

def filler():
	linout = (bang+space)
	return linout

def fifth(n):
	if n%5 == 0:
		return True
	else: 
		return False	



while (grid_counter <= grid):
	i=0
	while i<=4:
		if fifth(i):
			linout = border()*wgrid+plus
		else:
			linout = filler()*wgrid+bang
		print (linout)
		i = i+1
	grid_counter+=1
linout = border()*wgrid+plus
print (linout)	
		


print ('finished')	

	
		

