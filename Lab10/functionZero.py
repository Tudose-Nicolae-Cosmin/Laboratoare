def imp(a, b):
    try:
        rezultat = a / b
        return rezultat
    except ZeroDivisionError:
        return "nu imparti la 0"


try:
    x = float(input("x: "))
    y = float(input("y: "))

    print("x/y=:", imp(x, y))
except ValueError:
    print("doar cifre")