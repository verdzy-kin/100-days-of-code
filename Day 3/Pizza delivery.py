print("Welcome to python pizza delivery!!")
size = input("what size do you want? S, N, or L\n")
Addpeperoni = input("do you want peperoni? Y or N \n")
Extracheese = input("Do you want extra cheese? Y or N \n")
bill = 0
# if size == "S":
#     bill = 15
#     if Addpeperoni == "Y":
#         bill += 2
#         print(f"small sized pizza with peperoni amounts to ${bill}") 
#     else:
#         print(f"small sized pizza with no peperoni amounts to ${bill}")
# elif size == "L":
#     bill = 25
#     if Addpeperoni == "Y":
#         if Extracheese == "Y":
#             bill += 4
#             print(f"large pizza with peperoni and cheese amounts to ${bill}")
#         else:
#             bill +=3
#             print(f"large pizza with peperoni amounts to ${bill}")
#         bill += 3
#         print(f"large pizza with peperoni amounts to ${bill}") 
#     else:
#         print(f"large pizza amounts to ${bill}")
# elif size == "M":
#     bill = 20
#     if Addpeperoni == "Y":
#         if Extracheese == "Y":
#             bill += 4
#             print(f"medium pizza with peperoni and cheese amounts to ${bill}")
#         else:
#             bill +=3
#             print(f"medium pizza with peperoni amounts to ${bill}")
#     else:
#         print(f"medium pizza amounts to ${bill}")
# else:
#     print("follow instructions")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("follow instructions")

if Addpeperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if Extracheese == "Y":
    bill += 1


print(f"your bill is: ${bill}")