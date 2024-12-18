print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
 ''')

print("Welcome to TREASURE ISLAND")
print("your mission is to find the treasure")
step1 = input("you're on a crossroad where do you want to go? type 'left' or 'right':  ").lower()
if step1 == "left":
    step2 = input("you've arrived a lake. There's an island in the middle of the lake. \nType 'Wait' to wait for a boat or 'Swim' to swim accross:  ").lower()
    if (step2 == "wait"):
        step3 = input("You've arrived at the island unharmed. there are 3 doors which door would you choose? red, blue, or yellow:  ").lower()
        if (step3 == "yellow"):
            print("CONGRATS!!!!! you found the treasure.  YOU WIN")
        elif step3 == "blue":
            print("a room full of beast. GAME OVER")
        elif step3 == "red":
            print("is a room full of fire. GAME OVER")
        else:
            print("you chose a door that does not exist. GAME OVER")
    else:
        print("Lake is full of crocodiles         GAME OVER")
elif (step1 == "R") or (step1 == "r"):
    print("you fell of a cliff\n         GAME OVER")
# else:
#     print("         GAME OVER")