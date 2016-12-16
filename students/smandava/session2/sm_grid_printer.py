""""Oct 10th, 2016: Class 2: Grid Printer exercise."""


# Global constants
PLUS = '+'
MINUS = '-'

# Part 1: Printing a Grid.


def print_horizontal():
    """Return Horizontal line."""
    print(PLUS + 4 * MINUS + PLUS + 4 * MINUS + PLUS)


def print_vertical():
    """Return Vertical line."""
    print('|' + '    |' + '    |')


def print_grid1():
    """Return the grid."""
    i = 0
    print_horizontal()
    for i in range(1, 5):
        print_vertical()
    print_horizontal()
    for i in range(1, 5):
        print_vertical()
    print_horizontal()

print_grid1()

# Part 2: Printing a grid by accepting size of the grid.


def print_grid2(n):
    """Print grid based on input size."""
    m = ((n - 3) // 2)
    for i in range(0, n, n):
        for i in range(0, n, n):
            print(PLUS + m * MINUS + PLUS + m * MINUS + PLUS)
        for i in range(1, n // 2, 1):
            print('|' + m * ' ' + '|' + m * ' ' + '|')
        for i in range(0, n // 2, n // 2):
            print(PLUS + m * MINUS + PLUS + m * MINUS + PLUS)
        for i in range(n // 2 + 1, n - 1, 1):
            print('|' + m * ' ' + '|' + m * ' ' + '|')
        for i in range(0, n, n):
            print(PLUS + m * MINUS + PLUS + m * MINUS + PLUS)


# Part 3: Printing a grid by accepting number of rows and columns.


def print_plus():
    """Return +."""
    return PLUS


def print_minus():
    """Return ---."""
    return 3 * MINUS


def print_bar():
    """Return |   ."""
    return '|' + 3 * ' '


def print_grid3(x, y):
    """Print grid based on rows and columns input."""
    m = y + 1
    for i in range(0, x, 1):
        for i in range(0, y, 1):
            row = print_plus() + print_minus()
            print(row, end='')
        print('+', '\n')
        # for i in range(0, y, 1):
        for i in range(0, m, 1):
            column = print_bar()
            print(column, end='')
        print('\n')
    for i in range(0, y, 1):
        row = print_plus() + print_minus()
        print(row, end='')
    print('+')
# *******************************************************
# *******************End of Program**********************
