# print("this program is to check whether a year is a leap year or not")
# year = int(input("enter the year you want to check: "))
# print(type(year))
def Isleap(year):
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 != 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def DaysinMonth(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    Monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if Isleap(year) and month == 2:
        return 29
    return Monthdays[month - 1]
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = DaysinMonth(year, month)
print(days)