# DIP3 - Chapter 2 - 2.6 - Sets: 2.6.4

a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}

print(a_set)

if 30 in a_set:
    print("True, 30 in a_set")
else:
    print("False, 30 not in a_set")
                                                  
if 31 in a_set:
    print("True, 31 in a_set")
else:
    print("False, 31 not in a_set")

b_set = {1, 2, 3, 5, 6, 8, 9, 12, 15, 17, 18, 21}

print(b_set)

print(a_set.union(b_set))  

print(a_set.intersection(b_set))
                                    
print(a_set.difference(b_set))

print(a_set.symmetric_difference(b_set))

print(b_set.symmetric_difference(a_set))