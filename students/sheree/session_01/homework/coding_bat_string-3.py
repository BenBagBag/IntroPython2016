'''
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
'''


def make_tags(tag, word):

    tagged_word = str("<{0}>{1}</{0}>").format(tag, word)
    return tagged_word



print(make_tags('i', 'Yay')) # '<i>Yay</i>'
print(make_tags('i', 'Hello'))  # '<i>Hello</i>'
print(make_tags('cite', 'Yay'))  # '<cite>Yay</cite>'