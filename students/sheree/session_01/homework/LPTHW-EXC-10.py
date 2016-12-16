# excersize 10 was about showing newlines, escaping, tabs, etc
# we're using multi

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat fud
\t* Sid Fishous
\t* Catnipples\n\t* Grass
"""

# python 3.5
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# python 2.7
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# lol this bit is a inf loop that does a commandline spinner thing 
while True: 
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i, 
