import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns

#
csv_failo_pavadinimas = 'eismo ivykiai.csv'
data1 = pd.read_csv(csv_failo_pavadinimas)
# print(df)
#
df1 = pd.DataFrame(data1)
df1[['Metai', 'Menuo']] = df1["Laikotarpis"].str.split('M', expand=True )
# print(df1)
# csv_failo_pavadinimas = 'neblaiviu asmenu kalte pagal apsk.csv'
# data2 = pd.read_csv(csv_failo_pavadinimas)
# # print(data2)
# df2 = pd.DataFrame(data2)
# #sujungimas dviejų csv failų
# sujungimas = pd.concat([df1, df2],ignore_index =True)
# # print(sujungimas)
# sujungimas.dropna()
#
#
# sujungimas.to_csv('sujungimas.csv', index=False)
# print("CSV file sukurtas")



# filtravimas = df2[df2['Reikšmė'] ==df2['Reikšmė'].max()]
# print(f"Daugiausiu eismo ivykiu del neblaiviu: {filtravimas}")
#
# sujungimas = df1.append(df2, ignore_index=True)
# max_value_row = sujungimas.loc[sujungimas['Reikšmė'].idxmax()]

# print(f"Daugiausiu eismo ivykiu: {max_value_row}")
#
# # csv_failo_pavadinimas = 'Pagal transporto priemones.csv'
# # data2 = pd.read_csv(csv_failo_pavadinimas)
# # print(data2)
#
#
#
# # csv_failo_pavadinimas = 'Apskritis.csv'
# # data2 = pd.read_csv(csv_failo_pavadinimas)
# # print(data2)









# # Latvijos žuvusiųjų žmonių skaičius
url = 'https://www.csdd.lv/en/road-accidents/the-road-traffic-safety-statistics'
response = requests.get(url)
# print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
data = []
table = soup.find('div', class_='table-wrapper')
headers = table.find_all("th")
# print(headers)
titles = [header.text.strip() for header in headers]
rows = table.find_all('tr')[1:]
for row in rows:

    columns = row.find_all('td')
    year = columns[0].text.strip()
    from_date_columns = columns[1:2]
    from_date = ' '.join([col.text.strip() for col in from_date_columns])
    from_date_numbers = from_date.split()

    data.append({
        'Year': year,
        'From 01.01': from_date
    })

df2 = pd.DataFrame(data, columns=titles)
# print(df2)
# df2.drop('From')
df2.to_csv('Latvija.csv', index=False)
print("CSV file sukurtas")






df3 = pd.read_csv('estijos ivykiai.csv')
print(df3)

# #sujungimas tris csv failus
# sujungimas = pd.concat([df1, df2, df3],ignore_index =True)
# print(sujungimas)
# sujungimas.to_csv('sujungimas.csv', index=False)
# print("CSV file sukurtas")

