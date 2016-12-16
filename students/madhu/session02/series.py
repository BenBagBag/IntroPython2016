def fibonacci(n): #function to print out the nth element in the fibonacci series#
    """Return the nth element in the fibonacci series."""
    lst = []
    lst.insert(0,0)
    lst.insert(1,1)
    for i in range(2,n+1):
        value = lst[i-1] + lst[i-2]
        lst.insert(i,value)
    
    print ("The nth fibonacci number is: " + str(lst[n]))


def lucas(n): #function to print out the nth element in the lucas numbers series#
    """Return the nth element in the lucas sesies"""
    lst = []
    lst.insert(0,2)
    lst.insert(1,1)
    for i in range(2,n+1):
        value = lst[i-1] + lst[i-2]
        lst.insert(i,value)

    print ("The nth lucas number is: " + str(lst[n]))

def sum_series(n,first=0,second=1): #generalized function to return the nth in the series that starts with numbers specified in the first and second optional parameters# 
    """Return the nth element in the series whose first two elements are specified by the optional parameters"""
    lst = []
    lst.insert(0,first)
    lst.insert(1,second)
    for i in range(2,n+1):
        value = lst[i-1] + lst[i-2]
        lst.insert(i,value)

    print ("The nth number in the series is: " + str(lst[n]))



if __name__ == "__main__":
    fibonacci(10) #calling the fibonacci function to return the 10th element in the series#

    lucas(10) #calling the lucas function to retrun the 10th element in the series#

    sum_series(10) #calling the generalized function, sum_series without the optional parameters to generate the fibonacci number#

    sum_series(10,2,1) #calling the generalized function, sum_series to generate the lucas number#

    sum_series(10,3,2) #calling the generalized function, sum_series to generate the nth number in a random series#
