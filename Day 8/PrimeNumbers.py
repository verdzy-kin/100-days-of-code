def Primechecker(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime == True:
        print("It's a prime number")
    else:
        print("it's not a prime number")
prime = int(input("enter a number to check: "))
Primechecker(prime)