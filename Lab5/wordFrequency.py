def word_frequency(text):
    text = text.lower()

    semn = ".,!?;:"
    text_clar = ""

    for caracter in text:
        if caracter not in semn:
            text_clar = text_clar + caracter

    lista_cuv = text_clar.split()

    rezultat = {}

    for cuvant in lista_cuv:
        if cuvant in rezultat:
            rezultat[cuvant] = rezultat[cuvant] + 1
        else:
            rezultat[cuvant] = 1

    return rezultat


text_test = input("Text: ")
print(word_frequency(text_test))