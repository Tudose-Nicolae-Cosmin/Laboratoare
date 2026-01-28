inventar = {}

def adauga_produs():
    try:
        nume = input("Nume produs: ").lower()
        cantitate = int(input("Cantitate: "))
        if cantitate < 0:
            print("Eroare: Cantitatea nu poate fi negativa")
            return

        if nume in inventar:
            inventar[nume] += cantitate
        else:
            inventar[nume] = cantitate
        print(f"Produs adaugat. Stoc nou: {nume}: {inventar[nume]}")
    except ValueError:
        print("Eroare: Nu ai intordus bine")


def cauta_produs():
    nume = input("Introdu numele produsului cautat: ").lower()
    if nume in inventar:
        print(f"Produs gasit: {nume} -> Stoc: {inventar[nume]}")
    else:
        print("Eroare: Produsul nu exista")


def actualizeaza_stoc():
    try:
        nume = input("Nume produs pentru actualizare: ").lower()
        if nume not in inventar:
            raise KeyError

        noua_cantitate = int(input("Introdu noua cantitate: "))
        if noua_cantitate < 0:
            print("Eroare: Cantitatea nu poate fi negativa")
            return

        inventar[nume] = noua_cantitate
        print(f"Stoc actualizat pentru {nume}: {inventar[nume]}")
    except KeyError:
        print("Eroare: Produsul nu a fost gasit in baza de date")
    except ValueError:
        print("Eroare: Introdu un numar valid pentru cantitate")



while True:
    print("\n--- GESTIUNE INVENTAR ---")
    print("1. Adauga stoc")
    print("2. Cauta produs")
    print("3. Actualizeaza cantitate")
    print("4. Iesire")

    optiune = input("Alege optiunea: ")

    if optiune == "1":
        adauga_produs()
    elif optiune == "2":
        cauta_produs()
    elif optiune == "3":
        actualizeaza_stoc()
    elif optiune == "4":
        print("Program incheiat.")
        break
    else:
        print("Optiune invalida!")