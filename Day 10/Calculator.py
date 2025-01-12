from Art import logo
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def Calculator():
    print(logo)

    num1 = float(input("what's the first number?: "))
    for sign in operations:
        print(sign)
    decision = True
    while decision:
        Operationsymbol = input("pick an operation: ")
        num2 = float(input("Enter next number?: "))
        Calculation_function = operations[Operationsymbol]
        answer = Calculation_function(num1, num2)
        print(f"{num1} {Operationsymbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}: ") == "y":
            num1 = answer
        else:
            decision = False
            Calculator()
Calculator()