import random
Namestring = input("Enter your names seperated by a comma. ")
names = Namestring.split(",")
print(names)

random_name = random.choice(names)
print(f"{random_name} will pay the bills")
