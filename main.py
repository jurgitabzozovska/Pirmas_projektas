
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns
import pandas as pd
import folium

# # # # # 1#Visi keliu esimo ivykiai pagal metus(LT)
# csv_failo_pavadinimas = 'eismo ivykiai.csv'
# data1 = pd.read_csv(csv_failo_pavadinimas)
# print(data1)
#
# df1 = pd.DataFrame(data1)
# df1[['Metai', 'Menuo']] = df1["Laikotarpis"].str.split('M', expand=True)
# df1 = df1.drop(['Laikotarpis','Rodiklis','Matavimo vienetai'], axis=1)
# print(df1)
# # # #
# Suminis_grupavimas = df1.groupby('Metai')['Reikšmė'].sum()
# print(Suminis_grupavimas)
# # vid pagal metus
# vid = df1.groupby('Metai')['Reikšmė'].mean().round(0).astype(int)
# print(vid)
# # # # #
# # # print(type(vid))
# # #change values type
# w = 0.4
# Metai = vid.index.to_numpy().astype(int)
# print(Metai)
# total = Suminis_grupavimas.values
# print(total)
# mean = vid.values
# print(mean)
# print(type(Metai))
# print(Metai+w)
#
# plt.figure(figsize=(12,5))
# #Kelių eismo įvykiu kiekis ir vidurkis
# Metai1 = Metai
# Metai2 = Metai-w
# bar1 = plt.bar(Metai1, total, width=w, label='Visi kelių eismo įvykiai')
# for bar in bar1:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2),ha='center', va='bottom')
# bar2 = plt.bar(Metai2, mean, width=w, label='Vidurkis', alpha=0.5)
# for bar in bar2:
#     yval = bar.get_height()
#     plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2),ha='center', va='bottom')
#
# plt.xlabel('Metai')
# plt.ylabel('Reikšmė')
# plt.legend(loc='upper left')
# plt.title('Kelių eismo įvykiai ir jų vidurkis pagal metus')
# plt.xticks(Metai,  Metai)
# plt.show()


# #2. neblaiviu ivykiai pagal metus nuo min iki max
# csv_failo_pavadinimas = 'neblaiviu_ivykiai_pagal menesius_metus.csv'
# data3 = pd.read_csv(csv_failo_pavadinimas)
# print(data3)
# df3 = pd.DataFrame(data3)
# df3[['Metai', 'Menuo']] = df3["Laikotarpis"].str.split('M', expand=True)
# print(df3)
# df3 = df3.drop(['Laikotarpis'], axis=1)
# print(df3)
# x = df3['Metai']
# y = df3['Reikšmė']
# plt.plot(x, y, label = 'įvykiai', color = 'pink', linestyle = '', marker = 'o')
# plt.legend()
# plt.xlabel('Metai')
# plt.ylabel('Įvykių skaičius')
# plt.title('Kelių eismo įvykiai, kuriuose nukentėjo žmonės dėl neblaivių asmenų')
# plt.show()

