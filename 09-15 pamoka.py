# # 1 Užduotis
# # Sukurkite Pandas duomenų lentelę su 5 eilutėmis ir 3 stulpeliais.
# # Pavadinkite stulpelius "Vardas","Amžius"ir"Miestas".
# import pandas as pd
# duomenys = {'Vardas': ['Romas', 'Petras', 'Ona', 'Ula', 'Tonas'],
#             'Amzius': [21,25,35,62,25],
#             'Miestas': ['Vilnius', 'Kaunas', 'Kaunas', 'Utena', 'Joniskis']}
#
# df = pd.DataFrame(duomenys)
# # print(df)
# # Įtraukite naują eilutę į lentelę su duomenimis: "Jonas", 30, "Vilnius".
# df.loc[len(df.index)] = ['Jonas', 30, 'Vilnius']
# print(df)
# # Išspausdinkite pirmas 3 eilutes iš lentelės.
# print(df[0:3])
# # Išspausdinkite stulpelį "Amžius" visų eilučių atveju.
# print(df.Amzius)
# # Atrinkite visus žmones, kurių amžius yra mažesnis nei 25.
# pagal_amziu= df[df['Amzius']<25]
# print(pagal_amziu)
# # Sukurkite naują stulpelį "Gimimo metai" pagal esamą stulpelį "Amžius". Paskaičiuokite gimimo metus pagal 2023 metus.
# df['gimimo_metai'] = 2023 - df['Amzius']
# print(df)
# # Ištrinkite eilutę su "Jonas" iš lentelės.
# df = df[df['Vardas'] != 'Jonas']
# print(df)
# # Išsaugokite lentelę į CSV failą pavadinimu "duomenys.csv".
# df.to_csv('duomenys.csv')
# # Atrinkite visus žmones, gyvenančius Vilniuje.
# Vilniaus_gyventojai = df[df['Miestas']=='Vilnius']
# print(Vilniaus_gyventojai)
