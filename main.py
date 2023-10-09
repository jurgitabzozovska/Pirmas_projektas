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
table = soup.find('table', class_='table-wrapper')
Year = soup.find_all('th', class_='header')

# print(table)
if table:
    rows = table.find_all('tr')
    for row in rows[1:]:
        columns = row.find_all('td')
        year = Year[0].text.strip()
        # data = columns[0].text.strip()
    data.append({
            'Year': Year
                })

df = pd.DataFrame(data)
print(df)





