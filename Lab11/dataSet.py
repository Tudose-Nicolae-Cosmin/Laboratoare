import numpy as np
import pandas as pd


def generare_dataset():

    # np.random.seed(40)
    zile = 60
    data_list = []

    for zi in range(1, zile + 1):
        # 1. Numar aleatoriu de produse
        nr_produse = np.random.randint(5, 16)

        # 2. Preturi
        preturi = np.random.normal(40, 8, nr_produse)
        preturi = np.maximum(preturi, 1.0)

        # 3. Cantitati
        cantitati = np.random.randint(1, 11, nr_produse)

        # 4. Promotii (30% sanse sa scada pretul cu 20%)
        is_promo = np.random.random(nr_produse) < 0.30
        preturi_finale = np.where(is_promo, preturi * 0.8, preturi)

        # Adaugam in lista
        for p, c, promo in zip(preturi_finale, cantitati, is_promo):
            data_list.append({
                'Zi': zi,
                'Pret_Unitar': round(p, 2),
                'Cantitate': c,
                'Promotie': promo
            })

    df = pd.DataFrame(data_list)
    return df


def proceseaza_si_afiseaza_statistici(df):

    # 5. Totalul vanzarilor per tranzactie/zi
    df['Total_Vanzare'] = df['Pret_Unitar'] * df['Cantitate']

    # 6. Profitul
    df['Profit'] = df['Total_Vanzare'] * 0.30



    print(f"PRETURI -> Medie: {df['Pret_Unitar'].mean():.2f} | Max: {df['Pret_Unitar'].max():.2f} | Min: {df['Pret_Unitar'].min():.2f}")
    print(f"CANTITATI -> Medie: {df['Cantitate'].mean():.2f} | Max: {df['Cantitate'].max()} | Min: {df['Cantitate'].min()}")
    print(f"PROFIT (per item) -> Medie: {df['Profit'].mean():.2f} | Max: {df['Profit'].max():.2f} | Min: {df['Profit'].min():.2f}")

    total_vanzari_60_zile = df['Total_Vanzare'].sum()
    total_profit_60_zile = df['Profit'].sum()

    print(f"Total Vanzari (60 zile): {total_vanzari_60_zile:.2f} RON")
    print(f"Profit Total (60 zile):  {total_profit_60_zile:.2f} RON")

    return df


if __name__ == "__main__":
    dataset = generare_dataset()
    proceseaza_si_afiseaza_statistici(dataset)