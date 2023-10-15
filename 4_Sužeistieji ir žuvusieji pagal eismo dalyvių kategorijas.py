# # 4. SUŽEISTŲJŲ IR ŽUVUSIŲJŲ SKAIČIUS 2020-2022 M. PAGAL EISMO DALYVIŲ KATEGORIJAS

import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns

# #  CSV FAILO ĮKĖLIMAS

# csv_failo_pavadinimas = 'Pagal transporto priemones.csv'
# data1 = pd.read_csv(csv_failo_pavadinimas)
# print(data1)
#
# #  DUOMENŲ GRUPAVIMAS
#
# grupuojame = data1.groupby(['Nukentėjusiųjų tipas','Kelių naudotojai'])['Reikšmė'].sum().astype(int)
# print(grupuojame)
# # print(len(grupuojame))
# # print(type(grupuojame))
#
# first_table = grupuojame.loc['Sužeistieji']
# print(first_table)
# second_table = grupuojame.loc['Žuvusieji']
# print(second_table)
#
# # DUOMENŲ GRAFINIS ATVAIZDAVIMAS
#
# palette_color = sns.color_palette('colorblind')
# ex=(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
#
# plt.figure(figsize=(12,12))
# plt.subplot(1,2,1)
# plt.pie(first_table, colors=palette_color, autopct='%.0f%%', explode = ex)
# plt.title('2020-2022 m. kelių eismo įvykiuose sužeistųjų skaičius',fontsize=12)
#
# plt.subplot(1,2,2)
# plt.pie(second_table, colors=palette_color, autopct='%.0f%%',explode = ex,)
# plt.title('2020-2022 m. kelių eismo įvykiuose žuvusiųjų skaičius',fontsize = 12)
# plt.legend(loc='upper center', labels=first_table.index, borderpad=0, bbox_to_anchor=(0.1, 0.1))
# plt.show()
