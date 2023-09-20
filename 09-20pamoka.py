# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
# import random

# # Vizualizacijos 1.pvz
# x = [5, 8, 6, 4, 5]
# y = [4, 3, 2, 9, 7]
# z = [4, 6, 2, 5, 7]
#
# plt.plot(x, y, label='linija', color='blue', linestyle='--', marker='o')
# plt.plot(x, z, label='linija2', color='red', linestyle='--', marker='o')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Grafine vizualizacija')
# plt.show()

# Vizualizacijos 2.pvz
# y = [4, 3, 2, 9, 7]
# z = [4, 6, 2, 5, 7]
# plt.step(y, z, label='pakopos', color='blue', where='mid')
# plt.fill_between(y, z, color='grey', alpha=0.5)
# plt.legend()
# plt.xlabel('z')
# plt.ylabel('y')
# plt.title('Grafine vizualizacija')
# plt.show()

# Vizualizacijos 3.pvz
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 7, 12, 9]
# z = [4, 6, 2, 5, 7]
# # plt.step(y, z, label = "pakopos", color = 'purple', where = "mid")
# # plt.fill_between(y, z, color="grey", alpha = 0.5)
# # plt.text(4,6, 'svarbus taškas', fontsize = 12, color = 'blue')
# # plt.axhline(y = 3, color = 'green', linestyle = '--', label = "horizontali")
# # plt.axvline(x = 5, color = 'red', linestyle = '-.', label = "vertikali")
# # plt.clf()
# plt.subplot(2,1,1)
# plt.plot(x, y, label = "linija 1")
# plt.title('Grafinė vizualizacija')
# plt.legend()
# plt.subplot(2,1,2)
# plt.plot(x, [i**2 for i in y], label = 'linija2', color = 'green')
# plt.legend()
# plt.xlabel('z')
# plt.ylabel('y')
# plt.savefig('grafikas.png')
# plt.show()


# data = {'Stulpelis_id': [i+1 for i in range(50)],
#         'Vardas': [random.choice(['Jonas', 'Antanas', 'Benas'])for _ in range(50)],
#         'Alga': [random.randint(1000, 1500) for _ in range(50)]
#         }
# df = pd.DataFrame(data)
# df.to_csv('Atlyginimai.csv', index=False)


##UŽDUOTIS Nr. 1
# ## Įkelkite CSV failą, kuris turi duomenis apie prekių pardavimus.
# ## Išveskite pirmas 5 eilutes iš duomenų rinkinio, kad pamatytumėte, kaip atrodo duomenys.
# import pandas as pd
# import matplotlib as pdb
# import matplotlib.pyplot as plt
# data = pd.read_csv('sales_data.csv', encoding = 'iso-8859-1')
# df = pd.DataFrame(data)
# print(df.head(5))
# # Apskaičiuokite vidutinę prekių kainą ir vidutinį pardavimų kiekį.
# vidutine_kaina = df['PRICEEACH'].mean().round(2)
# vid_pard_kiekis = df['QUANTITYORDERED'].mean()
# print('vidutin4 kaina', vidutine_kaina)
# print(f'\n vidutinis parduotas kiekis',  vid_pard_kiekis)


# # Pateikite grafiką, kuriame būtų pavaizduota prekių pardavimų kiekio kitimas laiko atžvilgiu.
# df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
# df['Metai'] = df['ORDERDATE'].dt.year
# df['Mėnuo'] = df['ORDERDATE'].dt.month
# df['Diena'] = df['ORDERDATE'].dt.day
# print(f'\n', df)
# Mėn_suma = df.groupby(['Metai', 'Mėnuo', 'Diena'])['QUANTITYORDERED'].sum()
# Mėn_suma.plot(kind= 'line', color='skyblue')
# plt.xticks(rotation = 90)
# plt.xlabel('Data')
# plt.ylabel('Pardavimai')
# plt.title('pardavimų skaičius laiko atžvilgiu')
# plt.show()



##UŽDUOTIS Nr. 2
# Sukurkite du sąrašus: vienas su laiko žymėmis (mėnesiais nuo sausio iki gruodžio) ir kitas su kas mėnesį parduotų prekių kiekiu.

# Pavaizduokite šiuos duomenis linijiniame grafike. Pridėkite ašių pavadinimus ir pavadinimą grafiko viršuje.

# Pridėkite legenda, kurioje būtų nurodyta, ką reiškia ši linija.



##UŽDUOTIS Nr. 3
# Įkelkite kitą CSV failą su duomenimis apie studentų egzaminų rezultatus.
import pandas as pd
import matplotlib as pdb
import matplotlib.pyplot as plt
data = pd.read_csv('egzaminai.csv')
df = pd.DataFrame(data)
print(df.head(5))

# Pateikite histogramą, kuri atvaizduotų studentų matematikos egzaminų rezultatus.
df.hist()
plt.show(column='Math')

# Nustatykite tinkamą stulpelių (bins) skaičių, kad histograma būtų aiški ir informatyvi.

# Pridėkite ašių pavadinimus ir pavadinimą grafiko viršuje.

# Duomenų grupavimas ir pie grafikas:

# Grupuokite studentų egzaminų duomenis pagal lytį (vyrus ir moteris).

# Apskaičiuokite vidutinius rezultatus kiekvienoje grupėje.

# Pateikite PIE grafiką, kuriame būtų rodoma, kiek procentų vyrų ir moterų pasiekė aukštesnius nei vidutinius rezultatus.



##UŽDUOTIS Nr. 5
# Sukurkite tris linijinius grafikus viename paveiksle (subplots). Kiekvienas grafikas turėtų atvaizduoti skirtingus duomenų rinkinius (pavyzdžiui, kainas skirtinguose miestuose).

# Kiekvienam grafikui priskirkite ašių pavadinimus, pavadinimus ir legendas.

# Pateikite visus tris grafikus viename paveiksle.