#!/usr/bin/env python3
"""
List Lab -- October 12, 2016
"""

def fruit_tree():
    print('-> List Lab: Section 1 <-')
    l = [ 'Apples', 'Pears', 'Oranges', 'Peaches' ]
    print("Original list:", l)
    
    add_fruit = input('What fruit would you like to add? ')
    l.append(add_fruit)
    print('List with input:', l)
    
    l_size = len(l)
    pick_fruit = int(input('Pick a number between 1 and %d: ' % l_size ))
    print('You picked fruit: %s' % l[pick_fruit - 1])
    
    l = ['Pinapple'] + l
    print('List add with + operator', l)
    
    l.insert(0, 'Strawberry')
    print('List add with .insert()', l)
    
    for fruit in l:
        if fruit[0] == 'P':
            print('Starts with "P": %s' % fruit)
    
    print()
    print('-> List Lab: Section 2 and BONUS<-')
    print('Starting list:', l)

    l.pop()
    print('Last fruit removed:', l)
    l = l[:] * 2
    print('Multiply string * 2:',l)
    del_chk = True
    while del_chk == True:
        del_fruit = input('Which fruit would you like to delete? ')
        if del_fruit in l:
            while del_fruit in l:
                l.remove(del_fruit)
            del_chk = False
        else:
            continue
    print('Current list:', l)

    print()
    print('-> List Lab: Section 3 <-')
    i = 0
    while i < len(l):
        answer = input('Do you like %s (yes / no)? ' % l[i].lower())
        if answer == 'yes':
            i += 1
        elif answer == 'no':
            l.pop(i)
        else:
            continue
    print(l)

    print()
    print('-> List Lab: Section 4 <-')
    new_l = l[:]
    rev_l = []
    for j in new_l:
        rev_l.append(j[::-1])
    new_l.pop()
    print('Copy of original:', new_l)
    print('Reverse of copy:', rev_l)

fruit_tree()
