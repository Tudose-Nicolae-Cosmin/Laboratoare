def filter_lines(fisier_intrare, fisier_iesire, key):
    try:
        f_in = open(fisier_intrare, "r")
        randuri = f_in.readlines()
        f_in.close()

        f_out = open(fisier_iesire, "w")

        for rand in randuri:
            if key in rand:
                f_out.write(rand)

        f_out.close()
        print(f"Gata, liniile cu '{key}' s-au scris in {fisier_iesire}")

    except FileNotFoundError:
        print("Eroare: Fisierul nu exista")



cuvant = input("Introdu cheia: ")

filter_lines("input2.txt", "filtered.txt", cuvant)