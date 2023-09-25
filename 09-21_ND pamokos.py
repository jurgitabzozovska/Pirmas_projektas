import pandas as pd
from bs4 import BeautifulSoup
import requests
import psycopg2
import matplotlib.pyplot as plt
import random
import numpy as np

# Įkelkite failą su duomenimis iš CSV failo(amziaus_grupes) naudodami Pandas.
# Sukurkite histogramą, kuri vaizduotų žmonių pasiskirstymą pagal amžių grupes.
# Pridėkite pavadinimus ašims ir pavadinimą grafikui.
# Taip pat galite nustatyti atitinkamas spalvas ir kitus stilius, kad grafikas būtų informatyvus.

# HISTOGRAMA
data = pd.read_csv('amziaus_grupes.csv')
df = pd.DataFrame(data)
print(df)
pagal_amziu = df.groupby('Amžiaus grupė')['Žmonių skaičius'].sum()
plt.bar(pagal_amziu.index, pagal_amziu.values, color='red')
plt.xlabel('Amžiaus grupė')
plt.ylabel('Žmonių skaičius')
plt.title('žmonių pasiskirstymą pagal amžių grupes')
plt.show()


