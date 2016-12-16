def parrot_trouble(talking, hour):
    print(not(7 <= hour <= 20) and talking)


def makes10(a, b):
    return a == 10 or b == 10 or a + b == 10


def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)
