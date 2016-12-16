"""
Given a string, return the string made of its first two chars, so the String "Hello" yields\
 "He". If the string is shorter than length 2, return whatever there is, so "X" yields \
 "X", and the empty string "" yields the empty string "".
"""

def first_two(snip_string):
    if len(snip_string) < 2:
        snipped_string = snip_string
    else:
        snipped_string = str(snip_string[:2])
    return snipped_string


print(first_two('Hello'))  # 'He'
print(first_two('abcdefg'))  # 'ab'
print(first_two('ab')) # 'ab'
print(first_two('X')) # 'X'