# Aufgabe 1:
# Schreiben Sie ein Python-Programm, das
# 1) den Benutzer begrüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahl berechnet und ausgibt
# 5) die Differenz der kleineren von der größeren Zahl berechnen
# 6) das Produkt der beiden Zahlen berechnet und ausgibt
# 7) den Qoutient kleinere Zahl durch größere Zahl berechnet und ausgibt (inkl. Nachkommastellen)



print("Hallo Benutzer!")

Zahl_l_string = input("Eingabe der ersten Zahl:")
Zahl_2_string = input("Eingabe der zweiten Zahl:")

Zahl_1 = float(Zahl_l_string)
Zahl_2 = float(Zahl_2_string)

Summe = Zahl_1 + Zahl_2
print("Summe" , Summe)

Produkt = Zahl_1 * Zahl_2
print("Produkt" , Produkt)

#Differenz = kleinere Zahl - größere Zahl
if Zahl_1 > Zahl_2:
    print("Differenz" , Zahl_1 - Zahl_2)

else:
    print("Differenz" , Zahl_2 - Zahl_1)

#Quotient = kleinere Zahl / größere Zahl
if Zahl_1 < Zahl_2:
    print("Quotient: " , Zahl_1 / Zahl_2)
    
else:
    print("Quotient: " , Zahl_2 / Zahl_1)




