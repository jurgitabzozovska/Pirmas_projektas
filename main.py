import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns

csv_failo_pavadinimas = 'eismo ivykiai.csv'
df = pd.read_csv(csv_failo_pavadinimas)
print(df)

df = pd.DataFrame(df)



