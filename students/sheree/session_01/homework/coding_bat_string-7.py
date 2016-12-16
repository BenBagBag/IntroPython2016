"""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
"""


def first_half(stringed):
    split = len(stringed) // 2
    halved = stringed[:split]
    return halved

print(first_half('WooHoo'))  # 'Woo'
print(first_half('HelloThere'))  # 'Hello'
print(first_half('abcdef'))  # 'abc'
