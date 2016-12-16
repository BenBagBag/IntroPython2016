def near_ten(num):
    return (num % 10) == 0 or (num % 10) == 1 or (num % 10) == 2 or (num % 10) == 8 or (num % 10) == 9

def cigar_party(cigars, is_weekend):
    if is_weekend:
      if cigars >= 40:
        return True
    else:
      if cigars >= 40 and cigars <= 60:
        return True
    return False


print(near_ten(54))
print()
print(cigar_party(55, True))

print(locals())