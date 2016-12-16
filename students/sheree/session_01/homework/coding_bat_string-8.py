"""
Given a string, return a version without the first and last char, so "Hello" \
yields "ell". The string length will be at least 2.

"""


def without_end(stringg):
    middles = stringg[1:-1]
    return middles


print(without_end('Hello'))  # 'ell'
print(without_end('java'))  # 'av'
print(without_end('coding'))  # 'odin'
