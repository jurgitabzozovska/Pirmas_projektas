# # 2. NEBLAIVIŲ ASMENŲ EISMO ĮVYKIAI

import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns

# #  CSV FAILO ĮKĖLIMAS
# csv_failo_pavadinimas = 'neblaiviu_ivykiai_pagal menesius_metus.csv'
# data3 = pd.read_csv(csv_failo_pavadinimas)
# print(data3)

# #  DUOMENŲ IŠSKAIDYMAS
# df3 = pd.DataFrame(data3)
# df3[['Metai', 'Menuo']] = df3["Laikotarpis"].str.split('M', expand=True)
# print(df3)
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
