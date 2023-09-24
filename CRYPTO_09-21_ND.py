import pandas as pd
from bs4 import BeautifulSoup
import requests
import psycopg2
import matplotlib.pyplot as plt
import random
import numpy as np


## 3 UŽDUOTIS
## Naudokite Beautiful Soup, kad galėtumėte „web scraping" funkcionalumą,
## kad gautumėte kriptovaliutos kainų duomenis iš populiarios kriptovaliutų rinkos svetainės.
## Išgaukite kainų, laiko ir kitus susijusius duomenis iš svetainės.
## Įkelkite gautus duomenis į Pandas DataFrame.

url = 'https://coinmarketcap.com'
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
table=soup.find("table", class_='sc-b28ea1c6-3 izgIsg cmc-table')
pavadinimai = table.find_all('th')
crypto_data =[]
for i in pavadinimai:
    pavadinimas = i.text
    crypto_data.append(pavadinimas)
    # print(antrasciu_pavadinimai)
# print(pavadinimai)
df=pd.DataFrame(columns=crypto_data)
# print(df)
rows = table.find_all('tr')
# print(rows)
for i in rows[1:]:
    duomenys=i.find_all('td')
    # print(duomenys)
    row=[tr.text for tr in duomenys]
    print(row[1:7])

## Atliekant duomenų tvarkymą, galite konvertuoti datą į tinkamą formatą,
# df.to_csv(r"C:\Users\Kursai\export_dataframe.csv", index=False, header=True)
# print(df)

## ištrinti dublikatus arba tvarkyti trūkstamas reikšmes.
# df2 = df.drop_duplicates()
# print(df2)
## Atlikite analizę, kad gautumėte statistiką apie kriptovaliutos kainų kitimą.

## Paskaičiuokite vidutines, minimalias ir maksimalias kainas, taip pat kitas statistikos vertes.
# avg = np.mean(masyvas)
# min = np.min(masyvas)
# max = np.max(masyvas)
## Sukurkite linijinį grafiką, kuris atvaizduoja kriptovaliutos kainos kitimą laike (x ašis - laikas, y ašis - kaina).
## Taip pat galite sukurti stulpelinį grafiką, kuris rodo kainos svyravimus tarp skirtingų kriptovaliutų.


