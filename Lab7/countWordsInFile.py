def count_words_in_file(nume_fisier):
    try:
        f = open(nume_fisier, "r")
        continut = f.read()
        f.close()

        lista_cuvinte = continut.split()
        rezultat = len(lista_cuvinte)

        return rezultat

    except FileNotFoundError:
        return "Eroare: Fisierul nu se gaseste"


nume = input("Introdu numele fisierului: ")

numar_cuvinte = count_words_in_file(nume)

print("Numar cuvinte:")
print(numar_cuvinte)