'''
Given two int values, return their sum. Unless the two values are the same, then return double their sum.
'''

def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b
	  

sum_double(1, 2) # 3
sum_double(3, 2) # 5
sum_double(2, 2) # 8
sum_double(2, 0) # 
sum_double(4, 4) # 
sum_double(22, 22) # 
sum_double(44, 22) # 