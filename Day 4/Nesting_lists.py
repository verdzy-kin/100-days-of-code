row1 = ["OIP[1].jpg", "OIP[1].jpg", "OIP[1].jpg"]
row2 = ["OIP[1].jpg", "OIP[1].jpg", "OIP[1].jpg"]
row3 = ["OIP[1].jpg", "OIP[1].jpg", "OIP[1].jpg"]
map = [row1, row2, row3]
position = input("where do you want to place the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
map[vertical - 1][horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")
# print(map)