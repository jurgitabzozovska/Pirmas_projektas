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
# # print(week_days, day_temperature)
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