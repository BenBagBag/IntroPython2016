# recursion scratch file

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)
        
countdown(10)
print()
countdown(1)
print()
countdown(0)
print()
countdown(100)

print()
print()
print()

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)
    
print_n("Spam & Eggs Forever", 20)