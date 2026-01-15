def reverse_lines(fisier_intrare, fisier_iesire):
    try:
        f_in = open(fisier_intrare, "r")
        randuri = f_in.readlines()
        f_in.close()

        f_out = open(fisier_iesire, "w")

        for rand in randuri:
            rand = rand.strip()
            rand_inversat = rand[::-1]
            f_out.write(rand_inversat + "\n")

        f_out.close()
        print(f"S-a facut treaba:)) {fisier_iesire}")

    except FileNotFoundError:
        print("Eroare: Fisierul nu exista")


reverse_lines("input.txt", "output.txt")