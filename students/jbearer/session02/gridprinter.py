# Grid Printer Exercise
# Session02 - Oct. 5, 2016

def simple_grid():
    """ Prints a simple grid """
    print("Simple Grid")
    print("+----+----+")
    print("|" + "    " + "|" + "    " + "|")
    print("|" + "    " + "|" + "    " + "|")
    print("|" + "    " + "|" + "    " + "|")
    print("|" + "    " + "|" + "    " + "|")
    print("+----+----+")
    print("|" + "    " + "|" + "    " + "|")
    print("|" + "    " + "|" + "    " + "|")
    print("|" + "    " + "|" + "    " + "|")
    print("|" + "    " + "|" + "    " + "|")
    print("+----+----+")
    print()

simple_grid()

""" ================================================== """

def print_dyn(n):
    """ Prints a dynamic grid """
    print("Dynamic Grid")
    line = ("+" + ("-" * n) + "+" + ("-" * n) + "+")
    bars = ("|" + (" " * n) + "|" + (" " * n) + "|")

    def print_it():
        for i in range(0, 2):
            print(line)
            for j in range(n):
                print(bars)
        print(line)

    print_it()
    print()

print_dyn(5)

""" ================================================== """

def print_grid(x,y):
    print("Variable size grid")
    line = (("+" + ("-" * x )) * y + "+")
    bars = (("|" + (" " * x )) * y + "|")

    def print_it():
        for i in range(y):
            print(line)
            for j in range(x):
                print(bars)
        print(line)

    print_it()
    print()

print_grid(6,5)







