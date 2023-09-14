import pandas as pd
# data = {'Miestas': ['Vilnius', 'Kaunas', 'Kaunas', 'Vilnius'],
#         'Lytis': ['Vyras', 'Vyras', 'Moters', 'Vyras'],
#         'Amzius': [25,25,22,30]
#         }
# datal = pd.DataFrame(data)
#
# vid_amzius_pagal_miesta = datal.groupby('Miestas') ['Amzius'].mean()
# print(vid_amzius_pagal_miesta)


##  Sukurkite Pandas DataFrame(4 miestai ir ju populiacija).
##  Filtravimas ir paieška:
##  a. Filtruokite miestus, kurių populiacija yra didesnė nei 200 000 žmonių.
##  b. Raskite miestą, turintį mažiausią populiaciją.

##  Duomenų grupavimas ir agregavimas:
##  a. Pridėkite stulpelį "Šalis" prie ankstesnio DataFrame, kuriame nurodoma, kuri šalis priklauso kiekvienam miestui
##  (pvz., "Lietuva").
##  b. Grupuokite duomenis pagal "Šalis" stulpelį ir apskaičiuokite bendrą populiaciją kiekvienai šaliai.

## Duomenų rikiavimas:
## Rikiuokite miestus pagal populiaciją mažėjimo tvarka.

# duomenys = {'Miestas': ['Vilnius', 'Ryga', 'Talinas'],
#         'Populiacija': [541000, 621000, 454000]
#         }
#
# df = pd.DataFrame(duomenys)
#
# populiacijos_filtravimas = df[df['Populiacija'] > 200000]
# # print(populiacijos_filtravimas)
#
# min_miestas = df[df['Populiacija'] == df['Populiacija'].min()]
# # print(min_miestas)
#
# df['Salis'] = ['Lietuva', 'Latvija', 'Estija']
# # print('Atnaujintas datarframe su nauju stulpeliu:')
#
# bendra_populiacija = df.groupby('Salis')['Populiacija'].sum()
# # print(bendra_populiacija)
#
# miestai_pagal_populiacija = df.sort_values('Populiacija',ascending=False)
# print(miestai_pagal_populiacija)



