input_file = open('words.txt')

words_raw = input_file.readlines()

words = [word.strip() for word in words_raw]


def recurse(array, lower, upper, item):
    midpoint = (lower + upper) // 2
    midpoint_value = array[midpoint]
    if lower > upper:
        return None
    elif midpoint_value < item:
        return recurse(array, midpoint + 1, upper, item)
    elif midpoint_value > item:
        return recurse(array, lower, midpoint - 1, item)
    else:
        return midpoint

print(recurse(words, 0, len(words), "cat"))
print(recurse(words, 0, len(words), "sldkjlasdfjk"))
