'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
'''


def sleep_in(weekday, vacation):
    return vacation == True or weekday == False


sleep_in(False, False) # True
sleep_in(True, False) # False
sleep_in(False, True) # True
sleep_in(False, False) # 
sleep_in(True, True) # 
sleep_in(None, True) # 
sleep_in(False, None) # 
