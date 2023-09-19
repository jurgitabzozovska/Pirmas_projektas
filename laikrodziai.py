from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2

url = 'https://www.senukai.lt/c/telefonai-plansetiniai-kompiuteriai/ismanieji-laikrodziai-ir-apyrankes/5ji'
response = requests.get(url)
# print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
product_elements = soup.find_all('div', class_='GRID ITEM')
print(product_elements)
# product_data = []
for product_element in product_elements:
    product_name = product_element.find_all('div', class_='catalog-taxons-product__files').text.strip()
    product_price = float(product_element.find('span', class_='catalog-taxons-product-price__item-price').text.strip())
    product_price=product_price.replase('%', '')
    print(product_price)


