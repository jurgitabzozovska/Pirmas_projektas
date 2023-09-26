# import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt
# import random
#
# # # Vizualizacijos 1.pvz
# # x = [5, 8, 6, 4, 5]
# # y = [4, 3, 2, 9, 7]
# # z = [4, 6, 2, 5, 7]
# #
# # plt.plot(x, y, label='linija', color='blue', linestyle='--', marker='o')
# # plt.plot(x, z, label='linija2', color='red', linestyle='--', marker='o')
# # plt.legend()
# # plt.xlabel('x')
# # plt.ylabel('y')
# # plt.title('Grafine vizualizacija')
# # plt.show()
#
# # Vizualizacijos 2.pvz
# y = [4, 3, 2, 9, 7]
# z = [4, 6, 2, 5, 7]
# plt.step(y, z, label='pakopos', color='blue', where='mid')
# plt.fill_between(y, z, color='grey', alpha=0.5)
# plt.legend()
# plt.xlabel('z')
# plt.ylabel('y')
# plt.title('Grafine vizualizacija')
# plt.show()
#
# # Vizualizacijos 3.pvz
# # x = [1, 2, 3, 4, 5]
# # y = [10, 15, 7, 12, 9]
# # z = [4, 6, 2, 5, 7]
# # # plt.step(y, z, label = "pakopos", color = 'purple', where = "mid")
# # # plt.fill_between(y, z, color="grey", alpha = 0.5)
# # # plt.text(4,6, 'svarbus taškas', fontsize = 12, color = 'blue')
# # # plt.axhline(y = 3, color = 'green', linestyle = '--', label = "horizontali")
# # # plt.axvline(x = 5, color = 'red', linestyle = '-.', label = "vertikali")
# # # plt.clf()
# # plt.subplot(2,1,1)
# # plt.plot(x, y, label = "linija 1")
# # plt.title('Grafinė vizualizacija')
# # plt.legend()
# # plt.subplot(2,1,2)
# # plt.plot(x, [i**2 for i in y], label = 'linija2', color = 'green')
# # plt.legend()
# # plt.xlabel('z')
# # plt.ylabel('y')
# # plt.savefig('grafikas.png')
# # plt.show()
#
#
# # data = {'Stulpelis_id': [i+1 for i in range(50)],
# #         'Vardas': [random.choice(['Jonas', 'Antanas', 'Benas'])for _ in range(50)],
# #         'Alga': [random.randint(1000, 1500) for _ in range(50)]
# #         }
# # df = pd.DataFrame(data)
# # df.to_csv('Atlyginimai.csv', index=False)
#
#
# ##UŽDUOTIS Nr. 1
# # ## Įkelkite CSV failą, kuris turi duomenis apie prekių pardavimus.
# # ## Išveskite pirmas 5 eilutes iš duomenų rinkinio, kad pamatytumėte, kaip atrodo duomenys.
# # data = pd.read_csv('sales_data.csv', encoding = 'iso-8859-1')
# # df = pd.DataFrame(data)
# # print(df)
# # print(df.head(5))
# # # Apskaičiuokite vidutinę prekių kainą ir vidutinį pardavimų kiekį.
# # vidutine_kaina = df['PRICEEACH'].mean().round(2)
# # vid_pard_kiekis = df['QUANTITYORDERED'].mean()
# # print('vidutin4 kaina', vidutine_kaina)
# # print(f'\n vidutinis parduotas kiekis',  vid_pard_kiekis)
#
#
# # # Pateikite grafiką, kuriame būtų pavaizduota prekių pardavimų kiekio kitimas laiko atžvilgiu.
# # df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])
# # df['Metai'] = df['ORDERDATE'].dt.year
# # df['Mėnuo'] = df['ORDERDATE'].dt.month
# # df['Diena'] = df['ORDERDATE'].dt.day
# # print(f'\n', df)
# # Mėn_suma = df.groupby(['Metai', 'Mėnuo', 'Diena'])['QUANTITYORDERED'].sum()
# # Mėn_suma.plot(kind= 'line', color='skyblue')
# # plt.xticks(rotation = 90)
# # plt.xlabel('Data')
# # plt.ylabel('Pardavimai')
# # plt.title('pardavimų skaičius laiko atžvilgiu')
# # plt.show()
#
#
#
# ##UŽDUOTIS Nr. 2
# # Sukurkite du sąrašus: vienas su laiko žymėmis (mėnesiais nuo sausio iki gruodžio) ir
# # kitas su kas mėnesį parduotų prekių kiekiu.
#
#
# # Pavaizduokite šiuos duomenis linijiniame grafike. Pridėkite ašių pavadinimus ir pavadinimą grafiko viršuje.
#
# # Pridėkite legenda, kurioje būtų nurodyta, ką reiškia ši linija.
#
#
#
# ##UŽDUOTIS Nr. 3
# # Įkelkite kitą CSV failą su duomenimis apie studentų egzaminų rezultatus.
# data = pd.read_csv('egzaminai.csv')
# df = pd.DataFrame(data)
# print(df.head(5))
#
# # Pateikite histogramą, kuri atvaizduotų studentų matematikos egzaminų rezultatus.
# ## Sukurkite histogramą, kuri vaizduotų žmonių pasiskirstymą pagal amžių grupes.
# pagal_studentus = df.groupby('Student ID')['Math Score'].sum()
# plt.bar(pagal_studentus.index, pagal_studentus.values, color='green')
# plt.show()
#
# # Nustatykite tinkamą stulpelių (bins) skaičių, kad histograma būtų aiški ir informatyvi.
#
# # Pridėkite ašių pavadinimus ir pavadinimą grafiko viršuje.
# # plt.ylabel('Studentų sk')
# # plt.xlabel('matematikos egz')
# # plt.title('Studentų matematikos egzaminų rezultatus')
# # plt.show()
# # Duomenų grupavimas ir pie grafikas:
#
# # Grupuokite studentų egzaminų duomenis pagal lytį (vyrus ir moteris).
# # plt.figure(figsize=(12,5))
# # x = df['Math Score', 'Science score', 'English score']
# # y = df['Gender']
# # plt.xlabel('Math Score', 'Science score', 'English score')
# # plt.ylabel('Gender')
# # plt.bar(x, y)
# # plt.show()
#
#
#
# # Apskaičiuokite vidutinius rezultatus kiekvienoje grupėje.
#
# # Pateikite PIE grafiką, kuriame būtų rodoma, kiek procentų vyrų ir moterų pasiekė aukštesnius nei vidutinius rezultatus.
#
#
#
# ##UŽDUOTIS Nr. 5
# ## Sukurkite tris linijinius grafikus viename paveiksle (subplots). Kiekvienas grafikas turėtų atvaizduoti skirtingus duomenų rinkinius (pavyzdžiui, kainas skirtinguose miestuose).
# ## Kiekvienam grafikui priskirkite ašių pavadinimus, pavadinimus ir legendas.
# ## Pateikite visus tris grafikus viename paveiksle.
## 1 UŽDUOTIS
## Apskaičiuokite kiekvieno produkto mėnesinį pardavimų sumažėjimą per metus.
## Sukurkite Matplotlib grafiką, kuriame būtų pateikti šie mėnesiniai sumažėjimai kiekvienam produktui
## (x ašis - mėnesiai, y ašis - sumažėjimas, produkto pavadinimas - linijos pavadinimas).
## Pridėkite pavadinimus ašims ir bendrą pavadinimą grafikui.

