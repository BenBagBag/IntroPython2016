'''
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
'''


def make_abba(a, b):
    abba = str(a + (b * 2) + a)
    return abba


print(make_abba('Hi', 'Bye'))  # 'HiByeByeHi'
print(make_abba('Yo', 'Alice'))  # 'YoAliceAliceYo'
print(make_abba('What', 'Up'))  # 'WhatUpUpWhat'