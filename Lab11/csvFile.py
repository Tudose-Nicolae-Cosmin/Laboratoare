import pandas as pd

df = pd.read_csv('vanzari_companie - vanzari_companie.csv')
df['Data'] = pd.to_datetime(df['Data'])
df['Venit'] = df['Cantitate'] * df['Pret']
df['An'] = df['Data'].dt.year
df['Luna'] = df['Data'].dt.month

#1: Cele mai vandute produse pe luna
cantitate_luna = df.groupby(['An', 'Luna', 'Produs'])['Cantitate'].sum().reset_index()
idx = cantitate_luna.groupby(['An', 'Luna'])['Cantitate'].idxmax()
cele_mai_vandute = cantitate_luna.loc[idx]

#2: Venitul total pe fiecare produs
venit_total_produs = df.groupby('Produs')['Venit'].sum().reset_index()

#3: Filtrare pentru intervalul 01.01.2023 - 31.03.2023
vanzari_filtrate = df[(df['Data'] >= '2023-01-01') & (df['Data'] <= '2023-03-31')]

#4: Venitul mediu lunar
venit_lunar_total = df.groupby(['An', 'Luna'])['Venit'].sum().reset_index()
venit_mediu_lunar = venit_lunar_total['Venit'].mean()


print("1. Cele mai vandute produse pe luna")
print(cele_mai_vandute[['An', 'Luna', 'Produs', 'Cantitate']])

print("\n2. Venit total pe produs")
print(venit_total_produs)

print("\n--- Venit mediu lunar ---")
print(round(venit_mediu_lunar, 2))