# # 2. NEBLAIVIŲ ASMENŲ EISMO ĮVYKIAI

import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns

 # CSV FAILO ĮKĖLIMAS
# csv_failo_pavadinimas = 'Darbo_failai/neblaiviu_ivykiai_pagal menesius_metus.csv'
# data3 = pd.read_csv(csv_failo_pavadinimas)
# print(data3)
#
# # #  DUOMENŲ IŠSKAIDYMAS
# df3 = pd.DataFrame(data3)
# df3[['Metai', 'Menuo']] = df3["Laikotarpis"].str.split('M', expand=True)
# # print(df3)
# Viso_įvykių_pagal_metus = df3.groupby('Metai')['Reikšmė'].sum()
# # print(Viso_įvykių_pagal_metus)
#
# df3 = df3.drop(['Laikotarpis'], axis=1)
# print(df3)

# # #  DUOMENŲ GRAFINIS ATVAIZDAVIMAS
# x = df3['Metai']
# y = df3['Reikšmė']
# plt.plot(x, y, label = 'Įvykiai', color = 'pink', linestyle = '', marker = 'o')
# plt.legend()
# plt.xlabel('Metai')
# plt.ylabel('Įvykių skaičius')
# plt.title('Kelių eismo įvykiai, kuriuose nukentėjo žmonės dėl neblaivių asmenų')
# plt.show()


# # Kitoks atvaizdavimas
# plt.figure(figsize=(8,8))
# Laikotarpis = ['Gruodis', 'Lapkritis', 'Spalis', 'Rugsėjis',	'Rugpjūtis',	'Liepa',	'Birželis',	'Gegužė',	'Balandis', 'Kovas',	'Vasaris',	'Sausis']
# metai2022 = [7,11,13,14,19,12,16,21,22,14,14,14]
# metai2021 = [12,9,15,21,18,27,22,14,19,18,4,4]
# metai2020 = [9,20,21,20,26,24,22,20,24,22,19,12]
# x_axis = np.arange(len(Laikotarpis))
# plt.bar(x_axis + 0.20, metai2022, width = 0.2, label = '2022 m.', color = 'yellow')
# plt.bar(x_axis+0.20*2, metai2021, width = 0.2, label = '2021 m.', color = 'green')
# plt.bar(x_axis+0.20*3, metai2020, width = 0.2, label = '2020 m.', color = 'red')
# x_axis = np.arange(len(Laikotarpis))
# plt.xlabel('Metai')
# plt.ylabel('Įvykių skaičius')
# plt.legend()
# plt.show()