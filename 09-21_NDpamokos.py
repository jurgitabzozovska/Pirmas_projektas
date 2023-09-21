## 3 UŽDUOTIS
# URL: https://coinmarketcap.com
#
# Naudokite Beautiful Soup, kad galėtumėte „web scraping" funkcionalumą,
# kad gautumėte kriptovaliutos kainų duomenis iš populiarios kriptovaliutų rinkos svetainės.
# Išgaukite:
# kainų,
# div- class="sc-4984dd93-0 fiHcNM"
#
# # laiko
# 1 h class="sc-4984dd93-0 fiHcNM"
# 24h class="sc-4984dd93-0 fiHcNM""
#
# 7d class="sc-4984dd93-0 fiHcNM"
# name class="sc-4984dd93-0 fiHcNM"
# kitus susijusius duomenis iš svetainės.
#
# Įkelkite gautus duomenis į Pandas DataFrame.
# Atliekant duomenų tvarkymą, galite konvertuoti datą į tinkamą formatą,
# ištrinti dublikatus arba tvarkyti trūkstamas reikšmes.
#
# Atlikite analizę, kad gautumėte statistiką apie kriptovaliutos kainų kitimą.
# Paskaičiuokite vidutines, minimalias ir maksimalias kainas, taip pat kitas statistikos vertes.
#
# Sukurkite linijinį grafiką, kuris atvaizduoja kriptovaliutos kainos kitimą laike (x ašis - laikas, y ašis - kaina).
# Taip pat galite sukurti stulpelinį grafiką, kuris rodo kainos svyravimus tarp skirtingų kriptovaliutų.


import pandas as pd
# from bs4 import BeautifulSoup
# import requests
# import psycopg2
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host='localhost',
#         port=5432,
#         database='crypto_products',
#         user='postgres',
#         password='truputukas1982'
#     )
#
#     cursor = connection.cursor()
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS crypto(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR (255),
#         price DECIMAL (10,2),
#         quantity INT)
#     """
#     cursor.execute(create_table_query)
#     print('Table created successfully')
#     url = f'https://coinmarketcap.com/'
#     response = requests.get(url)
#     print(response.status_code)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     product_elements = soup.find_all('div', class_='GRID_ITEM')
#     # print (product_elements)
#     product_data = []
#     for product_element in product_elements:
#             product_name = product_element.find('div', class_='product-title').text.strip()
#             product_price = float(product_element.find('span', class_='price-value').text.strip().replace('€', ''))
#             product_quantity = product_element.find('b').text.strip()[:1]
#             print(f"Adding products to the list: {product_name}")
#            # time.sleep(2)
#             # product_data.append((product_name, product_price, product_quantity))
#             # insert_query ='INSERT INTO varle_products (name, price, quantity) VALUES(%s, %s, %s)'
#             # cursor.execute(insert_query, (product_name, product_price, product_quantity))
#             # print('Products inserted into list sucessfully!')
#     connection.commit()
#         # df = pd.DataFrame(product_data, columns=['name', 'price', 'quantity'])
#         # print(df)
#     select_query = 'SELECT * FROM varle_products'
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     df = pd.DataFrame(rows, columns=['id', 'name', 'price', 'quantity'])
#     print(df)
# if __name__ == '__main__':
#     create_and_insert_product()
