from geometry import circle, rectangle

def executa_calcule():
    try:
        print("Cerc:")
        r = float(input("Introdu raza: "))
        print(f"Aria: {round(circle.aria(r), 2)}")
        print(f"Circumferinta: {round(circle.circumferinta(r), 2)}\n")

        print("Dreptunghi")
        L = float(input("Introdu lungimea: "))
        l = float(input("Introdu latimea: "))
        print(f"Aria: {rectangle.aria(L, l)}")
        print(f"Perimetrul: {rectangle.perimetru(L, l)}")

    except ValueError:
        print("Eroare: Introdu numere")

if __name__ == "__main__":
    executa_calcule()