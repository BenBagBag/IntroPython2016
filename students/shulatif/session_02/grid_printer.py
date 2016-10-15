"""
grid printer
"""


def grid(i):
    cross = '+ ' + '- ' * i + '+ ' + '- ' * i + '+\n'
    blanks = '| ' + '  ' * i + '| ' + '  ' * i + '|\n'
    middle = blanks * i

    print(cross+middle+cross+middle+cross)

grid(5)
