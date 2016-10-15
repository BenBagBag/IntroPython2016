"""
Slicing Lab

Goal
Get the basics of sequence slicing down

Tasks
Write some functions that:

return a sequence with the first and last items exchanged.
return a sequence with every other item removed
return a sequence with the first and last 4 items removed, and every other item in between
return a sequence reversed (just with slicing)
return a sequence with the middle third, then last third, then the first third in the new order
NOTE: these should work with ANY sequence – but you can use strings to test, if you like.
"""

sequence = "This is definitely a sequence."

first_last_exchanged = sequence[-1]+sequence[1:-1]+sequence[0]
print(first_last_exchanged)

every_other_item_removed = sequence[::2]
print(every_other_item_removed)

# Award for worst variable name goes to.....
first_and_last_4_removed_every_other_item_between = sequence[4]+sequence[4:-5:2]+sequence[-5]
print(first_and_last_4_removed_every_other_item_between)

sequence_reversed = sequence[::-1]
print(sequence_reversed)


third_of_a_sequence = int(len(sequence)/3)
sequence_thirds_new_order = sequence[third_of_a_sequence*1:third_of_a_sequence*2]+ sequence[third_of_a_sequence*2:third_of_a_sequence*3]+sequence[third_of_a_sequence*0:third_of_a_sequence*1]
print(sequence_thirds_new_order)