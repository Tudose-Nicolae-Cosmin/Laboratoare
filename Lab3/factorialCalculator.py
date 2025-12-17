def factorial(n):
    if n == 0:
        return 1

    produs = 1
    for i in range(1, n + 1):
        produs = produs * i

    return produs

text = input("Introdu un numar intreg: ")


if text.isdigit():
    n = int(text)

    rezultat = factorial(n)

    print(f"Factorialul lui {n} este: {rezultat}")

else:
    print("Introdu un numar natural")