import matplotlib.pyplot as plt
import pandas as pd
import dataSet

df = dataSet.generare_dataset()

df['Venit'] = df['Pret_Unitar'] * df['Cantitate']
df['Profit'] = df['Venit'] * 0.30

#Evolutia veniturilor si profitului pe zile
evolutie_zilnica = df.groupby('Zi')[['Venit', 'Profit']].sum()

#Vizualizarea promotiilor
pret_mediu_promo = df[df['Promotie'] == True]['Pret_Unitar'].mean()
pret_mediu_fara = df[df['Promotie'] == False]['Pret_Unitar'].mean()

#Grafic
plt.figure(figsize=(12, 10))

# Grafic 1: Evolutia Venit si Profit
plt.subplot(2, 2, 1)
plt.plot(evolutie_zilnica.index, evolutie_zilnica['Venit'], label='Venit Total', color='blue')
plt.plot(evolutie_zilnica.index, evolutie_zilnica['Profit'], label='Profit Total', color='green', linestyle='--')
plt.title('Evoluția Veniturilor și Profitului pe Zile')
plt.xlabel('Ziua')
plt.ylabel('RON')
plt.legend()
plt.grid(True, alpha=0.3)

# Grafic 2: Distributia Preturilor
plt.subplot(2, 2, 2)
plt.hist(df['Pret_Unitar'], bins=20, color='orange', edgecolor='black')
plt.title('Distribuția Prețurilor')
plt.xlabel('Preț Unitar')

# Grafic 3: Distributia Cantitatilor
plt.subplot(2, 2, 3)
plt.hist(df['Cantitate'], bins=10, color='purple', edgecolor='black')
plt.title('Distribuția Cantităților Vândute')
plt.xlabel('Cantitate')

# Grafic 4: Impact Promotii
plt.subplot(2, 2, 4)
plt.bar(['Fără Promoție', 'Cu Promoție'], [pret_mediu_fara, pret_mediu_promo], color=['gray', 'red'])
plt.title(f'Preț Mediu: {pret_mediu_fara:.1f} vs {pret_mediu_promo:.1f}')
plt.ylabel('Preț Mediu (RON)')

plt.tight_layout()
plt.show()
