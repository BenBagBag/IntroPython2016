'''3rd LAB exercise from 161004'''

def fibonacci(n = 25):
    '''Returns the nth value in the Fibonacci series'''
    test_length(n)
    fib_list = [0, 1]
    for i in range(3,n+1):
        fib_list.append(fib_list[-1] + fib_list[-2])
    print("series: ", fib_list)
    return(fib_list[-1])

def lucas(n = 25):
    '''Returns the nth value in the Lucas series'''
    test_length(n)
    luc_list = [2, 1]
    for i in range(3,n+1):
        luc_list.append(luc_list[-1] + luc_list[-2])
    print("series: ", luc_list)
    return(luc_list[-1])

def sum_series(n = 25, sum0 = 0, sum1 = 1):
    '''Given two seeds returns the nth value in an integer series that adds 
    two consecutive terms to obtain the next one'''
    test_length(n)
    test_seeds(sum0, sum1)
    sum_list = [sum0, sum1]
    for i in range(3,n+1):
        sum_list.append(sum_list[-1] + sum_list[-2])
    print("series: ", sum_list)
    return(sum_list[-1])
    
def test_length(n):
    # Test for valid series length
    assert n > 2, "Series must have three or more elements"

def test_seeds(sum0, sum1):
    # Test for valid series seeds
    assert sum0 + sum1 > 0, "At least one of the initial values must be > 0"

# ===== Examples =====
# fibonacci(9)
# fibonacci(27)
# fibonacci(2)
# lucas(7)
# lucas(11)
# lucas(0)
# sum_series(5)
# sum_series(3,2,1)
# sum_series(15,1,1)
# sum_series(9,0,0)
