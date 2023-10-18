# # # 1 Visi 2020-2022 m. Lietuvos kelių eismo įvykiai

import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns

# # # CSV FAILO ĮKĖLIMAS

csv_failo_pavadinimas = 'Darbo_failai/eismo ivykiai.csv'
data1 = pd.read_csv(csv_failo_pavadinimas)
print(data1)
#
#
# # # DUOMENŲ IŠSKAIDYMAS
#
df1 = pd.DataFrame(data1)
df1[['Metai', 'Menuo']] = df1["Laikotarpis"].str.split('M', expand=True)
df1 = df1.drop(['Laikotarpis','Rodiklis','Matavimo vienetai'], axis=1)
df1.to_csv('eismo_ivykiai.csv', index=False)
print(df1)
#
# # #  DUOMENŲ GRUPAVIMAS

Suminis_grupavimas = df1.groupby('Metai')['Reikšmė'].sum()
print(Suminis_grupavimas)
# # vid pagal metus
vid = df1.groupby('Metai')['Reikšmė'].mean().round(0).astype(int)
print(vid)
# # #
# print(type(vid))
# # #  DUOMENŲ TIPO PAKEITIMAS
w = 0.4
Metai = vid.index.to_numpy().astype(int)
print(Metai)
total = Suminis_grupavimas.values
print(total)
mean = vid.values
print(mean)
print(type(Metai))
print(Metai+w)

# # #  DUOMENŲ GRAFINIS ATVAIZDAVIMAS

#Kelių eismo įvykiu kiekis ir vidurkis
plt.figure(figsize=(12,5))
Metai1 = Metai
Metai2 = Metai-w
bar1 = plt.bar(Metai1, total, width=w, label='Visi kelių eismo įvykiai')
for bar in bar1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2),ha='center', va='bottom')
bar2 = plt.bar(Metai2, mean, width=w, label='Vidurkis', alpha=0.5)
for bar in bar2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2),ha='center', va='bottom')

plt.xlabel('Metai')
plt.ylabel('Reikšmė')
plt.legend(loc='upper left')
plt.title('Kelių eismo įvykiai ir jų vidurkis pagal metus')
plt.xticks(Metai,  Metai)
plt.show()

