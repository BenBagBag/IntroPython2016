# This was me getting ahead of myself reading about stuff. I haven't gotten 
# that far yet. Keeping here so I can revisit it once I know what I'm doing
# and have better ideas about how to approach things


# class LineBuilder(object):

#     def __init__(self, size, count, join_char, sides_char):

#         self.size = size
#         self.count = count
#         self.join_char = join_char
#         self.sides_char = sides_char

#     def line_builder(self):
#         self.sides_char = sides_char
#         self.join_char = join_char
#         line = ""
#         while self.count > 1:
#             line = line + self.join_char + (self.sides_char * self.size)
#             self.count -= 1
#         else:
#             line = line + self.join_char + (self.sides_char * self.size) + self.join_char
#         return line


# def grid_printer(box_size, box_count):


    # for box in range(box_count):
    #     print(horizontal_line(box_size, box_count))
    #     for line in range(box_size):
    #         print(vertical_line(box_size, box_count))

    # print(horizontal_line(box_size, box_count))

 # grid_printer(False, 5.089777)
# grid_printer(2, 2)


# TODO: take input from the user asking for modest integers lower than 20
# validate that it's useful, print a box
# ask for side chars x and y so they can make a box out of whatever they want
