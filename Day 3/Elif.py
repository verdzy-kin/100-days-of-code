print("Welcome to the rollercoaster!!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster! ")
    age = int(input("enter your age: "))
    if age < 12:
        print("please pay $5. ")
    elif age < 18:
        print("please pay $7.")
    else:
        print("please pay $12.")
else:
    print("sorry, you have to grow taller to be able to ride!!")