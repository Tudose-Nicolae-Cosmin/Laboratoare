import math

def distance(x1, y1, x2, y2):
    x = (x2 - x1) ** 2
    y = (y2 - y1) ** 2

    return math.sqrt(x + y)

while True:
    try:
        x1 = float(input("Introdu x1: "))
        y1 = float(input("Introdu y1: "))
        x2 = float(input("Introdu x2: "))
        y2 = float(input("Introdu y2: "))

        dist = distance(x1, y1, x2, y2)

        print(f"Distanta dintre puncte este: {dist:.2f}")
        break

    except ValueError:
        print("Introdu doar numere reale")