#
# #3 ivykiai pagal lyti ir amziu
# csv_failo_pavadinimas = 'Lytis.csv'
# data2 = pd.read_csv(csv_failo_pavadinimas)
# print(data2)
# df2 = pd.DataFrame(data2)
# print(df2)
#
# Suminis_grupavimas = df2.groupby(["Amžius", 'Lytis'])['Reikšmė'].sum()
# # # print(Suminis_grupavimas)
# moteru_grupavimas = df2[df2['Lytis'] == 'Moterys']
# # # print(moteru_grupavimas)
# M_group = moteru_grupavimas.groupby(['Amžius'])['Reikšmė'].sum().astype(int)
# print(M_group)
# # #
# vyru_grupavimas = df2[df2['Lytis'] == 'Vyrai']
# # # print(vyru_grupavimas)
# V_group = vyru_grupavimas.groupby(['Amžius'])['Reikšmė'].sum().astype(int)
# # # print(vid)
# print(V_group)
#
# M_Age = M_group.index.to_numpy()
# print(M_Age)
# V_Age = V_group.index.to_numpy()
# print(V_Age)
# total_M = M_group.values
# print(total_M)
# total_V = V_group.values
# print(total_V)
#
# age = ['0-6','6–9','10–14','15–17','18–20','21–24','25–34','35–44','45–54','55–64','65+']
# Male = [130, 162, 278, 385, 364, 436, 1118, 895, 699, 630, 527]
# Female = [92, 133, 234, 203, 231, 312, 551, 518, 585, 643, 948]
#
# population_df = pd.DataFrame({"Age": age, "Male": Male, "Female": Female})
# population_df["Female_Left"] = 0
# population_df["Female_Width"] = population_df["Female"]
# population_df["Male_Left"] = -population_df["Male"]
# population_df["Male_Width"] = population_df["Male"]
# print(population_df)
#
# female_color = '#ee7a87'
# male_color = '#4682b4'
# #
# fig = plt.figure(figsize=(15,10))
# #
# plt.barh(y=population_df["Age"], width=population_df["Female_Width"], color="#ee7a87", label="Female");
#
# plt.barh(y=population_df["Age"], width=population_df["Male_Width"], left=population_df["Male_Left"],
#         color="#4682b4", label="Male");
# # plt.show()
#
# plt.xticks(range(-1200,1201,250));
# plt.xlabel('sužeistųjų ir žuvusiųjų skaičius',fontsize=10, fontweight="bold")
# plt.ylabel('Amžius',fontsize=10, fontweight="bold")
# plt.title("Kelių eismo įvykiuose sužeistųjų ir žuvusiųjų skaičius pagal amžių",loc="left", pad=20, fontsize=25, fontweight="bold")
# plt.xlim(-1200,1200);
#
# plt.text(-5, 17, "Male", fontsize=25, fontweight="bold");
# plt.text(4, 17, "Female", fontsize=25, fontweight="bold");
# plt.show()
# #
# #
# # #4suzeistuju ir zuvusiuju skaicius per 3 metus pagal dalyvius
# csv_failo_pavadinimas = 'Pagal transporto priemones.csv'
# data1 = pd.read_csv(csv_failo_pavadinimas)
# print(data1)
# # #
# grupuojame = data1.groupby(['Nukentėjusiųjų tipas','Kelių naudotojai'])['Reikšmė'].sum().astype(int)
# print(grupuojame)
# # print(len(grupuojame))
# print(type(grupuojame))
#
# first_table = grupuojame.loc['Sužeistieji']
# print(first_table)
# second_table = grupuojame.loc['Žuvusieji']
# print(second_table)
# # #
# # define Seaborn color palette to use
# palette_color = sns.color_palette('colorblind')
# ex=(0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1)
# plt.figure(figsize=(12,12))
# plt.subplot(1,2,1)
# plt.pie(first_table, colors=palette_color, autopct='%.0f%%', explode = ex)
# plt.title('Kelių eismo įvykiuose sužeistųjų skaičius',fontsize=12)
#
# plt.subplot(1,2,2)
# plt.pie(second_table, colors=palette_color, autopct='%.0f%%',explode = ex)
# plt.title('Kelių eismo įvykiuose žuvusiųjų skaičius',fontsize = 12)
# plt.legend(loc='upper center', labels=first_table.index, borderpad=0, bbox_to_anchor=(0.1, 0.1))
# plt.show()
# # # #
# #5 eismo įvykių per 3 metus pagal apskritis
# df2 = pd.read_csv('Apskritis.csv')
# # print(df2)
# df2 = pd.DataFrame(df2)
# Apskritis = df2.groupby(['Administracinė teritorija'])['Reikšmė'].sum().astype(int)
# print(Apskritis)
#
# m = folium.Map(location=[55.55267395452089, 23.962904604687534], zoom_start=8)
#
# locations = [
#     {
#         'coordinates': [55.85769555597272, 21.201016443516764],
#         'tooltip': 'Klaipedos_apskritis',
#         'value': 1360,
#     },
#     {
#         'coordinates': [55.93541715494644, 23.314281451279456],
#         'tooltip': 'Siauliu_apskritis',
#         'value': 924,
#     },
#     {
#         'coordinates': [54.987061474233016, 23.95325788817995],
#         'tooltip': 'Kauno_apskritis',
#         'value': 2251,
#     },
#     {
#         'coordinates': [54.29787234367851, 24.08204682928195],
#         'tooltip': 'Alytaus_apskritis',
#         'value': 478,
#     },
#     {
#         'coordinates': [54.55393386606704, 23.354531619269398],
#         'tooltip': 'Marijampolės_apskritis',
#         'value': 387,
#     },
#     {
#         'coordinates': [55.9751616402609, 25.0798177183858],
#         'tooltip': 'Panevežio_apskritis',
#         'value': 1029,
#     },
#     {
#         'coordinates': [55.24825227738376, 22.29501453149007],
#         'tooltip': 'Tauragės_apskritis',
#         'value': 280,
#     },
#     {
#         'coordinates': [55.9790078321016, 22.25038452365091],
#         'tooltip': 'Telšių_apskritis',
#         'value': 482,
#     },
#     {
#         'coordinates': [55.49987587972921, 25.60791218551143],
#         'tooltip': 'Utenos_apskritis',
#         'value': 356,
#     },
#
#     {
#         'coordinates': [54.808622296543824, 25.217868210446827],
#         'tooltip': 'Vilnius_apskritis',
#         'value': 2590,
#     }]
#
# for location in locations:
#     folium.Marker(
#         location=location['coordinates'],
#         popup=f"Įvykiai: {location['value']}",
#         tooltip=location['tooltip'],
#
#     ).add_to(m)
#
#
# folium.Marker(
#         location=location['coordinates'],
#         icon=folium.DivIcon(html=f'<div>{location["value"]}</div>'),
#     ).add_to(m)
#
# m.save('name2.html')


