# ===== Slicing Lab ======
# In class assignment

# return a sequence with the first and last items exchanged.
def first_last(sequence):
    return sequence[-1:] + sequence[1:-1] + sequence[:0]
    # sequence[-1] is just an integer, sequence[-1:] is a list with a single element
    # Otherwise: TypeError: unsupported operand type(s) for +: 'int' and 'list'

print("first_last")
print(first_last("123456789"))
print(first_last([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# return a sequence with every other item removed
def every_other(sequence):
    return sequence[::2]

print("every_other")
print(every_other("123456789"))
print(every_other([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# return a sequence with the first and last 4 items removed, and 
#   remove every other item in between
def first_last4(sequence):
    # return sequence[1:-3:2] # I interpreted this different
    return sequence[4:-4:2]

print("first_last4")
print(first_last4("123456789abcdef"))
print(first_last4([1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]))

# return a sequence reversed (just with slicing)

def reversed(sequence):
    return sequence[::-1]

print("reversed")
print(reversed("123456789"))
print(reversed([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# return a sequence with the middle third, then last third, then the first third in the new order

def thirds(sequence):
    # third = int(len(sequence)/3)
    third = len(sequence)//3 # int
    return sequence[third:third*2] + sequence[third*2:] + sequence[0:third]

print("thirds")
print(thirds("123456789"))
print(thirds([1, 2, 3, 4, 5, 6, 7, 8, 9]))
