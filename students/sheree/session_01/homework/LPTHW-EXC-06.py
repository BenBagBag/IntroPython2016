#exersize 6 - strings and text
# here we set the placeholder in the var which is  string and the placeholder is a num
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# here we set a var with two of our other vars and replace two placeholders with those vars
y = "Those who know %s and those who %s." % (binary, do_not)

#here we print our vars above that then show other values
print(x)
print(y)

# here we print strings with placeholders that are our longer vars that contain other vars and placeholders
print("I said: %r." % x)
print("I also said: '%s'." % y)

# this var should be a boolean, shouldn't it, we get a clean print out because we are using r which will print anything
hilarious = True
# this is a var that has a string that contains our boolean above
joke_evaluation = "Isn't that joke so funny!? %r" 

# here we print out the var which contains ours boolean 
print(joke_evaluation % hilarious)

# here are some vars that are strings
w = "This is the left side of..."
e = "a string with a right side."

# this shows concatenation of those vars as strings
print(w + e)

