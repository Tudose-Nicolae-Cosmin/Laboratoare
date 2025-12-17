import random

print("JOC: GHICESTE NUMARUL (1-100)")
print("Ai 10 incercari")

# generare numar random
numar = random.randint(1, 100)
incercari_ramase = 10
ghicire = -1

while incercari_ramase > 0:

    print(f"\nVieti ramase: {incercari_ramase}")
    text_introdus = input("Introdu un numar intre 1 si 100: ")

    # verificare input
    if not text_introdus.isdigit():
        print("Nu ai introdus un numar valid")
        continue


    ghicire = int(text_introdus)


    if ghicire < 1 or ghicire > 100:
        print("Nu ai introdus un numar valid din range-ul [1,100]")
        continue


    if ghicire == numar:
        print(f"BRAVO! Ai ghicit numarul {numar}!")
        break

    elif ghicire < numar:
        print("Prea mic")
        incercari_ramase = incercari_ramase - 1

    else:
        print("Prea mare")
        incercari_ramase = incercari_ramase - 1



if ghicire != numar:
    print(f"Nu mai ai vieti. Numarul era: {numar}")