# 5# Žuvusiujų skaičius Baltijos šalyse per...
#
#
# # # # Latvijos žuvusiųjų žmonių skaičius
url = 'https://www.csdd.lv/en/road-accidents/the-road-traffic-safety-statistics'
response = requests.get(url)
# print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
data = []
table = soup.find('div', class_='table-wrapper')
# print(table)
headers = table.find_all("th")
# print(headers)
titles = [header.text.strip() for header in headers][:2]
# print(titles)
rows = table.find_all('tr')[1:]
# print(rows)
rows = rows[:-1]
for row in rows[1:]:


    columns = row.find_all('td')
    year = columns[0].text.strip()
    from_date_columns = columns[1:]
    from_date = ' '.join([col.text.strip() for col in from_date_columns])
    from_date_numbers = from_date.split()

    # print(from_date)
    # print(from_date_numbers)
    # break

    data.append({
        'Year': year,
        'From 01.01': from_date_numbers[1]
    })
#
df2 = pd.DataFrame(data, columns=titles)
df2 = df2.tail(3)
print(df2)


#
# #
# #
#
df3 = pd.read_csv('estijos zuve.csv')
# # print(df3)
df3 = pd.DataFrame(df3)
# # print(df3)
df3 = df3.drop(0)
# # print(df3)
Sum = df3.groupby('Indicator').sum()
sum = pd.DataFrame(Sum)
sum.drop('Month',axis=1, inplace=True)
sum = sum.transpose()
# print(sum.columns)
print(sum)
#
#
data4 = pd.read_csv('Lietuvos zuve.csv')
# print(data4)

df4 = pd.DataFrame(data4)
# print(df4)
df4[['Metai', 'Menuo']] = df4["Laikotarpis"].str.split('M', expand=True)
# print(df4)
df4 = df4.drop(['Laikotarpis','Rodiklis','Matavimo vienetai'], axis=1)
# print(df4)
Suminis_grupavimas2 = df4.groupby('Metai')['Reikšmė'].sum()
print(Suminis_grupavimas2)

#
#
Metai = Suminis_grupavimas2.index.astype(int)
print(Metai)
Lietuva = Suminis_grupavimas2.values
print(Lietuva)
#
Latvija = df2["From 01.01"].to_numpy().astype(int)
print(Latvija)
#
Estija = [i[0] for i in sum.values]
print(Estija)
# #
plt.figure(figsize=(8,8))
w = 0.4
Metai1 = Metai
Metai2 = Metai - w
Metai3 = Metai + w

bar1 = plt.bar(Metai, Lietuva, width=w, label='Lietuva', color='mediumseagreen')
bar2= plt.bar(Metai - w, Latvija, width=w, label='Latvija', color='tomato')
bar3 = plt.bar(Metai + w, Estija, width=w, label='Estija', color='royalblue')
for bars in [bar1, bar2, bar3]:
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, round(yval, 2), ha='center', va='bottom')
plt.xlabel('Metai')
plt.ylabel('Ivykiai')
plt.legend(loc='upper left')
plt.title('2022 -2020 m. Baltijos šalių eismo įvykių žuvusiųjų skaičius')
plt.xticks(Metai,  Metai)
plt.show()