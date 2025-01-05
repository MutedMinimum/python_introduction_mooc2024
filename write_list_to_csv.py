coders = []                 #leere Liste

coders.append(["Eric", "Windows", "Pascal", 10])            #fügt Unterlisten Hinzu
coders.append(["Matt", "Linux", "PHP", 2])
coders.append(["Alan", "Linux", "Java", 17])
coders.append(["Emily", "Mac", "Cobol", 9])

print(coders)







with open("coders.csv", "w") as my_file:
    for coder in coders:

        line = ""

        for value in coder:                 #Innerer Loop: Iteriert über die Werte der aktuellen Unterliste 
                                            #(z. B. "Eric", "Windows", "Pascal", 10).
            line += f"{value};"
        
        line = line[:-1]                    #Entfernen des letzten Semikolons

        my_file.write(line+"\n")            #schreibt in die Datei coders.csv, mit Zeilenumbruch
                                            #"Eric;Windows;Pascal;10\n"