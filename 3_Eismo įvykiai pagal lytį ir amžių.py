# # 3. EISMO ĮVYKIAI PAGAL LYTĮ IR AMŽIŲ

import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns

# #  CSV FAILO ĮKĖLIMAS
csv_failo_pavadinimas = 'Darbo_failai/Lytis.csv'
data2 = pd.read_csv(csv_failo_pavadinimas)
print(data2)
df2 = pd.DataFrame(data2)
print(df2)
# #
# #  DUOMENŲ GRUPAVIMAS
# Suminis_grupavimas = df2.groupby(["Amžius", 'Lytis'])['Reikšmė'].sum()
# print(Suminis_grupavimas)

# # #  MOTERŲ GRUPAVIMAS
moteru_grupavimas = df2[df2['Lytis'] == 'Moterys']
# print(moteru_grupavimas)
M_group = moteru_grupavimas.groupby(['Amžius'])['Reikšmė'].sum().astype(int)

# print(M_group)

# # #  VYRŲ GRUPAVIMAS
vyru_grupavimas = df2[df2['Lytis'] == 'Vyrai']
# print(vyru_grupavimas)
V_group = vyru_grupavimas.groupby(['Amžius'])['Reikšmė'].sum().astype(int)

# print(V_group)

M_Age = M_group.index.to_numpy()
# print(M_Age)
V_Age = V_group.index.to_numpy()
# print(V_Age)
total_M = M_group.values
# print(total_M)
total_V = V_group.values
# print(total_V)
#
age = ['0-6','6–9','10–14','15–17','18–20','21–24','25–34','35–44','45–54','55–64','65+']
Male = [130, 162, 278, 385, 364, 436, 1118, 895, 699, 630, 527]
Female = [92, 133, 234, 203, 231, 312, 551, 518, 585, 643, 948]
Viso_moterų= sum(Male)
print(Viso_moterų)
Viso_vyrų = sum(Female)
print(Viso_vyrų)

population_df = pd.DataFrame({"Age": age, "Male": Male, "Female": Female})
population_df["Female_Left"] = 0
population_df["Female_Width"] = population_df["Female"]
population_df["Male_Left"] = -population_df["Male"]
population_df["Male_Width"] = population_df["Male"]
print(population_df)

# GRAFINIS ATVAIZDAVIMAS

fig = plt.figure(figsize=(15,10))
plt.barh(y=population_df["Age"], width=population_df["Female_Width"], color="#ee7a87", label="Female");
plt.barh(y=population_df["Age"], width=population_df["Male_Width"], left=population_df["Male_Left"],
        color="#4682b4", label="Male");
female_color = '#ee7a87'
male_color = '#4682b4'
plt.xticks(range(-1200,1201,250));
plt.xlabel('Sužeistųjų ir žuvusiųjų skaičius',fontsize=10, fontweight="bold")
plt.ylabel('Amžius',fontsize=10, fontweight="bold")
plt.title("Kelių eismo įvykiuose sužeistųjų ir žuvusiųjų skaičius pagal amžių ir lytį",loc="left", pad=20, fontsize=16,
        fontweight="bold")
plt.xlim(-1200,1200);
plt.text(-5, 17, "Male", fontsize=25, fontweight="bold");
plt.text(4, 17, "Female", fontsize=25, fontweight="bold");
plt.show()