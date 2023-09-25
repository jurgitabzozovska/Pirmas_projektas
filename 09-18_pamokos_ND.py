from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
# SIGITOS
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host="localhost",
#         port=5432,
#         database="ZaislaiProducts",
#         user="postgres",
#         password="truputukas1982"
#     )
#     cursor = connection.cursor()
#     create_table_query = """
#         CREATE TABLE IF NOT EXISTS zaislai_products (
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(255),
#         price DECIMAL(10,2)
#         )
#     """
#     cursor.execute(create_table_query)
#     print('Table created successfully')
#     url = 'https://www.1a.lt/c/zaislu-pasaulis-20-zaislams-su-kodu/87w'
#     response = requests.get(url)
#     print(response.status_code)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     product_elements = soup.find_all('div', class_='catalog-taxons-products-container__grid-row')
#     # print(product_elements)
#     product_data = []
#     for product_element in product_elements:
#         product_name = product_element.find('div', class_='catalog-taxons-product__files').text.strip()
#         product_price = float(product_element.find('span', class_='catalog-taxons-product-price__item-price').text.strip().replace('€', '').replace('vnt.', '').replace('\n\n/', '').replace(' ','').replace(',', '.'))
#         print(f'Pridedame produktus i sarasa: {product_name}')
#         product_data.append((product_name, product_price))
#         insert_query = "INSERT INTO zaislai_products (name, price) VALUES(%s, %s)"
#         cursor.execute(insert_query, (product_name, product_price))
#         print(f'Products inserted into list succesfully!')
#         connection.commit()
#     # df=pd.DataFrame(product_data, columns=['name', 'price'])
#     # print(df)
#     select_query = "SELECT * FROM zaislai_products"
#     cursor.execute(select_query)
#     rows = cursor.fetchall()
#     df=pd.DataFrame(rows, columns = ['id', 'name', 'price'])
#     print(df)
# if __name__ =='__main__':
#     create_and_insert_product()
# EUGENIJAUS
# def create_and_insert_product():
#     connection = psycopg2.connect(
#         host = "localhost",
#         port=5432,
#         database = "products",
#         user='postgres',
#         password = "truputukas1982"
#     )
#     cursor = connection.cursor()
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS varle_products (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(500),
#     price DECIMAL(10,2),
#     quantity INT)
#     """
#     cursor.execute(create_table_query)
#     print("Table is created successfully!")
#     for i in range(1,125):
#         url = f'https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/?p={i}'
#         response = requests.get(url)
#         # print(response.status_code)
#         soup = BeautifulSoup(response.content, 'html.parser')
#         product_elements = soup.find_all('div', class_ = 'GRID_ITEM')
#         # print(product_elements)
#         product_data = []
#         for product_element in product_elements:
#             product_name = product_element.find('div', class_ = 'product-title').text.strip()
#             product_price = float(product_element.find('span', class_ = 'price-value').text.strip().replace('€', ''))
#             product_quantity = product_element.find('b').text.strip()[:1]
#             print(f'Adding products to the list: {product_name}')
#             # time.sleep(2) ## nei b8tina nei privaloma
#             # product_data.append((product_name, product_price, product_quantity))
#             # insert_query = "INSERT INTO varle_products (name, price, quantity) VALUES (%s, %s, %s )"
#             # cursor.execute(insert_query, (product_name, product_price, product_quantity))
#             # print("Products inserted into list successfully!")
#             connection.commit()
#             # df = pd.DataFrame(product_data, columns=['name', 'price', 'quantity'])
#             # print(df)
#             # df.to_excel('kompa.xlsx')
#         select_query = "SELECT * FROM varle_products"
#         cursor.execute(select_query)
#         rows = cursor.fetchall()
#         df = pd.DataFrame(rows, columns = ['id', 'name', 'price', 'quantity'])
#         print(df)
# if __name__ == '__main__':
#     create_and_insert_product()