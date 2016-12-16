"""
Grid Printer Assignment

Prints a box:

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
+ - - - - - - - + - - - - - - - +

"""

def make_grid(size, boxes):
    """
    This is gross, but it works.
    """
    if boxes > 1:
        border = ("+" + "-" * size)
        row = ("|" + " " * size)
        for i in range(0, boxes):
            print(border * boxes + "+")
            for i in range(0, size):
                print(row * boxes + "|")
        print(border * boxes + "+")
    elif boxes == 1:
        print("+" + "-" * size + "+")
        for i in range(0, size):
            print("|" + "   " * size + "|")
        print("+" + "-" * size + "+")
