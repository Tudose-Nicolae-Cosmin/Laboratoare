def inverted_index(lista_documente):
    index = {}

    for i in range(len(lista_documente)):
        document_curent = lista_documente[i]

        cuvinte = document_curent.split()

        for cuvant in cuvinte:
            cuvant = cuvant.lower()

            if cuvant in index:
                index[cuvant].add(i)
            else:
                index[cuvant] = {i}

    return index

documente = []
while True:
    linie = input(f"Document [{len(documente)}]: ")

    if linie.lower() == 'gata': #ca sa termini de citit
        break

    documente.append(linie)

rezultat = inverted_index(documente)
if len(documente) > 0:
    print("Dictionarul:")
    for cheie, valoare in rezultat.items():
        print(f"{cheie}: {valoare}")
else:
    print("Nu ai introdus nimic")