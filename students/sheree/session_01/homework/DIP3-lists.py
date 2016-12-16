a_list = ['a', 'b', 'sheree', 'z', 'example']

print(a_list)

print(a_list[0])

print(a_list[4])

print(a_list[-1])

print(a_list[-3])

print(a_list[1:3])

print(a_list[1:-1])

print(a_list[0:3])

print(a_list[:3])

print(a_list[3:])

'''
	If both slice indices are left out, all items of the list are included. But this is not the same as the original a_list variable. It is a new list that happens to have all the same items. a_list[:] is shorthand for making a complete copy of a list.
'''

print(a_list[:])

a_list = a_list + [2.0, 3]

print(a_list)

a_list.append(True)

print(a_list)

a_list.extend(['four', "some char I can't print"])

print(a_list)

a_list.insert(0, "FIRST")

print(a_list)

a_list = ['1']

print(a_list)

a_list.append("one item")

print(a_list)

a_list.extend(['item one', 'item two', 'item three'])

print(a_list)

print(a_list.count('1'))

print(a_list.count('one'))

print(a_list.count('one item'))

print(a_list.index('1'))

del a_list[1]

print(a_list)

a_list.remove('item three')

print(a_list)

a_list.pop()

print(a_list)


a_list.pop()

print(a_list)