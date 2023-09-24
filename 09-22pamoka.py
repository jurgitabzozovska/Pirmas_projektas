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