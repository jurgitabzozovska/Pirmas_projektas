# # 6. DĖL NEBLAIVIŲ ASMENŲ ŽUVUSIŲJŲ KELIŲ EISMO ĮVYKIUOSE 2020-2022 M. LIETUVOJE, LATVIJOJE IR ESTIJOJE SKAIČIAUS
# # PALYGINIMAS

import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns


# #  FAILO IŠ INTERNETINIO TINKLAPIO NUSKAITYMAS
# url = 'https://www.csdd.lv/en/road-accidents/the-road-traffic-safety-statistics'
# response = requests.get(url)
# # print(response.status_code)
# soup = BeautifulSoup(response.content, 'html.parser')
# data = []
# table = soup.find('div', class_='table-wrapper')
# # print(table)
# headers = table.find_all("th")
# print(headers)
# titles = [header.text.strip() for header in headers][:2]
# # print(titles)
# rows = table.find_all('tr')[1:]
# # print(rows)
# rows = rows[:-1]
# for row in rows[1:]:
#     columns = row.find_all('td')
#     year = columns[0].text.strip()
#     from_date_columns = columns[1:]
#     from_date = ' '.join([col.text.strip() for col in from_date_columns])
#     from_date_numbers = from_date.split()
#     # print(from_date)
#     # print(from_date_numbers)
#     # break
##     data.append({
#         'Year': year,
#         'From 01.01': from_date_numbers[1]
#     })
# #
# df2 = pd.DataFrame(data, columns=titles)
# df2 = df2.tail(3)
# # print(df2)


#
# # #  ESTIJOS ĮVYKIŲ CSV FAILO ĮKĖLIMAS
#
# df3 = pd.read_csv('estijos zuve.csv')
# # print(df3)
# df3 = pd.DataFrame(df3)
# # print(df3)
# df3 = df3.drop(0)
# # print(df3)
# Sum = df3.groupby('Indicator').sum()
# sum = pd.DataFrame(Sum)
# sum.drop('Month',axis=1, inplace=True)
# sum = sum.transpose()
# # print(sum.columns)
# # print(sum)
# Viso_EE = sum['Traffic accidents with fatalities'].sum()
# # print(f'Bendras Estijos įvykių skaičius:{Viso_EE}')
# #
# # # #   LIETUVOS ĮVYKIŲ CSV FAILO ĮKĖLIMAS
# # data4 = pd.read_csv('Lietuvos zuve.csv')
# # # print(data4)
# # df4 = pd.DataFrame(data4)
#
# # # DUOMENŲ TVARKYMAS
# # print(df4)
# df4[['Metai', 'Menuo']] = df4["Laikotarpis"].str.split('M', expand=True)
# # print(df4)
# df4 = df4.drop(['Laikotarpis','Rodiklis','Matavimo vienetai'], axis=1)
# # print(df4)
#
# # # DUOMENŲ GRUPAVIMAS IR JUNGIMAS
# Suminis_grupavimas2 = df4.groupby('Metai')['Reikšmė'].sum()
# # print(Suminis_grupavimas2)
# Metai = Suminis_grupavimas2.index.astype(int)
# # print(Metai)
# Lietuva = Suminis_grupavimas2.values
# # print(Lietuva)
# Viso_LT = df4['Reikšmė'].sum()
# # print(f'Bendras Lietuvos įvykių skaičius:{Viso_LT}')
# #
# Latvija = df2["From 01.01"].to_numpy().astype(int)
# print(Latvija)
# Estija = [i[0] for i in sum.values]
# print(Estija)
#
# # # # GRAFINIS ATVAIZDAVIMAS
# plt.figure(figsize=(8,8))
# w = 0.4
# Metai1 = Metai
# Metai2 = Metai - w
# Metai3 = Metai + w
#
# bar1 = plt.bar(Metai, Lietuva, width=w, label='Lietuva', color='mediumseagreen')
# bar2= plt.bar(Metai - w, Latvija, width=w, label='Latvija', color='tomato')
# bar3 = plt.bar(Metai + w, Estija, width=w, label='Estija', color='royalblue')
# for bars in [bar1, bar2, bar3]:
#     for bar in bars:
#         yval = bar.get_height()
#         plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, round(yval, 2), ha='center', va='bottom')
# plt.xlabel('Metai')
# plt.ylabel('Ivykiai')
# plt.legend(loc='upper left')
# plt.title('Žuvusių kelių eismo įvykiuose 2020-2022 m. Baltijos šalyse skaičiaus palyginimas')
# plt.xticks(Metai,  Metai)
# plt.show()