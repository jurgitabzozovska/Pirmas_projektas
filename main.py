import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns




# # 1#Visi keliu esimo ivykiai pagal metus(LT)
# csv_failo_pavadinimas = 'eismo ivykiai.csv'
# data1 = pd.read_csv(csv_failo_pavadinimas)
# # # print(df)
# # # #
# df1 = pd.DataFrame(data1)
# df1[['Metai', 'Menuo']] = df1["Laikotarpis"].str.split('M', expand=True)
# df1 = df1.drop(['Laikotarpis','Rodiklis','Matavimo vienetai'], axis=1)
# df1.to_csv('eismo_ivykiai.csv', index=False)
# # # print(df1)
# Suminis_grupavimas = df1.groupby('Metai')['Reikšmė'].sum()
# # print(Suminis_grupavimas)
# # # vid pagal metus
# vid = df1.groupby('Metai')['Reikšmė'].mean().round(0).astype(int)
# # print(vid)
# #
# # print(type(vid))
# #
# #change values type
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
#

# linijine
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

#
#
#
# # # #
# 2csv_failo_pavadinimas = 'Lytis.csv'
# data2 = pd.read_csv(csv_failo_pavadinimas)
# print(data2)
# df2 = pd.DataFrame(data2)
# print(df2)
# #
# Suminis_grupavimas = df2.groupby(["Amžius", 'Lytis'])['Reikšmė'].sum()
# # # print(Suminis_grupavimas)
# #
# moteru_grupavimas = df2[df2['Lytis'] == 'Moterys']
# # # print(moteru_grupavimas)
# M_group = moteru_grupavimas.groupby(['Amžius'])['Reikšmė'].sum().astype(int)
# # # # print(vid)
# # # print(M_group)
# #
# vyru_grupavimas = df2[df2['Lytis'] == 'Vyrai']
# # # print(vyru_grupavimas)
# V_group = vyru_grupavimas.groupby(['Amžius'])['Reikšmė'].sum().astype(int)
# # # print(vid)
# # # print(V_group)
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
# age = ['0-6','6–9','10–14','15–17','18–20','21–24','25–34','35–44','45–54','55–64',
# '65+']
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
# #
# # plt.xticks(1200, "Male", fontsize=25, fontweight="bold");
# # plt.xticks(1200,  "Female", fontsize=25, fontweight="bold");
# plt.xticks(range(-1200,1201,100));
# plt.show()
# # #
# #
# plt.xlabel('sužeistųjų ir žuvusiųjų skaičius',fontsize=10, fontweight="bold")
# plt.ylabel('Amžius',fontsize=10, fontweight="bold")
# plt.title("Kelių eismo įvykiuose sužeistųjų ir žuvusiųjų skaičius pagal amžių",loc="left", pad=20, fontsize=25, fontweight="bold")
# plt.xlim(-1200,1200);
#
# plt.xticks(range(-1200,1201), ["{} %". format(i) for i in range(-1200,1201)]);
# plt.legend(loc="best");
#
# plt.show()
# plt.text(-5, 17, "Male", fontsize=25, fontweight="bold");
# plt.text(4, 17, "Female", fontsize=25, fontweight="bold");
#
# for idx in range(len(population_df)):
#     plt.text(x=population_df["Male_Left"][idx]-0.1, y=idx, s="{} %".format(population_df["Male"][idx]),
#             ha="right", va="center",
#             fontsize=15, color="#4682b4");
#     plt.text(x=population_df["Female_Width"][idx]+0.1, y=idx, s="{} %".format(population_df["Female"][idx]),
#             ha="left", va="center",
#             fontsize=15, color="#ee7a87");
#
# plt.xlim(-15,15);
# plt.xticks(range(-15,16), ["{} %".format(i) for i in range(-15,16)]);
#
# plt.legend(loc="best");
#
# plt.xlabel("Percent (%)", fontsize=16, fontweight="bold")
# plt.ylabel("Age Range", fontsize=16, fontweight="bold")
# plt.title("Eismo įvykiai pagal amžių ir lytį", loc="left", pad=20, fontsize=25, fontweight="bold")
# plt.show()



csv_failo_pavadinimas = 'Pagal transporto priemones.csv'
data1 = pd.read_csv(csv_failo_pavadinimas)
print(data1)

grupuojame = data1.groupby(['Nukentėjusiųjų tipas','Kelių naudotojai'])['Reikšmė'].sum().astype(int)
print(grupuojame)
print(len(grupuojame))
print(type(grupuojame))

first_table = grupuojame.loc['Sužeistieji']
print(first_table)
second_table = grupuojame.loc['Žuvusieji']
print(second_table)

# define Seaborn color palette to use
palette_color = sns.color_palette('dark')

plt.figure(figsize=(10, 10))
plt.subplot(1,2,1)
plt.pie(first_table, colors=palette_color, autopct='%.0f%%')
plt.title('Kelių naudotojai')
plt.subplot(1,2,2)
plt.pie(second_table, colors=palette_color, autopct='%.0f%%')
plt.title('Kelių naudotojai2')
plt.legend(loc='upper left', labels=first_table.index, borderpad=0, bbox_to_anchor=(0.1, 0.1))



plt.show()



















# df2['Amžius'] = df2['Amžius'].replace('iki', '0')
# print(df2['Amžius'])
# print(type)

# #pagal lytis grupavimas
# grupavimas = df2.groupby(['Laikotarpis','Lytis'])['Reikšmė'].sum()
# # print(grupavimas)
# #pagal amžių

#


# Amzius = df2.groupby(['Amžius','Rodiklis','Lytis'])['Reikšmė'].sum().astype(int)
# print(Amzius)
# Amžius = df2['Amžius']
#
# Moterys = df2[df2['Lytis'] == "Moterys"]
# Vyrai = df2[df2["Lytis"] == 'Vyrai']
# moterys_grupavimas = Moterys.groupby('Amžius)['Reikšmė'].sum().astype(int)
#
#
#
# df2 = pd.DataFrame({"Age": [Amžius], "Male": [Vyrai], "Female": [Moterys]})
#
# print(df2)
#
# bar_plot = sns.barplot(x='Vyrai', y='Amžius', data=df2, order='Reikšmė', palette='OrRd', lw=0)
# bar_plot = sns.barplot(x='Moterys', y='Amžius', data=df2, order='Reikšmė', palette='PuBu', lw=0)
# print(bar_plot)

# bar_plot.set(xlabel="Population by sex", ylabel="Age-Group", title = "1980")
# bar_plot.set_xticklabels(labels)



# df2["Female_Left"] = 0
# df2["Female_Width"] = df2["Moterys"]
#
# df2["Male_Left"] = -df2["Vyrai"]
# df2["Male_Width"] = df2["Vyrai"]
#
# print(df2)

#
# Apskritis = df2.groupby(['Laikotarpis','Administracinė teritorija'])['Reikšmė'].sum()
# print(Apskritis)

#per 3 metus
# Apskritis2 = df2.groupby(['Administracinė teritorija'])['Reikšmė'].sum()
# print(Apskritis2)
# # #

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
