

def main():
	n=int(input('Pick a size, numbers only: '))
	grid(n)

def grid(n):
	plus='+'
	minus='-'
	bar='|'
	space=' '

	horizontal=plus+minus*n+plus+minus*n+plus+"\n"

	vertical=bar+space*n+ bar +space*n+bar+"\n"

	middle=vertical*n

	print(horizontal+ middle + horizontal + middle + horizontal)

main()



