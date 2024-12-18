print("WELCOME TO THE ROCK PAPER SCISSORS GAME!!!\n\n")
rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''
scissors = '''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''
paper = '''
_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|  
'''
Gameimages = [rock, paper, scissors]
import random
Computer_choice = random.randint(0,2)
User_choice = int(input("type 0 for Rock, 1 for paper, 2 for scissors.\n"))
if User_choice > 2 or User_choice < 0:
    print("you typed an invalid number. you lose")
else:
    print("You chose: ")
    print(Gameimages[User_choice])
    print("Computer chose: ")
    print(Gameimages[Computer_choice])
    if User_choice == 0 and Computer_choice == 2:
        print("you win")
    elif Computer_choice == 0 and User_choice == 2:
        print("you lose")
    elif Computer_choice == User_choice:
        print("its a draw")
    elif User_choice < Computer_choice:
        print("you lose")
    elif Computer_choice > User_choice: 
        print("you lose")
    else:
        print("Restart!!")