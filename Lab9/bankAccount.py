class BankAccount:
    def __init__(self, sold_initial=0):
        self._balance = sold_initial

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
            print(f"Ai depus: {amount} lei. Sold nou: {self._balance} lei.")
        else:
            print("Eroare: Nu depui bani negativi")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance = self._balance - amount
            print(f"Ai retras: {amount} lei. Sold ramas: {self._balance} lei.")
        elif amount > self._balance:
            print("Eroare: Fonduri insuficiente!")
        else:
            print("Eroare: Nu scoti bani negativi")




sold_start = float(input("Suma de start: "))
cont = BankAccount(sold_start)

while True:
    print("\n1. Depunere | 2. Retragere | 3. Vezi Sold | 4. Iesire")
    optiune = input("Alege: ")

    if optiune == "1":
        suma = float(input("Suma de depus: "))
        cont.deposit(suma)
    elif optiune == "2":
        suma = float(input("Suma de retras: "))
        cont.withdraw(suma)
    elif optiune == "3":
        print(f"Sold curent: {cont.get_balance()} lei")
    elif optiune == "4":
        break
    else:
        print("Doar de la 1 la 4")