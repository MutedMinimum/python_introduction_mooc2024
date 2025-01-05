my_dictionary = {}                          #erzeugen eines leeren dctionarys

                                            #dictionarys bestehen aus ["keys"] und "values"
my_dictionary["apina"] = "monkey"           #hinzufügen von Einträgen bzw. key/value Paaren
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"



print(my_dictionary)                        #my_dictionary hat 3 key/value Paare

print(len(my_dictionary))                   #len gibt deswegen den Wert 3 wieder

print(my_dictionary["apina"])               #der value der mit dem key "apina" verbunden ist



#word = input("Please type in a word: ")             #usereingabe für ein Wort
word = "hardcode"

if word in my_dictionary:                           #if Funktion sucht im Dictionary nach dem key word
    print("Translation: ", my_dictionary[word])     #wenn word dem key entspricht wird der value ausgegeben
else:
    print("Word not found")



### WAS KANN IN EINEM DICTIONARY GESPEICHERT WERDEN? ###


#string / integer paar

results = {}                    #neues dictionary, kein Inhalt

results["Mary"] = 4             #hinzufügen von key/value Paaren
results["Alice"] = 5
results["Larry"] = 2

lists = {}

lists[5] = [1, 2 , 3]           #hinzufügen von key werten 5, 42, 100 mit values in Listenform
lists[42] = [5, 4, 5, 4, 5]
lists[100] = [5, 2, 3]

lists[100].append(2)            #hinzufügen zur Liste 100 den int-Wert 2

lists[100].pop(0)               #entnehme der Liste 100 den Indexwert 0, also den ersten! = 5

lists[100].remove(2)

print(lists[100])

lists[100] = [5, 2, 3]
lists[101] = [5, 2, 3]
 
print(lists[100])               #key existiert bereits und ersetzt den bisherigen Wert
print(lists[101])               #doppelte values funktionieren / doppele keys nicht!

### MERKE: Keys are immutable -  values are mutable!



### TRAVERSING A DICTIONARY ###


my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

for key in my_dictionary:                               #einzelne ausgabe von keys und values nacheinander
    print(key)
    print(my_dictionary[key])


print("method .item:")


for key, value in my_dictionary.items():                #einzelne ausgabe von keys und values nacheinander
    print(key)                                          #.items() methode
    print(value)



### ZÄHLEN VON WÖRTERN IN EINER LISTE ###


word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

def counts(my_list):

    words = {}

    for word in my_list:
        
        if word not in words:
            words[word] = 0
        else:
            words[word] += 1

    return words


print(counts(word_list))