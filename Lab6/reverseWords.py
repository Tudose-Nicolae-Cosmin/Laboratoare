def reverse_words(prop):
    lista_cuvinte = prop.split()

    lista_inversata = []
    for i in range(len(lista_cuvinte) - 1, -1, -1):
        cuvant = lista_cuvinte[i]
        lista_inversata.append(cuvant)

    rezultat = " ".join(lista_inversata)
    return rezultat


text = input("Introdu propozitia: ")
prop_noua = reverse_words(text)
print("Rezultat:")
print(prop_noua)