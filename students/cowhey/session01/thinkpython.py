# ch. 6 exercises for thinking in python

def A(m, n):
    '''evaluates Ackerman function for two numbers'''
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return A(m - 1, 1)
    elif m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))
    print('those numbers don\'t work')

# print(A(3, 4))


def pal(string):
    if len(string) == 1:
        return True
    elif len(string) == 2:
        if string[0] == string[1]:
            return True
        return False
    elif string[0] == string[-1]:
        return pal(string[1:-1])
    else:
        return False

# print(pal("amanaplanacanalpanama"))

def power(x, y):
    '''see if x is a power of y, return True if so'''
    if x == 0 or (abs(x) == 1 and abs(y) != 1):
        return False
    if y % x == 0 and y / x == 1:
        return True
    elif y % x == 0 and y / x != 1:
        return power(x, y / x)
    else:
        return False

# print(power(-3, -9))

def gcd(a, b):
    sm = min(a, b)
    lg = max(a, b)
    if sm == 0:
        return 'dividing by zero is not a thing'
    elif sm == 1:
        return 1
    elif lg % sm == 0:
        return sm
    elif lg % sm != 0:
        r = lg % sm
        return gcd(sm, r)

print(gcd(3, 38))
