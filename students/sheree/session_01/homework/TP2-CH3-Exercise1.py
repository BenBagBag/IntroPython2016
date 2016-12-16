# Think Python v2 - Chapter 1 - 7 
#http://greenteapress.com/thinkpython2/html/index.html

# most of this is designed to be ran in the interactive interpreter 

# 3.14  Exercises

def right_justify(text):
    pep8_approved_length = 80
    length_of_string = len(text)
    move_string = ' '
    return move_string * (pep8_approved_length - length_of_string) + text
    
print(right_justify("ShortString"))
print(right_justify("x"))
print(right_justify("longlonglonglonglonglonglong"))
print(right_justify("************************************************"))
print(right_justify("what"))
print(right_justify("right"))
print(right_justify("babababababbabaabaabbababababababababbababababababbabababa"))
