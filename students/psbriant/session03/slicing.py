"""
Name: Paul Briant
Date: 10/11/16
Class: Introduction to Python
LAB: Slicing

Description:

"""
# -------------------------------Import-----------------------------------------

# -------------------------------Functions--------------------------------------


def first_last(s):
    """

    """
    return s[-1:] + s[1:-1] + s[:0]


def every_other(s):
    """

    """
    return s[::2]


def four_removed(s):
    """

    """
    return s[4:-4:2]


def reversed1(s):
    """

    """
    return s[::-1]


def third_is_the_word(s):
    """

    """
    t = len(s) // 3
    return s[t:-t] + s[-t:] + s[:t]


# ==============================================================================


def main():
    """
    Hi
    """
    first_last('mississippi')
    every_other('mississippi')
    four_removed('mississippi')
    reversed1('mississippi')
    third_is_the_word('mississippi')


if __name__ == '__main__':
    main()
