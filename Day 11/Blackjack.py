from Art import logo
print(logo)

import random

def dealcard():
    """returns a random card from deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def Calculatescore(cards):
    """takes a lost of cards and returns the score calculated."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
        
    return sum(cards)

Usercards = []
Computercards = []
Isgameover = False
while not Isgameover:
    for _ in range(2):
        Usercards.append(dealcard())
        Computercards.append(dealcard())

    Userscore = Calculatescore(Usercards)
    Computerscore = Calculatescore(Computercards)
    print(f"Your cards: {Usercards}  current score: {Userscore}")
    print(f"Computer first card: {Computercards[0]}")
    if Userscore == 0 or Computerscore == 0 or Userscore > 21:
        Isgameover = True
    else:
        Usershoulddeal = input("Type 'y' to get another card otherwise type 'n' to pass: ")
        if Usershoulddeal == "y":
            Usercards.append(dealcard())
        else:
            Isgameover == True 

while Computerscore != 0 and Computerscore < 17:
    Computercards.append(dealcard())
    Computerscore = Calculatescore(Computercards)
    