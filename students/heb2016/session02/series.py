
## Session02 Exercise 
# fibonacci 
def fibonacci(n):
		row=0
		while row<=n:
			if row==0:
				nth1=row
				nth2=0
				nth=nth1+nth2
				if n==0:
					print(row, "number", nth)
					return(nth)
				row+=1
			if row==1:
				nth2=row
				nth1=0
				nth=nth1+nth2
				if n==1:
					print(row,"number", nth)
					return(nth)
				row+=1
			nth=nth1+nth2
			if row>1 and row==n:
				print(row, "number",nth)
				return(nth)
			row+=1
			nth1=nth2
			nth2=nth

#print("fibonacci")
#fibonacci(0)
#fibonacci(1)
#fibonacci(2)
#fibonacci(3)


## Lucas
def lucas(n):
		row=0
		while row<=n:
			if n==0:
				nth1=2
				nth2=0
				nth=nth1+nth2
				print(row, "number", nth)
				return(nth)
				row+=1
			if n==1:
				nth2=1
				nth1=0
				nth=nth1+nth2
				print(row, "number",nth)
				return(nth)
				row+=1
			if row<=1:
				nth1=2
				nth2=1
			if row>1:
				if row==n:
					print(row," number",  nth)
					return(nth)
			row+=1
			nth=nth1+nth2
			nth1=nth2
			nth2=nth

#print( "Lucas")
#lucas(0)
#lucas(1)
#lucas(2)
#lucas(3)


## Generalization
def sum_series(n, n1, n2):
	if n1 ==' ': 
		print("fibonacci")
		fibonacci(n)
		return
	print("lucas")
	lucas(n)
	return

n0=0
n1=1
sum_series(3,' ' ,' ' )
sum_series(3,'2','1')



