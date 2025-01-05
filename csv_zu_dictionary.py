#Paul;5;4;5;3;4;5;5;4;2;4
#Beth;3;4;2;4;4;2;3;1;3;3
#Ruth;4;5;5;4;5;5;4;5;4;4

grades = {}                                      #initialisierung dictionary       

with open("grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")            #.csv daten werden umgewandelt für dictionary
        parts = line.split(";")                  #.csv daten werden umgewandelt für dictionary

        name = parts[0]                          #namen sind immer an erster stelle deswegen [0]
        grades[name] = []                        #initialisieren einer Liste für die Noten

        for grade in parts[1:]:                  #alle werte ab index 1 bis unendlich / ende
            grades[name].append(int(grade))      #die Noten werden dem Namen hinzugefügt

print(grades)

#dictionary: {'Paul': [5, 4, 5, 3, 4, 5, 5, 4, 2, 4], 
# 'Beth': [3, 4, 2, 4, 4, 2, 3, 1, 3, 3], 'Ruth': [4, 5, 5, 4, 5, 5, 4, 5, 4, 4]}


for name, grade_list in grades.items():

    best = max(grade_list)
    average = sum(grade_list) / len(grade_list)

    print(f"Name: {name}, best grade: {best}, average: {float(average)}")