import math

try:
    numar_text = input("Introdu numar: ")
    numar = float(numar_text)

    unghi_text = input("Introdu unghi: ")
    unghi = int(unghi_text)

    if numar < 0:
        print("Radacina se calculeaza din numar pozitiv")
    else:
        radacina = math.sqrt(numar)
        print(f"Radacina lui {numar} este {radacina}")

    if numar < 0:
        print("Factorialul se calculeaza din numar pozitiv")
    else:
        numar_intreg = int(numar)
        fact = math.factorial(numar_intreg)
        print(f"Factorialul lui {numar_intreg} este {fact}")

    unghi_radiani = math.radians(unghi)
    sinus = math.sin(unghi_radiani)
    print(f"Sinusul unghiului de {unghi} grade este {round(sinus, 2)}")

except ValueError:
    print("Eroare: Doar cifre")

except Exception as e:
    print(f"Eroare: {e}")