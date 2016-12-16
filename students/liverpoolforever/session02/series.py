"""
This file prints the fibonacci series
"""
import sys
print("=============== PRINT THE FIBONACCI SERIES USING RECURSION =================================")

# Get rows and cols from the user -- other ways to do thi
ITERATIONS = int(sys.argv[1])

n1 = 0
n2 = 1

print("First 2 values in the series" , n1,n2)

def fibonacci(n):
    # Takes a parameter which the no of itertions to be computed
    global n1,n2
    if( n > 0):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print("Value: ", n3)
        fibonacci(n-1)

fibonacci(ITERATIONS)

# print("The result is: " , result)
