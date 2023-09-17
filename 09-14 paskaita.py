# import pandas as pd

 # 1 užduotis
# # Sukurkite Pandas duomenų lentelę su 5 eilutėmis ir 3 stulpeliais.
# # Pavadinkite stulpelius "Vardas", "Amžius" ir "Miestas".
# duomenys = {'Vardas': ['Romas', 'Petras', 'Ona', 'Ula', 'Tonas'],
#             'Amzius': [21,25,35,62,25],
#             'Miestas': ['Vilnius', 'Kaunas', 'Kaunas', 'Utena', 'Joniskis']}
# df = pd.DataFrame(duomenys)
# print(df)
#
# ##Įtraukite naują eilutę į lentelę su duomenimis: "Jonas", 30, "Vilnius".
# df.loc[len(df.index)] = ['Jonas', 30, 'Vilnius']
# print(df)
#
# ##Išspausdinkite pirmas 3 eilutes iš lentelės.
# print(df[0:3])
#
# ##Išspausdinkite stulpelį "Amžius" visų eilučių atveju.
# print(df.Amzius)
#
# ##Atrinkite visus žmones, kurių amžius yra mažesnis nei 25.
# pagal_amziu= df[df['Amzius']<25]
# print(pagal_amziu)
#
# ##Sukurkite naują stulpelį "Gimimo metai" pagal esamą stulpelį "Amžius".
# ##Paskaičiuokite gimimo metus pagal 2023 metus.
# df['gimimo_metai'] = 2023 - df['Amzius']
# print(df)
#
# ##Ištrinkite eilutę su "Jonas" iš lentelės.
# df = df[df['Vardas'] != 'Jonas']
# print(df)
#
# ##Išsaugokite lentelę į CSV failą pavadinimu "duomenys.csv".
# # df.to_csv('duomenys.csv')
#
# ##Atrinkite visus žmones, gyvenančius Vilniuje.
# Vilniaus_gyventojai = df[df['Miestas']=='Vilnius']
# print(Vilniaus_gyventojai)
#
# import matplotlib.pyplot as plt
# plt.figure(figsize=(8,5))
# plt.bar(df['Vardas'], df['Amzius'], color='green')
# plt.xlabel('Vardas')
# plt.ylabel('Amzius')
# plt.title('Amzius pagal vardus')
# plt.show ()


# 2 užduotis
# data = {'Miestas': ['Vilnius', 'Kaunas', 'Kaunas', 'Vilnius'],
#         'Lytis':['Vyras', 'Vyras', 'Moteris', 'Vyras'],
#         'Amzius': [25, 25, 22, 30]
#         }
# detal = pd.DataFrame(data)
# vid_amzius_pagal_miesta = detal.groupby('Miestas') ['Amzius'].mean()
# print(vid_amzius_pagal_miesta)


# 3 užduotis
# ##Sukurkite Pandas DataFrame(4 miestai ir ju populiacija).
# # duomenys = {'Miestas': ['Vilnius', 'Kaunas', 'Klaip4da', 'Alytus'],
# #             'Populiacija': [300000, 250000, 200000, 150000]
# #             }
# # df = pd.DataFrame(duomenys)
# # print(df)
# # ##Filtravimas ir paieška:Filtruokite miestus, kurių populiacija yra didesnė nei 200 000 žmonių.
# # did_populiacija = df[df['Populiacija'] > 200000]
# # print(did_populiacija)
# #
# # ## Raskite miestą, turintį mažiausią populiaciją.
# # min_miestas = df[df['Populiacija']==df['Populiacija'].min()]
# # print(min_miestas)
# #
# # # Duomenų grupavimas ir agregavimas:
# # # Pridėkite stulpelį "Šalis" prie ankstesnio DataFrame, kuriame nurodoma, kuri šalis priklauso kiekvienam miestui (pvz., "Lietuva").
# # df['Salis'] = 'Lietuva'
# # print('Atnaujintas dataframe su salimi: ')
# # print(df)
# #
# # # Grupuokite duomenis pagal "Šalis" stulpelį ir apskaičiuokite bendrą populiaciją kiekvienai šaliai.
# # bendra_populiacija = df.groupby('Salis')['Populiacija'].sum()
# # print(bendra_populiacija)
# #
# # # Rikiuokite miestus pagal populiaciją mažėjimo tvarka.
# # miestai_pagal_populiacija = df.sort_values('Populiacija', ascending=False)
# # print(miestai_pagal_populiacija)
# #
# # ##Vaizinis atvaizdavimas
# # import matplotlib.pyplot as plt
# # plt.figure(figsize=(8,5))
# # plt.bar(df['Miestas'], df['Populiacija'], color='mediumturquoise')
# # plt.xlabel('Miestas')
# # plt.ylabel('Populiacija')
# # plt.title('Populiacija pagal miestu pavadinimus')
# # plt.show()

##Kazkas negerai su failo csv nuskaitymu
#csv_failo_pav = 'data-table.csv'
#df = pd. read_csv(csv_failo_pav)
#print(df.read(5))
