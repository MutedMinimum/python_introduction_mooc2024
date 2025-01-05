names = {}

with open("combining_employees.csv") as new_file:

    for line in new_file:
        parts = line.split(';')                         #entfernen der Trennzeichen

        if parts[0] == "pic":
            continue                                    #überspringen des Headers

        names[parts[0]] = parts[1]                      #hinzufügen der Einträge

#{
# '080488-123X': 'Pekka Mikkola', 
# '290274-044S': 'Liisa Marttinen', 
# '010479-007Z': 'Arto Vihavainen', 
# '010499-345K': 'Leevi Hellas'
#}



salaries = {}

with open("combining_salaries.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "pic":
            continue
        salaries[parts[0]] = int(parts[1]) + int(parts[2])
#{
# '080488-123X': 3300, 
# '290274-044S': 4350, 
# '010479-007Z': 2500
#}

print("incomes:")

for pic, name in names.items():
    if pic in salaries:
        salary = salaries[pic]
        print(f"{name:16} {salary} euros")          #Der Ausdruck :16 im Formatstring {name:16} sorgt dafür,
                                                    #dass der Wert der Variablen name in einer Spalte mit einer 
                                                    # festen Breite von 16 Zeichen ausgegeben wird. Es ist eine 
                                                    # Möglichkeit, Text in einer Tabelle auszurichten.
    else:
        print(f"{name:16} 0 euros")