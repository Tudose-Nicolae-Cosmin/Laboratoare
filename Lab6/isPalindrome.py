def is_palindrome(text):
    text = text.lower()
    text_curat = ""
    for ch in text:
        if ch != " ":
            text_curat = text_curat + ch

    text_inv = ""
    for i in range(len(text_curat) - 1, -1, -1):
        text_inv = text_inv + text_curat[i]

    if text_curat == text_inv:
        return True
    else:
        return False

text_utilizator = input("Introdu text: ")

if is_palindrome(text_utilizator):
    print("True")
else:
    print("False")