"""Given an array of ints, return a new array length 2 containing the first
 and last elements from the original array. The original array will be length 1 or more."""

def make_ends(nums):
    new_list = []
    new_list.append(nums[0])
    new_list.append(nums[-1])
    return new_list

print(make_ends([1, 2, 3]))  # [1, 3]
print(make_ends([1, 2, 3, 4]))  # [1, 4]
print(make_ends([7, 4, 6, 2]))  # [7, 2]
