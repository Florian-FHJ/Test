Iterationen = int(input("Geben Sie die Anzahl der gewünschten Iterationen ein:"))
Zwischenergebnisse = input("Zwischenergebnis anzeigen?[ja/nein]")

if Zwischenergebnisse == "nein":
    print("") #Absatz
elif Zwischenergebnisse == "ja":
    print("Zwischenergebnisse:")
else:
    print("Fehler")

Ergebnis = 0
k = 0
while k <= Iterationen:
    Ergebnis += 4*(((-1)**k)/(2*k+1))
    if Zwischenergebnisse == "ja":
        print(Ergebnis)
    k += 1
    
print("Pi:",Ergebnis)

        