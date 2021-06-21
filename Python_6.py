woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_englisch = ["apple", "pear", "cerry", "melon", "apricot", "peach"]

#Funktionen
def Wort_hinzufügen(Deutscher_Begriff, Englischer_Begriff):   
    woerterbuch_deutsch.append(Deutscher_Begriff)
    woerterbuch_englisch.append(Englischer_Begriff)
    print("Das Wort wurde hinzugefügt.")
        
def Wort_löschen():
    gelöschter_Begriff = input ("Welches Wort möchten Sie löschen?: ")
    K = 0
    while K < len(woertebuch_deutsch):
        if gelöschter_Begriff == woerterbuch_deutsch[K]:
            woerterbuch_englisch.remove(woerterbuch_englisch[K])          
            woerterbuch_deutsch.remove(gelöschter_Begriff)
            print("Das Wort wurde gelöscht")
            break
            
        if gelöschter_Begriff.lower() == woerterbuch_englisch[K]:
            woerterbuch_deutsch.remove(woerterbuch_deutsch[K])
            woerterbuch_englisch.remove(gelöschter_Begriff)
            print("Das Wort wurde gelöscht")
            break
        
        K += 1
            
        if K == len(woerterbuch_deutsch):
            print("nicht gefunden!")
def Wort_abfragen(Begriff):
    
    Index = 0
    while Index < len(woerterbuch_deutsch):
        if Begriff.lower() == woerterbuch_deutsch[Index].lower():
            print("Übersetzung von Deutsch in Englisch:",woerterbuch_englisch[Index])
            break
        if Begriff.lower() == woerterbuch_englisch[Index].lower():
            print("Übersetzung von Englisch in Deutsch: ",woerterbuch_deutsch[Index])
            break
        Index += 1      
    if Index == len(woerterbuch_deutsch):
        print("nicht gefunden")
            
def Eingabe():
    while True:
        Abfrage = input("Befehl? [E]infügen, [L]öschen, [A]bfragen, [B]eenden: ")
        if Abfrage.lower() == "e" or  Abfrage.lower() =="l" or Abfrage.lower() =="a" or Abfrage.lower() =="b":
            return Abfrage.lower()
        else:
            print("Falsche Eingabe")
    
    
while True:
    Abfrage = Eingabe()
    if Abfrage == "e":
        Deutscher_Begriff = input ("Neues deutsches Wort:")
        Englischer_Begriff = input ("Übersetzung ins Englische:")
        Wort_hinzufügen(Deutscher_Begriff, Englischer_Begriff)
        
    elif Abfrage == "a":
        Begriff = input("Welches Wort möchten Sie übersetzen?: ")
        Wort_abfragen(Begriff)
    elif Abfrage == "l":
        Wort_löschen()
    elif Abfrage == "b":
        break