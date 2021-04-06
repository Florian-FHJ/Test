# Schleifen-/Zählvariable: i, j, k
#Addieren Sie in einer Schleife(!) die Zahlen von 1 bis 100 und geben Sie das Ergebnis aus

#counter = 10
#while counter >= 0:
    #print(counter)
    #counter = counter - 1 #alt.: counter -= 1

Ergebnis = 0
x = 1
while x <= 100:
    Ergebnis += x
    x += 1
    print(Ergebnis)