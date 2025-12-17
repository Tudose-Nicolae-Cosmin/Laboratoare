def is_palindrome(cuvant):
    cuvant = cuvant.lower()

    cuvant_invers = ""

    for litera in cuvant:
        cuvant_invers = litera + cuvant_invers

    if cuvant == cuvant_invers:
        return True
    else:
        return False


text = input("Introdu un cuvant: ")

if text.isalpha():
    if is_palindrome(text):
        print("Este palindrom")
    else:
        print("Nu este palindrom")
else:
    print("Introdu doar litere")