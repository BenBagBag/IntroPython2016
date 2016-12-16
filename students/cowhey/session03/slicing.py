def switch_first_and_last(sequence):
    '''return a sequence with the first and last items exchanged.'''
    first = sequence[0]
    last = sequence[-1]
    # the problem here is that array[0] returns an int, not an arr
    # and you can't concatenate an int and an arr
    # so test for type before concatenating
    if type(sequence) == list:
        return [last] + sequence[1:-1] + [first]
    else:
        return last + sequence[1:-1] + first


def remove_every_other(sequence):
    '''return a sequence with every other item removed'''
    return sequence[::2]


def middle_skip(sequence):
    '''return a sequence with the first and last 4 items removed, and every other item in between'''
    return sequence[4:-4][::2]


def reverse(sequence):
    '''return a sequence reversed (just with slicing)'''
    return sequence[::-1]


def mix_thirds(sequence):
    '''return a sequence with the middle third, then last third, then the first third in the new order'''
    third = len(sequence) // 3
    return sequence[third:2*third] + sequence[2*third:] + sequence[0:third]
