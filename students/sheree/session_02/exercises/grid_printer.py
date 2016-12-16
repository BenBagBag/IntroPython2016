"""
    Grid Printer - First Draft In Class Exercise
    Python 3.5
"""

def horizontal_line(size, count):

    horizontal_rungs = "- "
    rung_joiner = "+ "
    line = ""
    while count > 1:
        line = line + rung_joiner + (horizontal_rungs * size)
        count -= 1
    else:
        line = line + rung_joiner + (horizontal_rungs * size) + rung_joiner
    return line
    pass


def vertical_line(size, count):

    vertical_rungs = "| "
    spaces = "  "
    line_count = count
    line = ""
    while line_count > 1:
        line = line + vertical_rungs + (spaces * size)
        line_count -= 1
    else:
        line = line + vertical_rungs + (spaces * size) + vertical_rungs
    return line
    pass


def grid_printer(box_size, box_count):

# TODO: are the args in fact integers, exit nicely if not


    for box in range(box_count):
        print(horizontal_line(box_size, box_count))
        for line in range(box_size):
            print(vertical_line(box_size, box_count))

    print(horizontal_line(box_size, box_count))

# grid_printer(False, 5.089777)
grid_printer(2, 2)
grid_printer(3, 1)
grid_printer(5, 5)
grid_printer(4, 4)
grid_printer(3, 3)
