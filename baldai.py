from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2

url = 'https://bigbox.lt/15388-virtuves-reikmenys'
response = requests.get(url)
# print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
product_elements = soup.find_all('div', class_='&nbsp')

product_data = []
for product_element in product_elements:
    product_name = product_element.find_all('div', class_='product-title').text.strip()
    product_price = float(product_element.find('span', class_='price-value').text.strip().replace('€', ''))
    product_quantity = product_element.find('b').text.strip()[:1]
    print(f"Adding products to the list: {product_name}")
