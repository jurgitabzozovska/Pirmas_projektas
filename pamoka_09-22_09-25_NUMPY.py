from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2
import numpy as np


# masyvas = np.array([1,2,3,4,5])
# masyvas2 = np.array([6,2,9,4,7])
# suma = np.sum(masyvas)
# vidurkis = np.mean(masyvas)
# min = np.min(masyvas)
# max = np.max(masyvas)
#
# mediana = np.median(masyvas)
# st_dev = np.std(masyvas)
# moda = np.mod(masyvas, masyvas2)
#
# print(f'suma: {suma}, vidurkis: {vidurkis}')
# print(f'mediana: {mediana}, nuokrypis: {st_dev}, moda:{moda}')
#
# suma2 = masyvas + masyvas2
# print(suma2)
# MATRICA

# matrica = np.array([[1,2,3], [4,5,6,], [7,8,9,]])
# print(matrica)
# sum = np.sum(matrica)
# print(sum)

# matrica = np.random.randint(1,11,(4,4))
# print(matrica)
# vidurkis_matricos = np.mean(matrica)
# print(vidurkis_matricos)

## SVARBU jei reikia stulpelio vidurkio = axis=0, o jei eilutes avg = axis=1
# avg_pagal_column = np.mean(matrica, axis=0)
# avg_pagal_row = np.mean(matrica, axis=1)
# print(avg_pagal_column, avg_pagal_row)

# studentų_pazymiai = np.array([[7, 8, 9], [6, 4, 10], [10, 9, 10], [8, 8, 7]])
# studentu_avg = np.mean(studentų_pazymiai, axis = 1).round(2)
# medianos = np.median(studentų_pazymiai, axis=1)
# print(studentu_avg, medianos)
# for i in range(len(studentu_avg)):
#     print(f'studentas {i+1}: vidurkis {studentu_avg[i]}, mediana {medianos[i]}')

# masyvas33 = np.random.randint(1,51,(1,1))
# maksis = np.argmax(masyvas33)
# minis = np.argmin(masyvas33)
# print(masyvas33, '\n', maksis, minis)

# masyvas = np.array([1, 2, 3, 4, 5])
# daugiau_uz_tris = masyvas[masyvas > 3]
# print(daugiau_uz_tris)


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
