text = input("Introdu valorile separate prin ,: ")

lista_temporara = text.split(',')

lista_fin = []
for element in lista_temporara:
    lista_fin.append(element.strip())


tupla = tuple(lista_fin)

print(f"Tupla creata este: {tupla}")


val = input("Valoare cautata: ")

if val in tupla:
    poz = tupla.index(val)
    print(f" Valoarea '{val}' se gaseste la indexul {poz}")
else:
    print(f"Valoarea '{val}' nu exista in tupla")