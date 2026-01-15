def run_length_encoding(text):
    if not text:
        return ""

    rezultat = ""
    contor = 1

    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            contor = contor + 1
        else:
            rezultat = rezultat + text[i] + str(contor)
            contor = 1

    rezultat = rezultat + text[-1] + str(contor)

    return rezultat


text = input("Introdu text: ")
print("Rezultat:", run_length_encoding(text))