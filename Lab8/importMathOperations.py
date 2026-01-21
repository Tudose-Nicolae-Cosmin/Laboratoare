import mathOperations

try:
    x = float(input("x= "))
    y = float(input("y= "))

    s = mathOperations.adunare(x, y)
    dif = mathOperations.scadere(x, y)
    p = mathOperations.inmultire(x, y)
    c = mathOperations.impartire(x, y)

    print(f"\nRezultate pentru numerele {x} si {y}:")
    print(f"Adunare: {s}")
    print(f"Scadere: {dif}")
    print(f"Inmultire: {p}")
    print(f"Impartire: {c}")

except ValueError:
    print("Eroare: Introdu 2 numere")