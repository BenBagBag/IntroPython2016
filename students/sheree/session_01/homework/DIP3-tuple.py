a_tuple = ('a', 'b', 'sheree', 'z', 'more')

print(a_tuple)

print(a_tuple[0])

print(a_tuple[-1])

print(a_tuple[1:3])

print(a_tuple.index('b'))

test = bool('z' in a_tuple)

print(test)

# 2.5.1 

def is_it_true(anything):
	if anything:
		print("yes, true")
	else:
		print("no, false")

is_it_true(())

is_it_true(('a', 'b'))

is_it_true((False,))

print(type((False)))

print(type((False,)))

# 2.5.2 

v = ('a', 2, True)

(x, y, z) = v

print(x)

print(y)

print(z)

		