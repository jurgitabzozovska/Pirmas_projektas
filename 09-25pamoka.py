from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
import numpy as np

# masyvas = np.arange(1, 11)
# # print(masyvas)
# suma = np.sum(masyvas)
# # print(suma)
# dvimatis_masyvas = masyvas.reshape(2,5)
# # print(dvimatis_masyvas)
# # atsp visus lyginius dk - nuliais
# naujas_masyvas = masyvas[masyvas %2 == 0]
# # print(naujas_masyvas)
#
# UZDUOTIS
# # masyvas_3 = masyvas [masyvas>5]
# # print(masyvas_3)
# masyvas = np.random.randint(1,101,(5,5))
# # print(masyvas)
# max_masyvas = np.max(masyvas)
# # print(max_masyvas)
# min_masyvas = np.min(max_masyvas)
# # print(min_masyvas)
# # Apsukti nuo galo eilutes
# nezinomas = np.flipud(masyvas)
# # print(nezinomas)
# # Apsukti stulpelis
# stulpelis = masyvas[:,::-1]
# # print(stulpelis)

# # UZDUOTIS
# #ujungti 2 masyvus i viena horizontaliai
# masyvas = np.random.randint(1, 10, 10)
# masyvas_2 = np.arange(1,50,10)
# print(masyvas, "\n", masyvas_2)
# masyvas_3 = np.hstack((masyvas, masyvas_2))
# # print(masyvas_3)

## KLASĖS DARBAS
## Sukurkite masyvą nuo 0 iki 9 ir jį pertvarkykite į 3x3 masyvą;
# masyvas = np.arange(0, 9)
# # print(masyvas)
# masyvas_3 = masyvas.reshape(3, 3)
# print(masyvas_3)

# Sukurkite 5x5 masyvą su atsitiktinėmis reikšmėmis ir raskite vidurkį kiekvieno stulpelio;
# masyvas_5 = np.random.randint(1,101,(5,5))
# print(masyvas_5)
# stulpeliu_avg = np.average(masyvas_5,axis=0)
# print(stulpeliu_avg)

# # Sukurkite 6x6 masyvą su skaičiais nuo 1 iki 36 ir transformuokite jį į 2D masyvą (matricą) 3x12;
# masyvas_6 = np.arange(1, 37)
# print(masyvas_6)
# masyvas2D = masyvas_6.reshape(3,12)
# print(masyvas2D)

# Sukurkite masyvą su atsitiktinėmis reikšmėmis nuo 0 iki 1 ir raskite jo visų elementų vidurkį.
# Toliau paverskite mažesnes reikšmes į 0 ir didesnes į 1.
# masyvas = np.random.randint(1)
# print(masyvas)


# Sukurkite du masyvus pirmas_masyvas ir antras_masyvas, kiekvieną su 5 atsitiktinėmis reikšmėmis nuo 1 iki 10,
# ir sudėkite juos taip, kad naujas masyvas turėtų visų reikšmių kvadratus.
# pirmas_masyvas = np.random.randint(1,11, (5))
# antras_masyvas = np.random.randint(1,11, (5))
# naujas_masyvas = pirmas_masyvas + antras_masyvas
# print(naujas_masyvas)
# print("Naujas masyvas kvadratu of naujas_masyvas:", np.square(naujas_masyvas))

