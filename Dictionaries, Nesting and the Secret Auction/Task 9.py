Student_score = {
    "Rakib": 85,
    "Rifat": 89,
    "Avesheak": 95,
    "Taj": 25,
    "Antim": 86,
}
print(Student_score["Avesheak"])
print (Student_score["Taj"])
for grade in Student_score:
    if (Student_score[grade]) >= 91:
        print("OutStanding")
    elif (Student_score[grade]) >= 81:
        print("Grate")
    if (Student_score[grade]) >= 71:
        print("Good")
    else:
        print("Fail")

## Travel Log: 
