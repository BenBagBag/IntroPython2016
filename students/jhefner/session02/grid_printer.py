"""
grid printer
"""

def cheat_grid():
    print("+ - - - - + - - - - +\n|         |         |\n|         |         |\n|         |         |\n|         |         |\n+ - - - - + - - - - +\n|         |         |\n|         |         |\n|         |         |\n|         |         |\n+ - - - - + - - - - +")

def grid_printer_part1():
    print("+"+" -"*4+" +"+" -"*4+" +")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("+"+" -"*4+" +"+" -"*4+" +")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("|"+" "*9+"|"+" "*9+"|")
    print("+"+" -"*4+" +"+" -"*4+" +")

def grid_printer_part2(size):
    height_width = size-1
    spaces = (size*2)-1
    print("+"+" -"*height_width+" +"+" -"*height_width+" +")
    for i in range(height_width):
        print("|"+" "*spaces+"|"+" "*spaces+"|")
    print("+"+" -"*height_width+" +"+" -"*height_width+" +")
    for i in range(height_width):
        print("|"+" "*spaces+"|"+" "*spaces+"|")
    print("+"+" -"*height_width+" +"+" -"*height_width+" +")

#cheat_grid()
#grid_printer_part1()
grid_printer_part2(10)