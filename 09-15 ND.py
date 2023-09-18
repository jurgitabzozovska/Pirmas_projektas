# import pandas as pd
#
#### ND_1
## Sukurkite DataFrame su mokinių pažymiais,kuriame yra stulpeliai "Vardas", "Pavardė" ir "Pažymys" (nuo 1 iki 10).
# duomenys = {'Vardas': ['Petriukas', 'Onyte', 'Jonukas', 'Maryte', 'Antanas'],
#             'Pavarde': ['Petraitis', 'Onytyte', 'Jonaitis', 'Marytyte', 'Antanaitis'],
#             'Pazymys': [10,8,6,4,2]
#             }
# df = pd.DataFrame(duomenys)
# print(df)
## Atvaizduokite tik tuos mokinius, kurių pažymys yra didesnis nei 7.
#pazymys_nuo_7 = df[df['Pazymys'] > 7]
#print(pazymys_nuo_7)
##Apskaičiuokite vidutinį pažymį visiems mokiniams;
#vid_pazymys = df['Pazymys'].mean()
#print(vid_pazymys)

#### ND_2
# ## Sukurkite DataFrame su "Prekės" stulpeliu ir "Kiekis" stulpeliu, ir kiekvienos prekės pardavimo kiekio informacija.
# duomenys = {'Preke':['Milteliai', 'Duona', 'Pienas', 'Dantu_pasta', 'Sampunas', 'Muilas'],
#             'Kiekis': [10, 30, 10, 15, 25, 35],
#             'Prekes_info': ['Chemija', 'Maistas', 'Maistas','Higiena', 'Higiena', 'Higiena']
#             }
# df = pd.DataFrame(duomenys)
# print(df)
# ## Grupuokite duomenis pagal prekes ir apskaičiuokite bendrą pardavimų kiekį kiekvienai prekei.
#
# bendras_kiekis = df.groupby('Preke')['Kiekis'].sum()
# print(bendras_kiekis)

#### ND_3
## Sukurkite Pandas DataFrame iš sąrašo žmonių duomenų su stulpeliais "Vardas", "Amžius" ir "Miestas".
## Atspausdinkite šį DataFrame.
# duomenys = {'Vardas': ['Jurgis', 'Antanas', 'Aloyzas', 'Martynas', 'Ona', 'Maryte', 'Aldona', 'Marta'],
#             'Amzius': [30, 60, 45, 15, 65, 45, 35, 20],
#             'Miestas': ['Kupiskis', 'Vilnius', 'Kaunas', 'Vilnius', 'Alytus', 'Kaunas', 'Varena', 'Vilnius']
#            }
# df = pd.DataFrame(duomenys)
# print(df)
#
# ##Filtruokite žmones, kurių amžius yra didesnis nei 25 metai ir kurie gyvena Vilniuje.
# Amzius_virs_25 = df[df['Amzius'] > 25]
# print(Amzius_virs_25)
#
# ##Surūšiuokite žmones pagal amžių didėjimo tvarka.
# Zmones_pagal_amziu = df.sort_values('Amzius')
# print(Zmones_pagal_amziu)
#
# ##Pridėkite stulpelį "Lytis" prie DataFrame ir nurodykite lytis (pvz., "Vyras" arba "Moteris").
# df['Lytis'] = 'Vyras', 'Vyras', 'Vyras', 'Vyras', 'Moteris', 'Moteris', 'Moteris', 'Moteris'
# print('Papildytas Dataframe_Lytimi')
# print(df)
#
# ##Grupuokite duomenis pagal "Lytis" stulpelį ir apskaičiuokite vidutinį amžių kiekvienai lyčiai.
# bendras_amzius = df.groupby('Lytis')['Amzius'].mean()
# print(bendras_amzius)
#
# ##Pridėkite naują žmogų į DataFrame su vardu "Laura", amžiumi 24 metai ir gyvenančią Kaune.
# df.loc[len(df.index)] = ['Laura', 24, 'Vilnius', 'Moteris']
# print(df)
#
# ##Redaguokite žmogų ir amžių padidinkite jį iki n metų.
# ## ???
#
# ##Pašalinkite žmogų iš DataFrame.
# df = df[df['Vardas'] != 'Laura']
# print(df)
# ##Išsaugokite galutinį DataFrame į CSV failą su pavadinimu "zmones.csv".
# df.to_csv('duomenys.csv')
#
##### ND_4
## Nuskaitykite duomenis iš CSV failo į Pandas lentelę.
# df = pd.read_csv('data-table.csv')
# print(df.to_string())

## Raskite miestą su daugiausia gyventojų.
# max_miestas = df.max()
## max_miestas = df[df['Reikšmė']==df['Reikšmė'].max()]
# print(max_miestas)

## Sukurkite naują lentelę, kuri rodytų miestų gyventojų skaičių pagal didėjimo tvarką.
# Gyventoju_skaicius = df.sort_values ('Reikšmė')
# print(Gyventoju_skaicius)

## Atrinkite miestus, kuriuose gyvena daugiau nei 200 000 gyventojų.
# Gyventoju_virs_200000 = df[df['Reikšmė'] > 200000]
# print(Gyventoju_virs_200000)

## Surikiuokite miestus pagal gyventojų skaičių nuo didžiausio iki mažiausio.
# Miestai_pagal_gyventoju_sk = df.sort_values('Reikšmė', ascending=False)
# print(Miestai_pagal_gyventoju_sk)

## Atrinkite miestus, kuriuose gyventojų skaičius yra tarp 100 000 ir 300 000 žmonių.
# Miestai = df[df['Reikšmė'].between(100000, 300000)]
# print(Miestai)

## Apskaičiuokite visų miestų gyventojų skaičiaus sumą ir vidurkį.
# bendra_populiacija = df.groupby('Administracinė teritorija')['Reikšmė'].sum()
# print(bendra_populiacija)

# Sukurkite lentelę, kurioje yra tik miesto pavadinimas ir gyventojų skaičius, ir išsaugokite ją atskirame CSV faile.
# duomenys = df['Administracinė teritorija'], ('Reikšmė')
# print(duomenys)