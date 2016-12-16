"""
Given an array of ints length 3, return a list with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
"""


def rotate_left3(nums):
    sliced = nums[1:]
    first_item = nums[0]
    modified_list = sliced + [first_item]
    return modified_list

print(rotate_left3([1, 2, 3, 4, 5]))
