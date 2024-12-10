height = float(input("enter your height is m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / height ** 2, 2)

BMI = "{:.2f}".format(BMI)
print(BMI)

if float(BMI) < 18.5:
    print(f"Your BMI is {BMI} and you are underweight")
elif float(BMI) < 25:
    print(f"Your BMI is {BMI} and you have a normal weight")
elif float(BMI) < 30:
    print(f"Your BMI is {BMI} and you are overweight")
elif float(BMI) < 35:
    print(f"Your BMI is {BMI} and you are obese.")
else:
    print("You are clinically obese.")