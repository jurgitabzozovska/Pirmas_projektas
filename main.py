import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns
#
# csv_failo_pavadinimas = 'eismo ivykiai.csv'
# data = pd.read_csv(csv_failo_pavadinimas)
# # print(df)
# #
# df = pd.DataFrame(data)
# # df[['Metai', 'Menuo']] = df["Laikotarpis"].str.split('M', expand=True )
# # print(df)
# filtravimas = df[df['Reikšmė'] ==df['Reikšmė'].max()]
# # print(f"Daugiausiu eismo ivykiu: {filtravimas}")
#
# csv_failo_pavadinimas = 'neblaiviu asmenu kalte pagal apsk.csv'
# data2 = pd.read_csv(csv_failo_pavadinimas)
# # print(data2)
# df = pd.DataFrame(data2)
# # filtravimas = df[df['Reikšmė'] ==df['Reikšmė'].max()]
# # print(f"Daugiausiu eismo ivykiu del neblaiviu: {filtravimas}")


# csv_failo_pavadinimas = 'Pagal transporto priemones.csv'
# data2 = pd.read_csv(csv_failo_pavadinimas)
# print(data2)
# df = pd.DataFrame(data2)

url = 'https://www.csdd.lv/en/road-accidents/the-road-traffic-safety-statistics'
#
#
response = requests.get(url)
# print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
data = []
table = soup.find_all('table', class_='table-wrapper')
# print(table)

rows = []

for row in rows[1:]:
    columns = row.find_all('td')
    Year = columns[0].text.strip()
    data.append({
            'Year':Year
                }) df = pd.DataFrame(data)

# table = soup.find('table')
# rows = []
# for i, row in enumerate(table.find_all('tr')):
#     rows.append([value.text.strip() for value in row.find_all('td')])

# if table:
#     # Initialize lists to store table data
#     data = {
#         'Year': [],
#         'number': []
#
#     }
#     # Find all rows in the table, skipping the header row
#     rows = table.find_all('tr')[1:]
#     for row in rows:
#         # Extract data from each row
#         columns = row.find_all('td')
#         if len(columns) >= 5:
#             Name = columns[1].text.strip()
#             # Append the extracted data to the lists
#             data['Year'].append('Year')
#
#     df = pd.DataFrame(data)
#     print(df)



