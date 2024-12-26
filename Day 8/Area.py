import math
def Paintcalc(Height, Width, cover):
    area = Height * Width
    cans = math.ceil(area / cover)
    print(f"You'll need {cans}cans")
test_h = int(input("Height of the room: "))
test_w = int(input("Width of the room: "))
coverage = 5
Paintcalc(test_h, test_w, coverage)