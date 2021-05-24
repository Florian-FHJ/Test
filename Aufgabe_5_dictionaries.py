woerterbuch_deutsch = {"Apfel": "apple",
                       "Birne": "pear",
                       "Kirsche": "cherry",
                       "Melone": "melon",
                       "Marille": "apricot",
                       "Pfirsich": "peach",
                       }

woerterbuch_englisch = {"apple":"Apfel",
                       "pear": "Birne",
                       "cherry":"Kirsche",
                       "melon":"Melone",
                       "apricot":"Marille",
                       "peach": "Pfirsich",
                       }


while True:
    try:
        eingabe = input("Welchen Begriff wollen Sie übersetzen? ")
        print(woerterbuch_deutsch[eingabe],"[EN]")
        break
             
    except KeyError:
        try:
            print(woerterbuch_englisch[eingabe],"[DE]")
            break
        
        except KeyError:
            print("Begriff konnte nicht gefunden werden.")
       



         

