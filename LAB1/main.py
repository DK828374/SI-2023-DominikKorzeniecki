import pandas as pd
import numpy as np

dane = "german-credit.txt"
typy = "german-credit-type.txt"

dane_rodzaj = np.loadtxt(dane, dtype=str)

dec_sys = []
with open("german-credit.txt") as file:
    for line in file:
        dec_sys.append(line[0:-1].split(" "))

df = pd.DataFrame(dec_sys)


# ZADANIE 3a

symbole = set(np.loadtxt(dane, dtype=str, usecols=20))

print("Istniejące w systemie symbole klas decyzyjnych:")
print(symbole)
print("\n")

# ZADANIE 3b

typ1 = np.count_nonzero(np.loadtxt(dane, dtype=float, usecols=20) == 1)
typ2 = np.count_nonzero(np.loadtxt(dane, dtype=float, usecols=20) == 2)

print("Elemety z 1:", typ1, "\nElemety z 2:", typ2)
print(" ")

# ZADANIE 3c
tab = np.loadtxt(typy, dtype=str, usecols=1) == 'n'
for i in range(20):
    if tab[i]==True:
        a = i+1
        print('Maksymalna wartość dla atrybutu numerycznego [', a, "]to: ", max(np.loadtxt(dane, dtype=float, usecols=i)))
        print('Minimalna wartość dla atrybutu numerycznego [', a, "] to: ", min(np.loadtxt(dane, dtype=float, usecols=i)))

# ZADANIE 3d
print("\nLiczba dostępnych wartości:")
uniq_count_val = []
for col in df:
    uniq_count_val.append(len(df[col].unique()))
print(uniq_count_val)

# ZADANIE 3e
print("\nLista wszystkich dostępnych wartości:")
for col in df:
    if(col != 20):
        print("\nDla wartości a", col + 1)
        print(df[col].unique())
    if(col == 20):
        print("\nDla wartości decyzyjnych:")
        print(df[col].unique())


print("\n")
# ZADANIE 3f
print("Odchylenie standardowe atrybutów numerycznych:")
tab = np.loadtxt(typy, dtype=str, usecols=1) == 'n'
for i in range(len(tab)):
    if tab[i]==True:
        print('Atrybut ', i + 1,": ", np.std(np.loadtxt(dane, dtype=float, usecols=i)))
print("\n")
print("Odchylenie standardowe klas decyzyjnych:")
print("Klasy decyzyjne: ", np.std([typ1, typ2]))



# ZADANIE 4A

num_of_rows = df[0].count()
ten_percent = int(0.1*num_of_rows)
r = np.random.choice(range(num_of_rows), ten_percent, replace=False)

for r in r:
    df[0][r] = "?"
print("\n", df)

df_c = df[0].value_counts().sort_values(ascending=False)
max = df[0].value_counts().sort_values(ascending=False).max()
for i in df_c:
    if i == max:
        max_key = str(df[0].get(i))

for x in range(num_of_rows):
    if df[0][x] == "?":
        df[0][x] = max_key


# ZADANIE 4D


file = "Churn_Modelling.csv"
df = pd.read_csv(file, index_col=0)
print(df.head().to_string())

df_dummied = pd.get_dummies(df, columns=['Geography'])
df_dummied.drop('Geography_Germany', inplace=True, axis=1)
print(df_dummied.head().to_string())