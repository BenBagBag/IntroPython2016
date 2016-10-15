"""
grid printer
"""
print('something')

def divider():
    print("+ " + "- " * 5 + "+ " + "- " * 5 + "+")

def rows():
    print("|" + " " * 11 + "|" + " " * 11 + "|")

def print_grid():
    print ("this will be a grid")
    print("+ " + "- " * 5 + "+ " + "- " * 5 + "+")
    print("|" + " " * 11 + "|" + " " * 11 + "|")
    print("|" + " " * 11 + "|" + " " * 11 + "|")
    print("|" + " " * 11 + "|" + " " * 11 + "|")
    print("|" + " " * 11 + "|" + " " * 11 + "|")
    print("+ " + "- " * 5 + "+ " + "- " * 5 + "+")
    print("|" + " " * 11 + "|" + " " * 11 + "|")
    print("|" + " " * 11 + "|" + " " * 11 + "|")
    print("|" + " " * 11 + "|" + " " * 11 + "|")
    print("|" + " " * 11 + "|" + " " * 11 + "|")
    print("+ " + "- " * 5 + "+ " + "- " * 5 + "+")

print_grid()

print()
print('this time with functions:')
print()

def print_grid_again():
    divider()
    rows()
    rows()
    rows()
    rows()
    divider()
    rows()
    rows()
    rows()
    rows()
    divider()

print_grid_again()
