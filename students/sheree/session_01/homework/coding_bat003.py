"""
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""

def pos_neg(a, b, negative):
	if negative: 
		print("i evaluated to True am returning true if a and b are negative")
		return (a < 0) and (b < 0)
	else:
		print("negative was set to False and I'm returning True if either a or b are negative")
		return ((a > 0) and (b < 0) or (b > 0) and (a < 0))


pos_neg(1, -1, False)
pos_neg(-1, 1, False)
pos_neg(1, 1, True)
pos_neg(1, 1, False)
pos_neg(-4, -5, True)
pos_neg(0, 0, True)
pos_neg(0, 0, False)