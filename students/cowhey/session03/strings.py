print("file_{:03d} : {:8.2f}, {:1.0e}".format(2, 123.4567, 10000))


def print_first_three(nums):
    '''print first three numbers of a tuple in formatted string'''
    print("the first 3 numbers are: {:d}, {:d}, {:d}".format(*nums))

print(print_first_three(3, 4, 2, 3, 1, 10))
