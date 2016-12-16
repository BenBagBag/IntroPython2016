def print_grid(n):

    plus = '+'
    minus = '- '

    cell_size = n // 2
    length = cell_size + (cell_size - 1) + 2
    ends = '+ ' + ('- ' * cell_size)
    bars = '|' + (' ' * length)
    
    for i in range(0,2):
        print ((ends * 2) + '+')
        for i in range(0,cell_size):
            print ((bars * 2) + '|')
    print ((ends * 2) + '+')



print_grid(10)
print_grid(15)


def print_grid2(rows,cell_size):

    plus = '+'
    minus = '- '
    length = cell_size + (cell_size - 1) + 2
    bars = '|' + (' ' * length)
    ends = '+ ' + ('- ' * cell_size)

    for i in range(0,rows):
        print ((ends * rows) + '+')
        for i in range(0,cell_size):
            print ((bars * rows) + '|')
    print ((ends * rows) + '+')


print_grid2(3,4)
print_grid2(2,3)
print_grid2(5,3)
