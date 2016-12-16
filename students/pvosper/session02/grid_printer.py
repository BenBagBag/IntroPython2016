'''
    Think Python - Allen B. Downey
    Ex 3-3 (pg 33)
    Write a function that draws a grid
'''

# Arguments:
#   cell: size of each cell
#   grid: # of cells to print
#   aspect: affects ratio of height to width (2 = square-ish)

# Print symbols:
bar = "|"
plus = "+"
minus = "-"
space = " "

# A single horizontal bar
def horizontal(cell, grid, aspect):
    for i in range(grid):
        print(plus+minus*(cell), end = "-")
    # close horizontal (only 1 is needed)
    print(plus)

# A series of vertical bars
def vertical(cell, grid, aspect):
    for i in range(int(cell/aspect)):
        for i in range(grid):
            print(bar+space*(cell), end = " ")
        # close every vertical along the way
        print(bar)

# Grid construction
def print_grid(cell = 3, grid = 2, aspect = 2):
    for i in range(grid):
        horizontal(cell, grid, aspect)
        vertical(cell, grid, aspect)
    # close bottom
    horizontal(cell, grid, aspect)

print_grid(5,8,2)