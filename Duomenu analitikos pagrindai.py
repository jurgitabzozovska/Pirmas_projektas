import pandas as pd

###### SARASO SUKURIMAS
#
# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
###### sukuriame DataFrame is saraso

# df = pd.DataFrame(duomenys)
#
###### DUOMENU FILTRAVIMAS PAGAL AMZIU
#
# jaunesni = df[df['Amzius'] <25]
## print(jaunesni)

#### VID  AMZIAUS SKAICIAVIMAS

# vidutinis_amzius = df['Amzius'].mean()
# print(f'Vidutinis amzius: {vidutinis_amzius}')

# temperaturos = [24.5, 25.2,23.8, 22.5]
# sr =pd.Series(temperaturos)
# print(sr)
# serija_rikiavimas = sr.sort_values(ascending=False)
# print(f'pirmas elementas: {sr[0]}')

######UŽDUOTIS
# duomenys = {'Vardas': ['Jonas', 'Ieva', 'Petras', 'Ona'],
#             'Amzius': [25, 28, 22, 30]
#             }
# df = pd.DataFrame(duomenys)
# # vardai = df['Vardas']
# # jeigu nori list
# vardai = df['Vardas'].to_list()
# # print('Vardai: ')
# # print(vardai)
#
######## NAUJO STULPELIO PRIDEJIMAS i Data Frame (zemiau)
#
# df['Lytis'] = ['Vyras', 'Moteris', 'Vyras', 'Moteris']
# print('Atnaujintas datarframe su nauju stulpeliu:')
# print(df)

import matplotlib.pyplot as plt

# plt.figure(figsize=(8,5))
# plt.bar(df['Vardas'], df['Amzius'], color='green')
# plt.xlabel('Vardauskai')
# plt.ylabel('Amziauskai')
# plt.title('Mano pavyko Amzius pagal vardus')
# plt.show()
#
## df.tail(2)
# df.head()