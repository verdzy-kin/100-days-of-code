print("Welcome to the rollercoaster!!")
height = float(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster! ")
    age = int(input("enter your age: "))
    if age < 12:
        bill = 5
        print("please pay $5. ")
    elif age <= 18:
        bill = 7
        print("please pay $7.")
    elif age >= 45 and age <= 55:
        print("you have a free ride")
    else:
        bill = 12
        print("please pay $12.")
    photo = input("Do you want a photo taken? Y or N \n")
    if photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("sorry, you have to grow taller to be able to ride!!")
