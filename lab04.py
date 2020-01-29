'''
Lab 4: Grades
Assignment by Lionel Di Giacomo
1/22/2020
'''

score = int(input("What is your numeric grade (0-100)?: "))

prefix = "You got a "
if score > 110:
    prefix = "Are you cheating... ? Well, until we find out, you get an "
    grade = "A+"
elif score >= 100:
    prefix = "WOW!! You earned a perfect "
    grade = "A+"
elif score >= 90:
    prefix = "Congratulations! You got an "
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    prefix = "Oof... you got an "
    grade = "F"

if grade != "F" and grade != "A+":
    gradeMod = int(str(score)[-1])
    if gradeMod <= 2:
        grade = grade + "-"
    elif gradeMod >= 8:
        grade = grade + "+"

print(prefix + grade)