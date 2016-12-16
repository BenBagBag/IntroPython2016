"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: grid printer

Description:
This program constructs a grid based on specific size parameters.
"""
# -------------------------------Functions--------------------------------------


def grid_line():
    """
    Print each row of grid.
    """
    print('+' + (2 * ('-' * 4 + '+')))
    print((('|' + (2 * (' ' * 4 + '|')) + '\n') * 4), end='')
    print('+' + (2 * ('-' * 4 + '+')))
    print((('|' + (2 * (' ' * 4 + '|')) + '\n') * 4), end='')
    print('+' + (2 * ('-' * 4 + '+')))


def print_grid(n):
    """
    Print each line of the grid based on the value of integer argument n.
    Values for n dictate the size of each line.
    """
    size = n // 2
    print('+' + (2 * ('-' * size + '+')))
    print((('|' + (2 * (' ' * size + '|')) + '\n') * size), end='')
    print('+' + (2 * ('-' * size + '+')))
    print((('|' + (2 * (' ' * size + '|')) + '\n') * size), end='')
    print('+' + (2 * ('-' * size + '+')))


def print_grid2(rc, s):
    """
    Print each line of the grid based on the value of integer arguments rc
    and s. Values for rc dictate the number of rows and colums while values for
    s dictate the size of each cell.
    """
    print('+' + (rc * ('-' * s + '+')))
    print(((('|' + (rc * (' ' * s + '|')) + '\n') * s) +
          ('+' + (rc * ('-' * s + '+'))) + '\n') * rc, end='')

# ==============================================================================


def main():
    """
    Build a grid based on a specific cell, row and column size parameters.
    """
    grid_line()
    print_grid(15)
    print_grid(3)
    print_grid2(3, 4)
    print_grid2(5, 3)


if __name__ == '__main__':
    main()
