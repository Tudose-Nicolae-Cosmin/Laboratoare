text = input("Introdu numerele separate prin ,: ")

try:
    lista_text = text.split(',')
    lista_numere = []

    for element in lista_text:
        numar = int(element)
        lista_numere.append(numar)


    if len(lista_numere) > 0:
        print(f"Lista ta este: {lista_numere}")
        print(f"Maximul este: {max(lista_numere)}")
        print(f"Minimul este: {min(lista_numere)}")
    else:
        print("Lista este goala")

except ValueError:
    print("Introdu doar numere separate prin virgula")