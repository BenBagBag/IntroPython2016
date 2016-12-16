def while_func(num, mystep=1):
    i = 0
    numbers = []

    for i in range(0,num,mystep):
    # while i < num:
        print ("At the top i is %d" % i)
        numbers.append(i)

        # i = i + mystep
        print ("Numbers now: ", numbers)
        print ("At the bottom i is %d" % i)


    print ("The numbers: ")

    for num in numbers:
        print (num)

while_func(5)

"""
WITH the incrementor in ouput looks like:
At the top i is 0
Numbers now:  [0]
At the bottom i is 1
At the top i is 1
Numbers now:  [0, 1]
At the bottom i is 2
At the top i is 2
Numbers now:  [0, 1, 2]
At the bottom i is 3
At the top i is 3
Numbers now:  [0, 1, 2, 3]
At the bottom i is 4
At the top i is 4
Numbers now:  [0, 1, 2, 3, 4]
At the bottom i is 5     <----- DIFF
The numbers: 
0
1
2
3
4

WITHOUT the incrementor in ouput looks like:
At the top i is 0
Numbers now:  [0]
At the bottom i is 0
At the top i is 1
Numbers now:  [0, 1]
At the bottom i is 1
At the top i is 2
Numbers now:  [0, 1, 2]
At the bottom i is 2
At the top i is 3
Numbers now:  [0, 1, 2, 3]
At the bottom i is 3
At the top i is 4
Numbers now:  [0, 1, 2, 3, 4]
At the bottom i is 4     <----- DIFF
The numbers: 
0
1
2
3
4
"""