import seaborn as sns
from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
import numpy as np
import matplotlib.pyplot as plt

# BARPLOT
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.barplot(data=df, x = "category", y = "reiksme")
# plt.show()

# LINEPLOT
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.lineplot(data= df, x = "category", y = "reiksme")
# plt.show()

# COUNTPLOT
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.countplot(data = df, y = "reiksme")
# plt.show()

# BOXPLOT
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.boxplot(data= df, x = "category", y = "reiksme")
# plt.show()

# PAIRPLOT
# df = pd.DataFrame({"category": ["a", "b", "a", "b"], "reiksme":[1,2,3,4]})
# sns.pairplot(df)
# plt.show()

# REGRESIJOS
# df = pd.DataFrame({'category':[2,4,6,8], 'reiksme':[1,2,3,4,]})
# sns.lmplot(data=df, x='category', y='reiksme')
# plt.show()

# HEATMAP
# df2=np.random.rand(5,4)
# sns.heatmap(df2, annot=True, cmap="coolwarm")
# plt.show()

# HISTPLOT
# data = sns.load_dataset("tips")
# sns.histplot(data=data, x="total_bill", kde=True)
# plt.show()

##UŽDUOTIS
## Naudojant "tips" duomenų rinkinį iš Seaborn, apskaičiuokite vidutinį sąskaitos sumos (total_bill) dydį ir
## vidutinį gauto mėnesinio mokesčio (tip) dydį;

# data = sns.load_dataset('tips')
# vidutine_saskaita = data['total_bill'].mean
# print(vidutine_saskaita)
# vidutinis_mokestis = data["tip"].mean()
# print(vidutinis_mokestis)

##UŽDUOTIS
## Naudojant "diamonds" duomenų rinkinį iš Seaborn, suskaičiuokite ir atvaizduokite vidutinį kainos (price) dydį
## pagal kiekvieną pjovimo (cut) grupę;

# data_1 = sns.load_dataset('diamonds')
# print(data_1)
# df = pd.DataFrame(data_1)
# vidutinis_pagal_cut = df.groupby('cut')['price'].mean()
# print(vidutinis_pagal_cut)
# plt.figure(figsize=(12,5))
# sns.barplot(x=vidutinis_pagal_cut.index, y=vidutinis_pagal_cut.values)
# plt.title('Vidutins kainos dydis pagal pjovimo grupe')
# plt.xlabel('Diamonds cut')
# plt.ylabel('Vidutine kaina')
# plt.show()

##UŽDUOTIS
## Panaudokite "tips" duomenų rinkinį, grupuokite duomenis pagal dienos dalį (time),
## apskaičiuokite vidutinį sąskaitos sumos (total_bill) dydį kiekvienoje dienos dalyje ir sukurkite kreivės grafiką,
## kuri vaizduoja vidutines sąskaitos sumas pagal dienos dalį;

# data_2 = sns.load_dataset('tips')
# print(data_2)
# df = pd.DataFrame(data_2)
# duomenys = df.groupby('time')['total_bill'].mean()
# print(duomenys)
# plt.figure(figsize=(12,5))
# sns.lineplot(x='time', y='total_bill', data=data_2)
# plt.xlabel('Dienos dalis')
# plt.ylabel('Bill')
# plt.title('Vidutinė sąskaitos suma kiekvienoje dienos dalyje')
# plt.show()


##UŽDUOTIS
## Įkelkite "titanic" duomenų rinkinį iš Seaborn. Grupuokite duomenis pagal lytį (sex) ir klasę (class),
## tada suskaičiuokite kiekvienos grupės išgyvenusiųjų skaičių.
## Tada sukurkite stulpelinę diagramą, kuri vaizduoja išgyvenusiųjų skaičių pagal lytį ir klasę;

# data_3 = sns.load_dataset('titanic')
# print(data_3)
# df = pd.DataFrame(data_3)
# duomenys_lyti_ir_klase = df.groupby(['sex', 'class'])
# # print(duomenys_lyti_ir_klase)
# pagal_isgyvenusiu_sk = df.groupby(['sex', 'class']).count()['survived']
# print(pagal_isgyvenusiu_sk)
# sns.barplot(data=df, x='sex', y='survived', hue = 'class')
# plt.title ('Išgyvenusiųjų skaičius pagal lytį ir klasę')
# plt.show()


##UŽDUOTIS
# # Įkelkite "penguins" duomenų rinkinį iš Seaborn. Sukurkite naują DataFrame,
# # kuriame būtų tik Empiriniai penguinai (species) ir kurie turi ne tuščią kiaušinio plotą (bill_length_mm).
# # Tada sukurkite kreivės grafiką, kuris vaizduotų kiaušinio pločio (bill_length_mm) pasiskirstymą pagal rūšį (species).

data_4 = sns.load_dataset('penguins')
# print(data_4)
df = pd.DataFrame(data_4)
Sarasas_pagal_species_and_length = df.get('species', 'bill_length_mm')
print(Sarasas_pagal_species_and_length)
sns.lineplot(data=data_4, x= 'species', y="bill_length_mm")
plt.title ('Kiaušinio pločio pasiskirstymą pagal rūšį')
plt.show()

# sns.lineplot(data= df, x = "category", y = "reiksme")