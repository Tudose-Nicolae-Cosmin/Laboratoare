def unique_pair_sum(numere, tinta):
    perechi_gasite = set()

    for i in range(len(numere)):
        for j in range(i + 1, len(numere)):
            numar1 = numere[i]
            numar2 = numere[j]

            if numar1 + numar2 == tinta:
                if numar1 <= numar2:
                    pereche = (numar1, numar2)
                else:
                    pereche = (numar2, numar1)

                perechi_gasite.add(pereche)

    return perechi_gasite


intrare = input("Introdu numerele: ")
lista_numere = []
for x in intrare.split():
    lista_numere.append(int(x))

tinta_input = int(input("Introdu valoarea: "))

rezultat = unique_pair_sum(lista_numere, tinta_input)
print("Perechi gasite:", rezultat)