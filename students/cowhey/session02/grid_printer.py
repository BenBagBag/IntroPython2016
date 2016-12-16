# part 1
def draw_grid():
    '''Write a function that draws a grid like the following:
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +

    '''
    end_row = ('+ ' + '- ' * 4) * 2 + '+'
    mid_row = ('| ' + '  ' * 4) * 2 + '|'
    for x in range(2):
        print(end_row)
        for y in range(4):
            print(mid_row)
    print(end_row)


# part 2
def get_multiplier(n):
    '''find correct multiplier for grid;
    round down by one if number is even'''
    if n % 2 == 0:
        return n / 2
    else:
        return n // 2


def print_grid(n):
    '''print a grid with n characters (if n is odd)
    or n + 1 characters (if n is even) between endpoints ('+')'''
    multiplier = get_multiplier(n)
    end_row = ('+ ' + '- ' * multiplier) * 2 + '+'
    mid_row = ('| ' + '  ' * multiplier) * 2 + '|'
    for x in range(2):
        print(end_row)
        for y in range(multiplier):
            print(mid_row)
    print(end_row)


# part 3
def make_end_row(w, num):
    '''make row of num columns with a width of w times "+ "'''
    return ('+ ' + '- ' * w) * num + '+'


def make_middle_row(w, num):
    '''make row of num columns with a width of w times "+ "'''
    return ('| ' + '  ' * w) * num + '|'


def print_two_param_grid(x, y):
    '''Print a grid with x boxes in x rows;
    each box has dimensions y by y.
    NB: your instructions say three columns, but your examples are different.
    I'm following the examples.'''
    end_row = make_end_row(y, x)
    mid_row = make_middle_row(y, x)
    for i in range(x):
        print(end_row)
        for j in range(y):
            print(mid_row)
    print(end_row)
