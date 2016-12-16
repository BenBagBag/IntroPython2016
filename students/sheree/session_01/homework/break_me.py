# Task 3 Week 1 Homework "Explore Errors"


def name_error_example():
    print("This should give a NameError")
    print(hello_error)
    return

def type_error_example():
    apple = "apple"
    pie = 3.14597
    print("This should give a TypeError")
    apple + pie
    return

def syntax_error_example():
    print("This should give a SyntaxError")
    7 + 8 ===
    return

def attribute_error_example():
    print("This should give an AttributeError")
    foo = False.foo
    return

attribute_error_example()
syntax_error_example()
type_error_example()
name_error_example()

