text = input("Introdu scorul (0-100): ")

if text.isdigit():

    scor = int(text)

    if scor > 100:
        print("Scorul nu este valid")
    else:
        if scor >= 90:
            print("Nota A")
        elif scor >= 80:
            print("Nota B")
        elif scor >= 70:
            print("Nota C")
        elif scor >= 60:
            print("Nota D")
        else:
            print("Nota F")

else:
    print("Valoarea introdusa este invalida")