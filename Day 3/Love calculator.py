print("Welcome to the love calculator!")
name1 = input("what is your name? ")
name2 = input("what is your name? ")

combined = name1 + name2
Lowercase = combined.lower()

t = Lowercase.count("t")
r = Lowercase.count("r")
u = Lowercase.count("u")
e = Lowercase.count("e")
l = Lowercase.count("l")
o = Lowercase.count("o")
v = Lowercase.count("v")
e = Lowercase.count("e")

true = t + r + u + e
love = l + o + v + e

Lovescore = int(str(true) + str(love))
# print(Lovescore)

if (Lovescore < 10) or (Lovescore > 90):
    print(f"your love score is {Lovescore}, you go together ")
elif (Lovescore >= 40) and (Lovescore <= 50):
    print(f"Your love scare is {Lovescore}, you are alright together")
else:
    print(f"love score is {Lovescore}")