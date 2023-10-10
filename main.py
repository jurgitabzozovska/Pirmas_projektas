import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns

# #
# csv_failo_pavadinimas = 'eismo ivykiai.csv'
# data = pd.read_csv(csv_failo_pavadinimas)
# # print(df)
# #
# df = pd.DataFrame(data)
# # df[['Metai', 'Menuo']] = df["Laikotarpis"].str.split('M', expand=True )
# # print(df)
# filtravimas = df[df['Reikšmė'] ==df['Reikšmė'].max()]
# # print(f"Daugiausiu eismo ivykiu: {filtravimas}")

# csv_failo_pavadinimas = 'neblaiviu asmenu kalte pagal apsk.csv'
# data2 = pd.read_csv(csv_failo_pavadinimas)
# # print(data2)
# df = pd.DataFrame(data2)
# # filtravimas = df[df['Reikšmė'] ==df['Reikšmė'].max()]
# # print(f"Daugiausiu eismo ivykiu del neblaiviu: {filtravimas}")


# csv_failo_pavadinimas = 'Pagal transporto priemones.csv'
# data2 = pd.read_csv(csv_failo_pavadinimas)
# print(data2)



csv_failo_pavadinimas = 'Apskritis.csv'
data2 = pd.read_csv(csv_failo_pavadinimas)
# print(data2)









#Latvijos žuvusiųjų žmonių skaičius
# url = 'https://www.csdd.lv/en/road-accidents/the-road-traffic-safety-statistics'
# response = requests.get(url)
# # print(response.status_code)
# soup = BeautifulSoup(response.content, 'html.parser')
# data = []
# table = soup.find('div', class_='table-wrapper')
# headers = table.find_all("th")
# # print(headers)
# titles = [header.text.strip() for header in headers]
# rows = table.find_all('tr')[1:]
# for row in rows:
#
#     columns = row.find_all('td')
#     year = columns[0].text.strip()
#     from_date_columns = columns[1:2]
#     from_date = ' '.join([col.text.strip() for col in from_date_columns])
#     from_date_numbers = from_date.split()
#
#     data.append({
#         'Year': year,
#         'From 01.01': from_date
#     })
#
# df = pd.DataFrame(data, columns=titles)
#
# df.to_csv('Latvija.csv', index=False)
# print("CSV file sukurtas")

#
# df = pd.read_excel('Estija_ivykiai.xlsx', index_col=0)
#
# grupavimas = df.groupby('Accidents').sum()
# print(grupavimas)
