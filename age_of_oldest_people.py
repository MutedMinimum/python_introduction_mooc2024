people = []                 #leere Liste um den Inhalt einer Datei zu speichern
                            #somit muss man eine Datei später nicht mehrfach mit dem open
                            #befehl öffnen

with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(";")

        people.append((parts[0], int(parts[1]), parts[2]))

for person in people:
    print("Name:", person[0])

    


#den ältesten finden

#people Liste
#[('Peter', 40, 'Helsinki\n'), ('Emily', 34, 'Espoo\n'), ('Eric', 42, 'London\n'), ('Adam', 100, 'Amsterdam\n'), ('Alice', 58, 'Paris')]

age_of_oldest = -1

for person in people:

    name = person[0]
    age = person[1]


    if age > age_of_oldest:

        age_of_oldest = age

        oldest = name

print(oldest, age_of_oldest)
    
