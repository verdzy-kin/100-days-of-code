Programmingdictionary = {
    "Bug": "a type of insect", 
    "Daisy": "flower menaing eye of the night"
}

Programmingdictionary["Loop"] = "the action of doing something over and over."
# Programmingdictionary = {}
# print(Programmingdictionary)
for key in Programmingdictionary:
    print(Programmingdictionary[key])

studentscores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 10,
}
Studentgrades = {}

for student in studentscores:
    score = studentscores[student]
    if score > 90:
        Studentgrades[student] = "Outstanding"
    elif score > 80:
        Studentgrades[student] = "Exceeds expectations"
    elif score > 70:
        Studentgrades[student] = "Acceptable"
    else:
        Studentgrades[student] = "Fail"
print(Studentgrades)