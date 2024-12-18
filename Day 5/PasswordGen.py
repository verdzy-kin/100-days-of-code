import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '&', '*', '+', '=']

print("Welcome to the Password Generator!!")
Nrletters = int(input("how many letters do you want in your password? \n"))
Nrnumbers = int(input("how many numbers would you like to be in your password? \n"))
Nrsymbols = int(input("how many symbols would you like? \n"))

passwordlist = []
for char in range(1, Nrletters + 1):
    passwordlist.append(random.choice(letters))
for char in range(1, Nrsymbols + 1):
    passwordlist.append(random.choice(symbols))
for char in range(1, Nrnumbers + 1):
    passwordlist.append(random.choice(numbers))

random.shuffle(passwordlist)
password = ""
for char in passwordlist:
    password += char
print(f"your password is {password}\n")