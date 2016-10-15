print("You climb into a car.  What do you do next?")
print("1. Put the seat belt on.")
print("2. Adjust the rearview mirror.")

action1 = input("> ")

if action1 == "1":
    print("The seat belt clicks into place. What do you do next?")
    print("1. Start the car.")
    print("2. Open the window.")
    action2 = input("> ")
    if action2 == "1":
        print("The car starts and you happily drive down the road.")
    elif action2 == "2":
        print("You open the window and get a breath of fresh air.")
    else:
        print("You are confused and pretend you are a race car driver.")
elif action1 == "2":
    print("You can now see out the rear window. What do you do next?")
    print("1. Start the car.")
    print("2. Relese the emergency break.")
    if action2 == "1":
        print("The car starts and you happily drive down the road.")
    elif action2 == "2":
        print("You release the emergency break and roll into the car in front of you.")
    else:
        print("You just stare into the mirror at yourself.")
else:
    print("You were arrested by the police because it wasn't your car!")
