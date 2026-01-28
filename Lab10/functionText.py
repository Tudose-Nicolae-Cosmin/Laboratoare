def suma_numere_fisier(nume_fisier):
    suma = 0
    try:
        f = open(nume_fisier, "r")

        for linie in f:
            rand = linie.strip()

            if rand:
                try:
                    numar = float(rand)
                    suma = suma + numar
                except ValueError:
                    print(f"valoarea nevalida: '{rand}'")

        f.close()
        return suma

    except FileNotFoundError:
        return "Eroare: fisierul nu a fost gasit"
    except IOError:
        return "Eroare: nu s-a putut citi"
    except Exception as e:
        return f"Alta eroare: {e}"


nume = input("Nume fisier: ")
rezultat = suma_numere_fisier(nume)

print("Suma:", rezultat)