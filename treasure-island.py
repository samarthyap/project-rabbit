print("Welcome to Treasure Island")
print("Your mission is to find treasure")
print("Type left or L or l to go to the  left ")
print("Type right or R or r to go to the right")
direction = input("Do You wanna go left or right?(L or R)?")
if (direction == "L" or direction == "left"):
    print("Do you want to swim or wait?")
    print("Type swim or s to swim")
    print("Type wait or w to wait")
    nextstop = input("Do you want to swim or wait?(s/w)")
    if (nextstop == "wait" or nextstop == "w"):
        print("Three Door Appear: Red /Blue/Yellow")
        print("Which door do you want to enter ?")
        print("Type Red or r for red door and  Blue or b for blue door and yellow or y for yellow door")
        door = input("Which door do you want to enter?(r/b/y)")
        if (door == "yellow" or door == "y"):
            print("You found the treasure")
        elif (door == "red" or door == "r"):
            print("You are burnt alive")
            print("Game Over")
        elif (door == "blue" or door == "b"):
            print("You got eaten by mosnter")
            print("Game Over")
        else:
            print("Error!Game Over")
    elif (nextstop == "swim" or nextstop == "s"):
        print("You got eaten by trout")
        print("Game Over")
    else:
        print("Game Over")
elif (direction == "R" or direction == "right"):
    print("You fell into hole")
    print("Game Over")
else:
    print("Game Over")
