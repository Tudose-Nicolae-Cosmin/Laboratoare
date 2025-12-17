text = input("Introdu numarul n: ")

if text.isdigit():
    n = int(text)

    if n <= 0:
        print("Introdu un numar mai mare decat 0.")
    else:
        print(f"Numerele impare pana la {n} sunt:")
        for i in range(1, n + 1, 2):
            print(i)

else:
    print("Introdu un numar natural")