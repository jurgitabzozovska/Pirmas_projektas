import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import random
import numpy as np


# # ## Įkelkite CSV failą, kuris turi duomenis apie prekių pardavimus.
# # ## Išveskite pirmas 5 eilutes iš duomenų rinkinio, kad pamatytumėte, kaip atrodo duomenys.
df = pd.read_csv('Butai22.csv')
data = pd.DataFrame(df)
print(data)


# kaina = df['Kaina']
# kv_kaina = df['Kv_kaina']
# adresas = df["Adresas"]
# # x = np.arange(len(kaina))
# plt.barx=adresas, y=kaina, hue = 'kv_kaina')
# plt.show()

# data = pd.read_csv('amziaus_grupes.csv')
# df = pd.DataFrame(data)
# print(df)
# pagal_amziu = df.groupby('Amžiaus grupė')['Žmonių skaičius'].sum()
# plt.bar(pagal_amziu.index, pagal_amziu.values, color='red')
# plt.xlabel('Amžiaus grupė')
# plt.ylabel('Žmonių skaičius')
# plt.title('žmonių pasiskirstymą pagal amžių grupes')
# plt.show()