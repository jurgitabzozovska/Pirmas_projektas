import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns

# #Visi keliu esimo ivykiai pagal metus(LT)
csv_failo_pavadinimas = 'eismo ivykiai.csv'
data1 = pd.read_csv(csv_failo_pavadinimas)
# print(df)
# #
df1 = pd.DataFrame(data1)
df1[['Metai', 'Menuo']] = df1["Laikotarpis"].str.split('M', expand=True)
df1 = df1.drop(['Laikotarpis','Rodiklis','Matavimo vienetai'], axis=1)
df1.to_csv('eismo_ivykiai.csv', index=False)
# print(df1)
Suminis_grupavimas = df1.groupby('Metai')['Reikšmė'].sum()
print(Suminis_grupavimas)
# vid pagal metus
vid = df1.groupby('Metai')['Reikšmė'].mean().round(0).astype(int)
print(vid)

print(type(vid))


w = 0.4
Metai = vid.index.to_numpy().astype(int)
print(Metai)
total = Suminis_grupavimas.values
print(total)
mean = vid.values
print(mean)
print(type(Metai))
print(Metai+w)

plt.figure(figsize=(12,5))
#Kelių eismo įvykiu kiekis ir vidurkis
Metai1 = Metai
Metai2 = Metai-w
bar1 = plt.bar(Metai1, total, width=w, label='Kiekis')
for bar in bar1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2),ha='center', va='bottom')

bar2 = plt.bar(Metai2, mean, width=w, label='Vidurkis', alpha=0.5)
for bar in bar2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2),ha='center', va='bottom')

plt.xlabel('Metai')
plt.ylabel('Reikšmė')
plt.legend(loc = 'upper left')
plt.title('Kelių eismo įvykiai pagal metus')
plt.xticks(Metai,  Metai, rotation=90)
plt.show()


#
# plt.figure(figsize=(12,5))
# plt.bar(df1.index, df1.values, color='blue')
# plt.xlabel('Metai')
# plt.ylabel('Reikšmė')
# plt.title('Kelių eismo įvykiai pagal metus')
# plt.show()


# csv_failo_pavadinimas = 'neblaiviu asmenu kalte pagal apsk.csv'
# data2 = pd.read_csv(csv_failo_pavadinimas)
# # print(data2)
# df2 = pd.DataFrame(data2)
# #sujungimas dviejų csv failų
# sujungimas = pd.concat([df1, df2],ignore_index =True)
# # print(sujungimas)
# sujungimas.dropna()
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
# csv_failo_pavadinimas = 'Apskritis.csv'
# data2 = pd.read_csv(csv_failo_pavadinimas)
# # print(data2)
# df2 = pd.DataFrame(data2)
#
# print(df2)
# #pagal lytis grupavimas
# grupavimas = df2.groupby(['Laikotarpis','Lytis'])['Reikšmė'].sum()
# # print(grupavimas)
# #pagal amžių
#
# # Amzius = df2.groupby(['Laikotarpis','Amžius','Rodiklis'])['Reikšmė'].sum()
# # print(Amzius)
#
# Apskritis = df2.groupby(['Laikotarpis','Administracinė teritorija'])['Reikšmė'].sum()
# # print(Apskritis)
#
# #per 3 metus
# Apskritis2 = df2.groupby(['Administracinė teritorija'])['Reikšmė'].sum()
# print(Apskritis2)
#

#
# # # # Latvijos žuvusiųjų žmonių skaičius
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
# df2 = pd.DataFrame(data, columns=titles)
# print(df2)
# # df2.drop('From')
# df2.to_csv('Latvija.csv', index=False)
# print("CSV file sukurtas")


#
# df3 = pd.read_csv('estijos ivykiai.csv')
# # print(df3)
# df3 = pd.DataFrame(df3)
# df3[['ivykiai','menuo']] = df3["Indicator"].str.split(' ', expand=True)
# print(df3)




# #sujungimas tris csv failus
# sujungimas = pd.concat([df1, df2, df3], ignore_index=True,)
# print(sujungimas)
# sujungimas.to_csv('sujungimas.csv', index=False)
# print("CSV file sukurtas")
#
