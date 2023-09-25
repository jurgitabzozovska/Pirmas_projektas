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

# UZDUOTIS
# sujungti 2 masyvus i viena horizontaliai
masyvas = np.random.randint(1, 10, 10)
masyvas_2 = np.arange(1,50,10)
# print(masyvas, "\n", masyvas_2)
masyvas_3 = np.hstack((masyvas, masyvas_2))
# print(masyvas_3)
