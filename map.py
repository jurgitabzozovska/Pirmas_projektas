import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns
import folium
m = folium.Map(location =[55.74522103685154, 21.115998695107294], zoom_start = 9)


tooltip = 'Klaipedos_apskritis'
tooltip_2 = 'Siauliu_apskritis'

folium.Marker([55.74522103685154, 21.115998695107294], popup ='Klaipedos_apskritis', tooltip=tooltip).add_to(m)
folium.Marker([55.93541715494644, 23.314281451279456], popup ='Siauliu_apskritis', tooltip=tooltip).add_to(m)

m.save('name.html')
#55.74522103685154, 21.115998695107294
#55.93541715494644, 23.314281451279456


#
# df2 = pd.read_csv('Apskritis.csv')
# # print(df2)
# df2 = pd.DataFrame(df2)
# Apskritis = df2.groupby(['Administracinė teritorija'])['Reikšmė'].sum().astype(int)
# # print(Apskritis)
