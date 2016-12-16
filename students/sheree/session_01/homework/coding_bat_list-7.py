"""
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
"""


def middle_way(a, b):
    del a[0], b[0]
    del a[-1], b[-1]
    new_mids_list = []
    new_mids_list.append(a[0])
    new_mids_list.append(b[0])
    return new_mids_list

print(middle_way([1, 2, 3], [4, 5, 6]))  # [2, 5]
print(middle_way([7, 7, 7], [3, 8, 0]))  # [7, 8]
print(middle_way([5, 2, 9], [1, 4, 5]))  # [2, 4]