def signcheck(number):
	if number > 0:
		signnum = 'positive'
	elif number == 0:
		signnum = 'zero'
	else:
		signnum = 'negative'
	return signnum

def main():
	number = float(input('Enter number: '))
	sign = signcheck(number)
	print ('Number is ', sign)

main()