# df = pd.read_csv('prekybos_duomenys.csv')
# print(df.head(5))
# df['Data'] = pd.to_datetime(df['Data'])
# df['Metai'] = df['Data'].dt.year
# df['Mėnuo'] = df['Data'].dt.month
# df['Diena'] = df['Data'].dt.day
# # print(f'\n', df)
# pagal_produkta = df.groupby(['Mėnuo','Produktas']) ['Pardavimai'].sum()
# products = df['Produktas']
# result = pd.DataFrame(columns=['Produktas', 'Metai', 'Mėnuo', 'Sumazejimas'])
# for product in products:
#     product_df=df[df['Produktas']== product]
#     for year in product_df['Metai'].unique():
#         for month in range(1,13):
#             if product_df[(product_df['Metai']==year) & (product_df['Mėnuo']==month)].shape[0]>0:
#                 sales = product_df[(product_df['Metai']==year) & (product_df['Mėnuo']==month)]['Pardavimai'].sum()
#                 if month >1:
#                     praeje_metai=year
#                     peaejes_men=month-1
#                 else:
#                     praeje_metai = year-1
#                     peaejes_men = 12
#                 pr_sales=\
#                 product_df[(product_df['Metai']==praeje_metai) & (product_df['Mėnuo']== peaejes_men)]['Pardavimai'].sum()
#                 decrease = pr_sales-sales
#                 result = pd.concat([result,pd.DataFrame([[product,year,month,decrease]],columns=result.columns)],ignore_index=True)
# print(result)
# plt.plot(result['Produktas'], result['Sumazejimas'], label='linija', color='blue', linestyle ='--', marker = 'o')
# plt.xticks(rotation=90)
# plt.legend()
# plt.xlabel('Mėnesiai')
# plt.ylabel('sumažėjimas')
# plt.title('Pardavimų mažėjimas')
# plt.show()

## 2 UŽDUOTIS
##  Išspausdinkite pirmas 5 eilutes;
## Filtruokite automobilius pagal jų kainą (pvz., kaina mažesnė nei 10 000). Išspausdinkite šiuos automobilius;
##  Suskirstykite automobilius pagal gamintoją ir susumuokite kiekvieno gamintojo automobilių kiekius.
##  Atvaizduokite stulpelinėje diagramoje automobilių kiekius;
##  Išspausdinkite pirmas 5 eilutes;
# df = pd.read_csv('automobiliai.csv')
# print(df.head(5))
# df[df['Kaina']>10000]
# print(df)
# pagal_gamintoja=df['Markė'].value_counts()
# print(pagal_gamintoja)
# pagal_gamintoja.plot(kind='bar', color = "red")
# plt.xlabel('Gamintojas')
# plt.ylabel('Kiekiai')
# plt.title('Gamintojo automobilių kiekiai')
# plt.show()
