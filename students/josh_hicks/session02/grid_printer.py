'''Grid Printer Exercise
PART 1
Printing a Grid

Goal:
Write a function that draws a grid like the following:

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
+ - - - - + - - - - +'''


def print_grid():
    grid1 = "+ - - - - + - - - - +"
    grid2 = "|         |         |"
    for x in range(0, 3):
        print(grid1)
        # Only print grid2 if we're not on the last iteration of grid1 loop
        if x < 2:
            for y in range(0, 4):
                print(grid2)


print_grid()


'''Write a function print_grid(n) that takes one integer argument and prints
a grid just like before, BUT the size of the grid is given by the argument.

For example, print_grid(11) prints the grid in the above picture.

print_grid(3) would print a smaller grid:

+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +
print_grid(15) prints a larger grid:

+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +'''


def print_grid(n):
    grid1 = "+ " + "- " * n + "+"
    grid2 = "|" + " " * n + "|" + " " * n + "|"
    for x in range(0, 3):
        print(grid1)
        # Only print grid2 if we're not on the last iteration of grid1 loop
        if x < 2:
            for y in range(0, n):
                print(grid2)

print_grid(3)
print_grid(15)
