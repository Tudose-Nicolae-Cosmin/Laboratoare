numar = int(input("Introduceti un numar: "))
if numar < 2:
    print("Numarul nu este prim")
else:
    este_prim = True

    for i in range(2, numar):
        if numar % i == 0:
            este_prim = False
            break

    if este_prim:
        print("Numarul este prim")
    else:
        print("Numarul nu este prim")