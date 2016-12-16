'''
'''






def printgrid():
    print("this will be a grid")

    pos = 0

    while pos < 11:
        if pos % 5 == 0:
            print("+----+----+")
            pos += 1
        else:
            print("|    |    |")
            pos += 1
    else:
        print()



printgrid()



