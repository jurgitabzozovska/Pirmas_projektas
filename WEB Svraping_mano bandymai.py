from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2

# url = "https://ticker.finology.in/"
# atsakymas = requests.get(url)
# print(atsakymas)
# soup = BeautifulSoup(atsakymas.text, 'lxml')
# table = soup.find("table", class_ = "table table-sm table-hover screenertable")
# print(table)
# headers = table.find_all("th")
# # print(headers)
# pavadinimai = []
# for i in headers:
#     pavadinimas = i.text
#     pavadinimai.append(pavadinimas)
# # print(pavadinimai)
# df = pd.DataFrame(columns=pavadinimai)
# # print(df)
# rows = table.find_all("tr")
# # print(rows)
# for i in rows[1:]:
#     # print(i.text)
#     duomenys = i.find_all("td")
#     # print(duomenys)
#     row = [tr.text for tr in duomenys]
#     # print(row)
#     l = len(df)
#     df.loc[l] = row
# print(df)

# a. Įkelkite CSV failą, kuris turi duomenis apie prekių pardavimus.
# b. Išveskite pirmas 5 eilutes iš duomenų rinkinio, kad pamatytumėte, kaip atrodo duomenys.
# c. Apskaičiuokite vidutinę prekių kainą ir vidutinį pardavimų kiekį.
# d. Pateikite grafiką, kuriame būtų pavaizduota prekių pardavimų kiekio kitimas laiko atžvilgiu.



url = "https://vaga.lt/naujos-knygos"
responce = requests.get(url)
# print(responce)
soup = BeautifulSoup(responce.text, "html.parser")
Pavadinimai = soup.find_all("p", class_="name")
Knygos_pavadinimas = []
for i in Pavadinimai:
    pavadinimas = i.text
    Knygos_pavadinimas.append(pavadinimas)
# print(Knygos_pavadinimas)
Autoriai = soup.find_all("p", class_="Autorius")
Autoriaus_vardas_pavarde = []
for i in Autoriai:
    autorius = i.text
    Autoriaus_vardas_pavarde.append(autorius)
# print(Autoriaus_vardas_pavarde)
Kaina = soup.find_all("div", class_="price price-align-wrapper")
Kainos = []
for i in Kaina:
    kaina = i.text
    Kainos.append(kaina)
# print(Kainos)
df = pd.DataFrame({"Knygos pavadinimas": Knygos_pavadinimas, "Autorius": Autoriaus_vardas_pavarde, "Kaina": Kainos})
# print(df)
df.to_csv("knygos.csv")

#
# url = "https://www.worldometers.info/world-population/population-by-country/"
# responce = requests.get(url)
# # print(responce)
# soup = BeautifulSoup (responce.text, "html.parser")
# # print(soup)
# rows = soup.find("table", {"id": "example2"}).find("tbody"). find_all("tr")
# Countries_list = []
# for row in rows:
#     dic = {}
#     dic["Country"] = row.find_all("td")[1].text
# #     dic["Popoliacija"] = row.find_all("td")[2].text.replace(",", " ")
#     Countries_list.append(dic)
# print(Countries_list)
# df = pd.DataFrame (Countries_list)
# print(df)
# # df.to_csv("Salys.csv", index=False)


