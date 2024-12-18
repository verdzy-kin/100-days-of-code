studentscores = input("input a list of student scores: ").split(",")
for n in range(0, len(studentscores)):
    studentscores[n] = int(studentscores[n])
print(studentscores)
highestscore = 0
for score in studentscores:
    if score > highestscore:
        highestscore = score
print(f"the highest score is: {highestscore}")
