print(''' 
''')

print("Welcome to TREASURE ISLAND")
print("your mission is to find the treasure")
step1 = input("you're on a crossroad would you want to go left or right? L or R:  ")
step2 = input("you've arrived a lake, would you like to swim or wait? S or W:  ")
step3 = input("which door would you like to enter? red, blue, or yellow:  ")
lowercase = step3.lower()
if (step1 == "L") or (step1 == "l"):
    print(step2)
    if (step2 == "W") or (step3 == "w"):
        print(step3)
        if (lowercase == "yellow"):
            print("YOU WIN")
        else:
            print("         GAME OVER")
    else:
        print("         GAME OVER")
elif (step1 == "R") or (step1 == "r"):
    print("you fell of a cliff\n         GAME OVER")
# else:
#     print("         GAME OVER")