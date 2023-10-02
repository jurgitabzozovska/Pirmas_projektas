import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import psycopg2
import numpy as np
import matplotlib.pyplot as plt


# def create_and_insert_product():
#         connection = psycopg2.connect(
#                 host="localhost",
#                 port=5432,
#                 database="Aruodas",
#                 user="postgres",
#                 password="truputukas1982"
#         )
#         cursor = connection.cursor()
#         create_table_query = """
#                 CREATE TABLE IF NOT EXISTS turtas (
#                 id SERIAL PRIMARY KEY,
#                 Adresas VARCHAR(255),
#                 Kambariu_sk INT,
#                 Plotas DECIMAL(10,2),
#                 Aukstas VARCHAR(255),
#                 Kaina INT,
#                 Kv_kaina DECIMAL(10,2)
#                 )
#                 """
#
#         cursor.execute(create_table_query)
#         #print('Table created successfully')
#
#         Butu_sarasas = []
#
#         for i in range(1,6):
#                 url = f'https://www.aruodas.lt/atviru-duru-dienos/puslapis/{i}/'
#                 response = requests.get(url)
#                 # print(response.content)
#                 soup = BeautifulSoup(response.content, 'html.parser')
#                 blokas = soup.find_all('div', class_='list-row-v2 object-row opendoor advert')
#
#                 for butas in blokas:
#                         Adresas = soup.select_one('div.list-adress-v2 h3').text.strip()
#                         Kambariu_sk = butas.find('div', class_='list-RoomNum-v2 list-detail-v2').text.strip()
#                         Plotas = butas.find('div', class_='list-AreaOverall-v2 list-detail-v2').text.strip()
#                         Aukstas = butas.find('div', class_='list-Floors-v2 list-detail-v2').text.strip()
#                         Kaina = butas.find('span', class_='list-item-price-v2').text.strip('€').replace(' ', '')
#                         Kv_kaina = butas.find('span', class_='price-pm-v2').text.strip().replace('€/m²', '').replace(' ', '').replace(',','.')
#                         if Kambariu_sk == '' or Plotas == '' or Kaina== '' or Kv_kaina == '':
#                                 continue
#                         Kambariu_sk = int(Kambariu_sk)
#                         Plotas = float(Plotas)
#                         Kaina = int(Kaina)
#                         Kv_kaina = float(Kv_kaina)
#
#                         Butu_sarasas.append((Adresas, Kambariu_sk, Plotas, Aukstas, Kaina, Kv_kaina))
#                         # print(Butu_sarasas)
#         df = pd.DataFrame(Butu_sarasas,columns=['Adresas', 'Kambarius_sk', 'Plotas', 'Aukstas', 'Kaina', 'Kv_kaina'])
#         # # print(df)
#         df.to_csv('Aruodas.csv')
#
#         insert_query = "INSERT INTO turtas (Adresas, Kambariu_sk, Plotas, Aukstas, Kaina, Kv_kaina) VALUES(%s, %s,%s,%s,%s,%s)"
#
#         cursor.executemany(insert_query, Butu_sarasas)
#         print(f'Products inserted into list succesfully!')
#         connection.commit()
#         select_query = "SELECT * FROM turtas"
#         # cursor.close()
#         # connection.close()
# if __name__ =='__main__':
#         create_and_insert_product()


# DUOMENŲ ANALIZĖ:

# df = pd.read_csv('Aruodas.csv')
# # print(df.to_string())
# Butai_pagal_kaina_ASC = df.sort_values(by=['Kaina'], ascending=False)
# # print(Butai_pagal_kaina_ASC)
#
# Brangiausias = df['Kaina'].max()
# Pigiausias = df['Kaina'].min()
# # print(f'Pigiausio buto verte: {Pigiausias}€ \nBrangiausio buto verte: {Brangiausias}€ ')
#
# Kainu_avg = df['Kaina'].mean()
# # print(f'Vidutinė buto kaina yra:', Kainu_avg, '€')
#
# Kainu_avg_pagal_adresa = df.groupby('Adresas')['Kaina'].mean().round(2)
# # print(Kainu_avg_pagal_adresa)
#
# Kaina_pagal_kambariu_sk = df.groupby('Kambarius_sk')['Kaina'].mean()
# # print(Kaina_pagal_kambariu_sk)
#
# Daugiausia_parduodama_butu = df['Adresas'].mode()
# # print(f'Daugiausia parduodama butu: {Daugiausia_parduodama_butu}')
#
# max = np.max(df['Kaina'])
# min = np.min(df['Kaina'])
# bendra_verte = np.sum(df['Kaina'])
# vidurkis = np.mean(df['Kaina'])
# mediana = np.median(df['Kaina'])
# print(f'Statistika:\n Maksimali kaina: {max} €,\n Minimali kaina: {min} €,\n Vidutine kaina:{vidurkis} €, \n Mediana: {mediana}\n Visu butu verte: {bendra_verte} €')

# plt.figure(figsize=(12,5))
# sns.barplot(x=Kaina_pagal_kambariu_sk.index, y=Kaina_pagal_kambariu_sk.values)
# plt.xlabel('Aukstai')
# plt.ylabel('Kaina')
# plt.title('Butu kainu vidurkis pagal buto auksta')
# plt.show()

# plt.figure(figsize=(12,5))
# sns.barplot(x = Kainu_avg_pagal_adresa.index, y= Kainu_avg_pagal_adresa.values)
# plt.xticks(rotation = 8)
# plt.xlabel('Vidutine kaina')
# plt.ylabel('Kainos avg')
# plt.title('Kainos vidurkis pagal adresa')
# plt.show()

# plt.pie(df['Kaina'], labels=df["Kaina"])
# plt.title('Kaina pagal adresa')
# plt.show()

