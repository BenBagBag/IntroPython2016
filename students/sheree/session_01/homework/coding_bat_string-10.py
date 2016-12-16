"""
Given 2 strings, return their concatenation, except omit the first char of each.
The strings will be at least length 1.
"""


def non_start(a, b):
    foo = str(a[1:] + b[1:])
    return foo

print(non_start("hello", "there"))  # ellohere
print(non_start("java", "code"))  # avaode
print(non_start("shotl", "java"))  # hotlava
