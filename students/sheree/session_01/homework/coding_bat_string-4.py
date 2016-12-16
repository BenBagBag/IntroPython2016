'''
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
'''


def make_out_word(out, word):
    echo_word = str(out[:2] + word + out[2:])
    return echo_word

print(make_out_word('<<>>', 'Yay'))  # '<<Yay>>'
print(make_out_word('<<>>', 'WooHoo'))  # '<<WooHoo>>'
print(make_out_word('[[]]', 'word'))  # '[[word]]'