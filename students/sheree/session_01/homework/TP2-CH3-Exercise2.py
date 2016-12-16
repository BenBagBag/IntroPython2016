# Think Python v2 - Chapter 1 - 7 
#http://greenteapress.com/thinkpython2/html/index.html

# most of this is designed to be ran in the interactive interpreter 

# 3.14  Exercises # 2

def do_twice(func, arg):
    func(arg)
    func(arg)

def print_twice(arg):
    print(arg)
    print(arg)

def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_twice(print_twice, 'eggs')

print()
print()
print()

do_four(print_twice, 'spam')