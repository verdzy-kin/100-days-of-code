# print("this program is to check whether a year is a leap year or not")
year = int(input("enter the year you want to check: "))
print(type(year))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print("\n")
    else:
        print("\n")
else:
    print(f"{year} is not a leap year")