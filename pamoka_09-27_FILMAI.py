import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import psycopg2
import numpy as np
import matplotlib.pyplot as plt

## UŽDUOTIS KNYGOS
# url = 'https://vaga.lt/grozine-literatura'
# response = requests.get(url)
# # print(response.status_code)
# soup = BeautifulSoup(response.content, 'html.parser')
# conteineris = soup.find_all('div', class_='product-item-container')
# Knygu_sarasas = []
# for knygos in conteineris:
#     pavadinimas = knygos.find('p', class_ = 'name').text.strip()
#     kaina = float(knygos.find('div', class_ = 'price price-align-wrapper').text.strip('€').replace(',','.'))
#     autorius = knygos.find('p', class_='Autorius').text.strip()
#     Knygu_sarasas.append((pavadinimas, kaina, autorius))
# df = pd.DataFrame(Knygu_sarasas, columns=['Pavadinimas','Kaina','Autorius'])
# print(df)
#
# suma = np.sum(df["Kaina"])
# vidurkis = np.mean(df["Kaina"])
# min = np.min(df["Kaina"])
# max = np.max(df["Kaina"])
# mediana = np.median(df["Kaina"])
# print(f"Kainu statistika: Maksimumas:{max}, \n Minimumas: {min}, \n Viurkis:{vidurkis}, \n Mediana: {mediana}")
#
# sns.set(style = "whitegrid")
# sns.histplot(data=df, x="Kaina", kde=True)
# plt.ylabel("Knygu skaicius")
# plt.show()




# NAUJAUSI/SENIAUSI FILMAI. 100 VNT. PAVADINIMAS. METAI. METASCORE

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
# }
# Filmu_sarasas = []
# for i in range(1,6):
#     url = f'https://www.metacritic.com/browse/movie/all/all/all-time/userscore/?releaseYearMin=1910&releaseYearMax=2023&page={1}'
#     page = requests.get(url, headers=headers)
#     # print(page.status_code)
#     soup = BeautifulSoup(page.content, "html.parser")
#     conteineris = soup.find_all('div', class_='c-finderProductCard')
# # print(conteineris)
#     for filmas in conteineris:
#         Pavadinimas = filmas.find('div', class_ = 'c-finderProductCard_title').text.strip()
#         Metai = filmas.find('span', class_ = 'u-text-uppercase').text.strip()
#         Metascore = (filmas.find('div', class_ = 'c-finderProductCard_meta g-outer-spacing-top-auto').text.strip().replace('Metascore',''))
#         Filmu_sarasas.append((Pavadinimas, Metai, Metascore))
#         df = pd.DataFrame(Filmu_sarasas, columns=["Pavadinimas", "Metai", "Metascore"])
# #         print(df)
# df.to_csv("filmai.csv")
#
# df = pd.read_csv('filmai.csv')
# print(df.to_string())

# DUOMENU ANALIZAVIMAS:
# min = np.min(df["Metascore"])
# max = np.max(df["Metascore"])
# # print(f'Maksimalus ivertinimas: {max}\nMinimalus ivertinimas: {min}')

# Naujausias_filmas = np.max(df["Metai"])
# # print(f'Naujausio filmo isleidimo metai yra:{Naujausias_filmas}')

# Seniausias_filmas = np.min(df["Metai"])
# # print(f'Seniausiai isleistas filmas -{Naujausias_filmas}')

# Vidutinis_ivertinimas = df['Metascore'].mean()
# # print(Vidutinis_ivertinimas)

# Filmai_pagal_metus_ASC = df.sort_values(by=['Metai'], ascending=False)
# # print(Filmai_pagal_metus_ASC)

# Kiek_filmu_ivertinta=df['Metascore'].value_counts()
## print(Kiek_filmu_ivertinta)



# Year =df["Metai"].str.split(',', expand=True)
# # print(Year)
# df["Metai"] = Metai
# # print(df)




