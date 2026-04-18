import pandas as pd
import matplotlib.pyplot as plt

# 1. Učitavanje podataka
df = pd.read_csv("netflix.csv")

# 2. Prikaz prvih redova
print("=== PRVI REDOVI ===")
print(df.head())

# 3. Osnovne informacije
print("\n=== INFO ===")
print(df.info())

# 4. Čišćenje podataka
df = df.dropna()

# 5. Analiza – koliko filmova po godini
movies_per_year = df['release_year'].value_counts().sort_index()

print("\n=== FILMOVI PO GODINAMA ===")
print(movies_per_year.tail(10))

# 6. Grafikon
movies_per_year.tail(20).plot(kind='bar')

plt.title("Broj filmova po godinama")
plt.xlabel("Godina")
plt.ylabel("Broj filmova")

plt.show()
