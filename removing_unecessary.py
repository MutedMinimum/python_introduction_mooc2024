#first; last
#Paul; Python
#Jean; Java
#Harry; Haskell


last_names = []

with open("removing_unnecessary.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        

        if parts[0] == "first":                     #überspringen der ersten Zeile/Header
            continue
        
        last_names.append(parts[1].strip())         #hinzufügen der Namen, strip entfernt alles unnörtige
                                                    #(den whitespace und \n)
    
    print(last_names)


test1 = " teststring "

print(test1.rstrip())           #entfernen aller nichtdruckbarer Zeichen links des strings
# teststring#

print(test1.lstrip())
#teststring #                   #beachte hier am ende ein unsichtbarer whitespace

print(test1.strip())            #entfernen aller nichtdruckbarer Zeichen links und rechts des Strings
#teststring#