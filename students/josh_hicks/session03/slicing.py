'''Write some functions that:

return a sequence with the first and last items exchanged.
return a sequence with every other item removed
return a sequence with the first and last 4 items removed, and every other item in between
return a sequence reversed (just with slicing)
return a sequence with the middle third, then last third, then the first third in the new order
NOTE: these should work with ANY sequence – but you can use strings to test, if you like.'''


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


def firstlast_exchange(l):
    flipped_ends = l[1:-1]
    flipped_ends.append(l[0])
    flipped_ends.insert(0, l[-1])
    return flipped_ends


def odds_removed(l):
    return l[1::2]


def four_by_four(l):
    four = l[4:-4]
    return four[1::2]


def reverse(l):
    return l[::-1]


def thirds(l):
    length = int(len(l) / 3)
    thirds = []
    thirds.extend(l[length:-length])
    thirds.extend(l[-length:])
    thirds.extend(l[:length])
    return thirds


print(firstlast_exchange(l))
print(odds_removed(l))
print(four_by_four(l))
print(reverse(l))
print(thirds(l))
