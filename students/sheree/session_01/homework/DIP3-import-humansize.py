import sys

my_path = "/Users/sheree/Documents/dev/IntroPython2016-ShereeFork/students/sheree/session_01/homework/"

sys.path.insert(0, my_path)

import humansize

print(humansize.approximate_size(4096, True))

print(humansize.approximate_size.__doc__)

## this is sloppy but the book wanted me to run this in an interactive interpreter and I did not want to