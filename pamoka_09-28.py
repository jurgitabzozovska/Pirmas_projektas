import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import psycopg2
import numpy as np
import matplotlib.pyplot as plt
#
#
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="ZaislaiProducts",
#         user="postgres",
#         password="truputukas1982"
#     )
#     drop_table query = ''''''
#         DROP TABLE IF EXISTS butai
#
#     cursor =
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS butai (
#         id SERIAL PRIMARY KEY,
#         Adresas VARCHAR(255),
#         Kambariu_sk INT,
#         Plotas DECIMAL(10,2),
#         Aukstas VARCHAR(255),
#         Kaina INT,
#         Kv_kaina DECIMAL(10,2)
#         )
#         """
#     cursor.execute(create_table_query)
#     print('Table created successfully')
#
#     Butu_sarasas = []
#
#     for i in range(1,6):
#         url = f'https://www.aruodas.lt/atviru-duru-dienos/puslapis/{i}/'
#         response = requests.get(url)
#         # print(response.content)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         blokas = soup.find_all('div', class_='list-row-v2 object-row opendoor advert')
#
#         for butas in blokas:
#                 Adresas = soup.select_one('div.list-adress-v2 h3').text.strip()
#                 Kambariu_sk = butas.find('div', class_='list-RoomNum-v2 list-detail-v2').text.strip()
#                 Plotas = butas.find('div', class_='list-AreaOverall-v2 list-detail-v2').text.strip()
#                 Aukstas = butas.find('div', class_='list-Floors-v2 list-detail-v2').text.strip()
#                 Kaina = butas.find('span', class_='list-item-price-v2').text.strip('€').replace(' ','')
#                 Kv_kaina = butas.find('span', class_='price-pm-v2').text.strip().replace('€/m²', '').replace(' ','').replace(',', '.')
#                 if Kambariu_sk == '' or Plotas == '' or Kaina == '' or Kv_kaina == '':
#                     continue
#                 Kambariu_sk = int(Kambariu_sk)
#                 Plotas = float(Plotas)
#                 Kaina = int(Kaina)
#                 Kv_kaina = float(Kv_kaina)
#
#                 Butu_sarasas.append((Adresas, Kambariu_sk, Plotas, Aukstas, Kaina, Kv_kaina))
#                 # print(Butu_sarasas)
#         df = pd.DataFrame(Butu_sarasas, columns=['Adresas', 'Kambarius_sk', 'Plotas', 'Aukstas', 'Kaina', 'Kv_kaina'])
#         # print(df)
#         df.to_csv('Butai.csv')
#
#         insert_query = "INSERT INTO butai (Adresas, Kambariu_sk, Plotas, Aukstas, Kaina, Kv_kaina) VALUES(%s,%s,%s,%s,%s,%s)"
#         cursor.executemany(insert_query,Butu_sarasas)
#         print(f'Products inserted into list succesfully!')
#         connection.commit()
# if __name__ =='__main__':
#     create_and_insert_product()

#
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import psycopg2
import numpy as np
import matplotlib.pyplot as plt

def create_and_insert_product():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="ZaislaiProducts",
        user="postgres",
        password="truputukas1982"
    )
    drop_table_query = '''
        DROP TABLE IF EXISTS butaix
'''
    create_table_query = """
        CREATE TABLE butaix (
        id SERIAL PRIMARY KEY,
        Adresas VARCHAR(255),
        Kambariu_sk INT,
        Plotas DECIMAL(10,2),
        Aukstas VARCHAR(255),
        Kaina DECIMAL(10,2),
        Kv_kaina DECIMAL(10,2)
        )
    """
    cursor = connection.cursor()
    cursor.execute(drop_table_query)
    cursor.execute(create_table_query)
    print('Table created successfully')
    Butu_sarasas = []
    for i in range(1,6):
        url = f'https://www.aruodas.lt/atviru-duru-dienos/puslapis/{i}/'
        response = requests.get(url)
        # print(response.content)
        soup = BeautifulSoup(response.content, 'html.parser')
        blokas = soup.find_all('div', class_='list-row-v2 object-row opendoor advert')
        for butas in blokas:
            Adresas = soup.select_one('div.list-adress-v2 h3').text.strip(). replace(',', '')
            Kambariu_sk = butas.find('div', class_='list-RoomNum-v2 list-detail-v2').text.strip()
            Plotas = butas.find('div', class_='list-AreaOverall-v2 list-detail-v2').text.strip()
            Aukstas = butas.find('div', class_='list-Floors-v2 list-detail-v2').text.strip()
            Kaina = butas.find('span', class_='list-item-price-v2').text.strip('€').replace(' ', '')
            Kv_kaina = butas.find('span', class_='price-pm-v2').text.strip().replace('€/m²', '').replace(' ', '').replace(',', '.')
            if Kambariu_sk == '' or Plotas == '' or Kaina == '' or Kv_kaina == '':
                continue
            Kambariu_sk = int(Kambariu_sk)
            Plotas = float(Plotas)
            Kaina = int(Kaina)
            Kv_kaina = float(Kv_kaina)
            Butu_sarasas.append((Adresas, Kambariu_sk, Plotas, Aukstas, Kaina, Kv_kaina))
            # print(Butu_sarasas)
    df = pd.DataFrame(Butu_sarasas, columns=['Adresas', 'Kambarius_sk', 'Plotas', 'Aukstas', 'Kaina', 'Kv_kaina'])
        # print(df)
    df.to_csv('Butaix.csv')
    insert_query = "INSERT INTO butaix (Adresas, Kambariu_sk, Plotas, Aukstas, Kaina, Kv_kaina) VALUES(%s, %s,%s,%s,%s,%s)"
    cursor.executemany(insert_query, Butu_sarasas)
    print(f'Products inserted into list succesfully!')
    connection.commit()
        # cursor.close()
        # connection.close()
    select_query = "SELECT * FROM butaix"
        # cursor.execute(select_query)
        # Butu_sarasas = cursor.fetchall()
    df = pd.DataFrame(Butu_sarasas, columns = ['Adresas', 'Kambarius_sk', 'Plotas', 'Aukstas', 'Kaina', 'Kv_kaina'])
    print(df)
if __name__ == '__main__':
    create_and_insert_product()

