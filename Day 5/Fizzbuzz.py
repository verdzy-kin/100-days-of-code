for number in range (0, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FIZZBUZZ")
    elif number % 3 == 0:
        print("FIZZ")
    elif number % 5 == 0:
        print("BUZZ")
    else:
        print(number)
