# 1) Funktion zur Eingabe des Befehls
# 2) Funktion zur Eingabe des Suchbegriffs bzw. Wortes
# 3) Funktion zur Suche
# 4) Funktion zur Ausgabe

def eingabe_befehl():
    korrekt = False
    while korrekt == False:
        taste = input("Eingabe Befehl (Ab[F]rage, [E]rgänzung: ")
        taste = taste.upper()
        if taste == "F":
            korrekt = True
            return taste
        elif taste == "E":
            korrekt = True
            return taste

def ergaenzung(neues_wort):

#while ...

    kommando = eingabe_befehl()
    
    if kommando == "F":
        suchwort = eingabe_suchwort()
        ergebnis = suche(suchwort)
        ausgabe(ergebnis)
        
    elif kommando == "E":
        wort = eingabe_suchwort()
        ergaenzung(wort)
        
    #elif ...
    
    #else ...
        
# Sequentielle Datentypen:
#
# 1) Strings / Zeichenketten
# -> Objekte / Klasse
# --> Methoden (Funktionen zur Manipulation von Klassen-Eigenschaften)
#

#zeichenkette = "Ich bin ein string"
#print(zeichenkette)
#großbuchstaben = zeichenkette.upper()
#print(großbuchstaben)
#kleinbuchstaben = großbuchstaben.lower()
#print(kleinbuchstaben)

#buchstabe = zeichenkette[2] # Meinung 1: 'c', Meinung 2: 'h', Meinung 3: 'bin'
#print(buchstabe)
#Zählung von sequentillen (Index) Elementen beginnt IMMER mit 0!
#print(zeichenkette[3])

# 2) Liste
#meine_liste = ["ich bin", "ein", "string in einer", "liste!"]
#print(meine_liste[2])

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

max = len(woerterbuch_deutsch)

running = True
while running:
    
    auswahl = input("Welchen Befehl möchten Sie ausführen? \n[E]Einfügen \n[L]Löschen \n[A]Abfragen ")

    if auswahl == 'E' or auswahl == 'e':
        Wort = input("Welches Wort möchten Sie einfügen?")
        woerterbuch_deutsch.append(Wort)
        print("Einfügen:", woerterbuch_deutsch)
    #Einfügen
    elif auswahl == 'L' or auswahl ==  'l':
        Wort = input("Welches Wort möchten Sie löschen?")
        woerterbuch_deutsch.remove(Wort)
        print("Löschen:", woerterbuch_deutsch)
    #löschen
    else: #Standardvorgang -> immer mit dem geringsten Risiko
        print("Abfragen:")
    #Abfrage
    


# 1) Eingabe Suchbegriff (deutsch)
# 2) Bestimmung der Gesamtanzahl der Elemente (=maximaler Index)
# 3) Schleife: Vergleich Eingabe mit jew. Listenelement
# 4) Wenn Element gefunden -> Index speichern
# 5) Zugriff auf Listenelement[Index] in Liste (englisches Woerterbuch)

    Begriff = input("Geben Sie einen Begriff ein: ")

    #print(Begriff.upper())

    index = 0 

    while index < max:
        if Begriff == woerterbuch_deutsch[index]:
            print("Übersetzung von deutsch ins englische lautet:", woerterbuch_english[index])
            break
        if Begriff == woerterbuch_english[index]:
            print("Übersetzung von englisch ins deutsche lautet:", woerterbuch_deutsch[index])
            break
        index += 1
    if index == max:
        print("Begriff nicht gefunden.")
        
