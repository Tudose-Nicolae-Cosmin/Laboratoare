text = input("Introdu numerele separate prin ,: ")

try:
    lista_text = text.split(',')
    lista_numere = []
    for element in lista_text:
        lista_numere.append(int(element.strip()))

    lista_unica = []

    for numar in lista_numere:
        if numar not in lista_unica:
            lista_unica.append(numar)

    print(f"Lista originala: {lista_numere}")
    print(f"Lista fara duplicate: {lista_unica}")

except ValueError:
    print("Introdu doar numere intregi")