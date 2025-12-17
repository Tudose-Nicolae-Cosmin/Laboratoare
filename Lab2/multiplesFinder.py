text_x = input("Introdu numărul x (de inceput): ")
text_y = input("Introdu numărul y (pana unde se duce): ")


if text_x.isdigit() and text_y.isdigit():

    x = int(text_x)
    y = int(text_y)

    if x > y:
        x, y= y, x

    if x == 0:
        print("0 nu e un numar valid")

    else:
        print(f"Multiplii lui {x} mai mici decat {y} sunt:")
        for numar in range(x, y, x):
            print(numar)

else:
    print("Introdu doar numere naturale pozitive.")