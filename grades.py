grades = {}

with open("grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", n)