people = 17
cats = 26
dogs = 7

if people < cats:
	print("too many cats, the world is doomed")
	pass

if people > cats:
	print("not many cats, the world is saved")
	pass

if people < dogs:
	print("the world is drooled on")
	pass

if people > dogs:
	print("the world is dry")
	pass

dogs += 5

if people >= dogs:
	print("people are greater than or equal to dogs")
	pass

if people <= dogs:
	print("people are less than or equal to dogs")
	pass

if people == dogs:
	print("People are dogs")