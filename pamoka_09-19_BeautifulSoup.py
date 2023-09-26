from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
# import time()
import pandas as pd
from bs4 import BeautifulSoup
import requests
import psycopg2
# url = 'http://www.meteo.lt/en/miestas?placeCode=Vilnius'
# response = requests.get(url)
# print(response.status_code)
# soup = BeautifulSoup(response.content, 'html.parser')
# forecast = soup.find_all('div', class_='forecast-day')
# week_days = soup.find_all('span', class_='date')
# # ima kas antr1 temperatura
# day_temperature = soup.find_all('span', class_='big up-from-zero')[1::2]
# print(week_days, day_temperature)
# filtered_week_days = [week_day.get_text().split(",")[0] for week_day in week_days]
# day_temperatures= []
# for temperature in day_temperature:
#     temp_text = temperature.get_text().replace('°C', '')
#     temp_value = int(temp_text[:-1])
#     day_temperatures.append(temp_value)
# print(day_temperatures)
# data={'weekday':filtered_week_days, 'temperature':day_temperatures}
# df=pd.DataFrame(data)
# print(df)
# max_temperature=df['temperature'].max()
# min_temperature=df['temperature'].min()
# import matplotlib.pyplot as plt
# plt.figure(figsize=(12,5))
# plt.bar('auksciausia temperatura', max_temperature, color='red')
# plt.bar('zemiausi temperatura', min_temperature, color='blue')
# plt.ylabel('temperatura: °C' )
# plt.title('Auksciausir ir zemiausia temperatura VLN')
# plt.show()
# vid = df['temperature'].mean()
# print(df2)

### UZDUOTIS
# import matplotlib.pyplot as plt
# proc = [90,10,45,60,70]
# pasiekimai = ['matematika', 'istorija', 'fizika', 'anglu', 'biologija']
# spalvos = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
# ex = (0.1,0,0,0,0)
# plt.pie(proc, explode=ex, labels=pasiekimai, colors=spalvos, autopct='%1.1f%%', startangle=140)
# plt.title('pasiekimu diagrama')
# plt.axis('equal')
# plt.show()


# data = pd.read_csv('COVID.csv')
# df = pd.DataFrame(data)
# print(df)


# Apskaičiuokite vidutini užsikrėtusiu virusu skaičių per savaitę;
# sav_mean = df['Susirgimu_sk'].mean()
# print(f'Vid_uzsikretimu_sk:', sav_mean)

# Atvaizduokite grafike kaip skiriasi užsikretusiu skaičius per mėnesį;


# Apskaičiuokite ir atvaizduokite,kuri mėnesį buvo daugiausiai užsikrėtimų;
# max_susirgimu = df['Weekly COVID-19 Hospital Admissions'].max()
# print(max_susirgimu)

# Atvaizuokite kiekvieno mėnesio užsikrėtimų skaičių(procentaliai)lyginant su praėjusiu mėnesiu. PIE grafike;

def create_and_insert_product():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="products",
        user="postgres",
        password="truputukas1982"
    )
    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS varle_products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        price DECIMAL(10,2),
        quantity INT)
    """
    cursor.execute(create_table_query)
    print('Table created successfully')
    url = 'https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/'
    response = requests.get(url)
    # print(response.status_code)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_elements = soup.find_all('div', class_='GRID_ITEM')
    # print(product_elements)
    product_data = []
    for product_element in product_elements:
        product_name = product_element.find('div', class_='product-title').text.strip()
        product_price = float(product_element.find('span', class_='price-value').text.strip().replace('€', ''))
        product_quantity = product_element.find('b').text.strip()[:1]
        # print(f'Adding products to the list: {product_name}')
        # time.sleep(2)
        # product_data.append((product_name, product_price, product_quantity))
        # insert_query = "INSERT INTO varle_products (name, price, quantity) VALUES(%s, %s, %s)"
        # cursor.execute(insert_query, (product_name, product_price, product_quantity))
        # print(f'Products inserted into list succesfully!')
        connection.commit()
    # df=pd.DataFrame(product_data, columns=['name', 'price', 'quantity'])
    # print(df)
    select_query = "SELECT * FROM varle_products"
    cursor.execute(select_query)
    rows = cursor.fetchall()
    df=pd.DataFrame(rows, columns = ['id', 'name', 'price', 'quantity'])
    print(df)
if __name__ =='__main__':
    create_and_insert_product()