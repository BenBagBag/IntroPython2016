"""Simple text grid drawing script
10/7/16 edit. Moved input typing to function call and eliminated redundant variables to shorten code and improve readability.
"""

ROWS = input("Rows: ")
COLUMNS = input("Columns: ")
SIZE = input("Size: ")

def print_grid(rows, columns, size):

    for i in range(rows):
        h_border(columns, size)

        for i in range(size):
            for j in range(columns):
                print("|" + (" " * ((size * 2 ) + 1)), end="")
                #print the vertical lines and cell spacing
            print("|")
    h_border(columns, size)

def h_border(columns, size):
    for i in range(columns):
        print('+' + (' -' * size) + ' ', end="")
    print('+')

print_grid(int(ROWS), int(COLUMNS), int(SIZE))

