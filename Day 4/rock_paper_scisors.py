print("WELCOME TO THE ROCK PAPER SCISSORS GAME!!!\n\n")
rock = '''

'''
scissors = '''

'''
paper = '''

'''
Gameimages = [rock, paper, scissors]
import random
Computer_choice = random.randint(0,2)
User_choice = int(input("type 0 for Rock, 1 for paper, 2 for scissors.\n"))
print(Gameimages[User_choice])
print(f"Computer chose: ")
print(Gameimages[Computer_choice])
if Computer_choice >= 3 or User_choice < 0:
    print("you typed an invalid number. you lose")
elif User_choice == 0 and Computer_choice == 2:
    print("you win")
elif Computer_choice == 0 and User_choice == 2:
    print("its a draw")
elif User_choice < Computer_choice:
    print("you lose")
elif Computer_choice > User_choice: 
    print("you lose")


# if Randomitem == 0:
#     if decision == 0:
#         print(f"Computer chose: {Randomitem},\n\n" + rock)
#         print("you draw!!!")
#     elif decision == 1:
#         print(f"Computer chose: {Randomitem},\n\n" + paper)
#         print("you win!!!")
#     elif decision == 2:
#         print(f"Computer chose: {Randomitem},\n\n" + paper)
#         print("you lose!!!")
#     # else:
#     #     print("follow instructions")
# elif Randomitem == 1:
#     if decision == 0:
#         print(f"Computer chose: {Randomitem},\n\n" + rock)
#         print("you lose!!!")
#     elif decision == 1:
#         print(f"Computer chose: {Randomitem},\n\n" + paper)
#         print("you draw!!!")
#     elif decision == 2:
#         print(f"Computer chose: {Randomitem},\n\n" + scissors)
#         print("you win!!!")
#     # else:
#     #     print("follow instructions")
# elif Randomitem == 2:
#     if decision == 0:
#         print(f"Computer chose: {Randomitem},\n\n" + rock)
#         print("you win!!!")
#     elif decision == 1:
#         print(f"Computer chose: {Randomitem},\n\n" + paper)
#         print("you lose!!!")
#     elif decision == 2:
#         print(f"Computer chose: {Randomitem},\n\n" + scissors)
#         print("you draw!!!")
#     # else:
#     #     print("follow instructions")
# # else:
# #     print("Wrong entry start over!!!")
