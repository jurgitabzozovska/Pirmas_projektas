## Užduotis
## Įkelkite failą su duomenimis iš CSV failo naudodami Pandas.
# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
# import random
# data = pd.read_csv('amziaus_grupes.csv')
# df = pd.DataFrame(data)
# print(df)

## Sukurkite histogramą, kuri vaizduotų žmonių pasiskirstymą pagal amžių grupes.
# pagal_amziu = df.groupby('Amžiaus grupė')['Žmonių skaičius'].sum()
# plt.figure(figsize=(12,5))
# plt.bar(pagal_amziu.index, pagal_amziu.values, color='green')
# plt.show()
## Pridėkite pavadinimus ašims ir pavadinimą grafikui.
# plt.xlabel('Amžiaus grupė')
# plt.ylabel('Žmonių skaičius')
# plt.title('Žmonių pasiskirstymas pagal amžių grupes')
# plt.show()
## Taip pat galite nustatyti atitinkamas spalvas ir kitus stilius, kad grafikas būtų informatyvus.