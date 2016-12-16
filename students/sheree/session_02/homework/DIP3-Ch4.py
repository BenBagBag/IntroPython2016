#Dive Into Python Chapter 4

# 4.4

s = "🐍 深入 Python"

print(len(s))

print(s[0])

print(s[1])

print(s[2])

print(s[3])

username = 'sheree'

password = 'notthemamaimthebaby'

print("{0}'s password is {1}".format(username, password))

print()
print()

# 4.5

long_stringy =  ''' finished files are the result of years of scientific study combined with the experience of years'''

print(long_stringy.splitlines())

print(long_stringy.upper())

print(long_stringy.count('f'))

print()
print()

query = 'user=sheree&database=master&password=notthemamaimthebaby'
a_list = query.split('&')
print(a_list)

a_list_of_lists = [v.split("=", 1) for v in a_list if "=" in v]
print(a_list_of_lists)

a_dict = dict(a_list_of_lists)

print(a_dict)

print()
print()

# 4.5.1

a_string = "My alphabet starts where your alphabet ends."

print(a_string[3:11])
print(a_string[3:-3])
print(a_string[0:2])
print(a_string[:18]) # from the beginning to n
print(a_string[18:]) # from n to the end 