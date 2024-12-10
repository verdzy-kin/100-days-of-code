print("wekcome to the tip calculator")
Bill = float(input("what is the total bill: $"))
tip = int(input("what percentage tip would you like to give? 10, 12 or 15: $"))
Numofpeople = int(input("how many people are to split the bill? "))
Percentagetipped = tip / 100
Totaltipped = Bill * Percentagetipped
Totalbill = Bill + Totaltipped
Billperperson = Totalbill / Numofpeople

Finalamount = round(Billperperson, 2)
Finalamount = "{:.2f}".format(Billperperson)
print(f"Each person is to pay ${Finalamount}")
