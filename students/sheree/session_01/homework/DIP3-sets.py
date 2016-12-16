# DIP3 - Chapter 2 - 2.6 - Sets

a_set = {1}

print(a_set)

print(type(a_set))

a_set = {1, 2}

print(a_set)

a_list = ['a', 'b', 'c']

a_set = set(a_list)

print(a_set)

new_set = set()

print(new_set)

print(len(new_set))

not_a_set = {}

print(type(not_a_set))

# 2.6.2 

qwik_set = {1, 2}

qwik_set.add(4)

print(qwik_set)

print(len(qwik_set))

qwik_set.add(1)

print(qwik_set)

print(len(qwik_set))

another_set = {1, 2, 3}

print(another_set)

another_set.update({2, 4, 6})

print(another_set)

another_set.update({3, 6, 9}, {1, 2, 3, 5 ,8, 13})

print(another_set)

another_set.update([10, 30, 40])

print(another_set)

# 2.6.3 

set_remove = {1, 3, 6, 10, 15, 21, 28, 36, 45}

print(set_remove)

set_remove.discard(10)

print(set_remove)

#set_remove.remove(12324)

