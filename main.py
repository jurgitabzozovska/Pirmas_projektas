import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns
#
# csv_failo_pavadinimas = 'eismo ivykiai.csv'
# data = pd.read_csv(csv_failo_pavadinimas)
# # print(df)
# #
# df = pd.DataFrame(data)
# # df[['Metai', 'Menuo']] = df["Laikotarpis"].str.split('M', expand=True )
# # print(df)
# filtravimas = df[df['Reikšmė'] ==df['Reikšmė'].max()]
# print(f"Daugiausiu eismo ivykiu: {filtravimas}")

csv_failo_pavadinimas = 'neblaiviu asmenu kalte pagal apsk.csv'
data2 = pd.read_csv(csv_failo_pavadinimas)
print(data2)
df = pd.DataFrame(data2)
filtravimas = df[df['Reikšmė'] ==df['Reikšmė'].max()]
print(f"Daugiausiu eismo ivykiu del neblaiviu: {filtravimas}")





