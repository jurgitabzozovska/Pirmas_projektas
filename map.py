import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import numpy as np
import seaborn as sns
import folium
m = folium.Map()
# (location =[55.74522103685154, 21.115998695107294], zoom_start=9))


tooltip = 'Klaipedos_apskritis'
tooltip_2 = 'Siauliu_apskritis'
tooltip_3 = 'Kauno_apskritis'
tooltip_4 = 'Alytaus_apskritis'
tooltip_5 = 'Marijampolės_apskritis'
tooltip_6 = 'Panevėžio_apskritis'
tooltip_7 = 'Tauragės_apskritis'
tooltip_8 = 'Telšių_apskritis'
tooltip_9 = 'Utenos_apskritis'
tooltip_10 = 'Vilniaus_apskritis'


folium.Marker([55.85769555597272, 21.201016443516764], popup ='Klaipedos_apskritis', tooltip=tooltip).add_to(m)
folium.Marker([55.93541715494644, 23.314281451279456], popup ='Siauliu_apskritis', tooltip=tooltip_2).add_to(m)
folium.Marker([54.987061474233016, 23.95325788817995], popup = 'Kauno_apskritis', tooltip = tooltip_3).add_to(m)
folium.Marker([54.29787234367851, 24.08204682928195], popup = 'Alytaus_apskritis', tooltip = tooltip_4).add_to(m)
folium.Marker([54.55393386606704, 23.354531619269398], popup = 'Marijampolės_apskritis', tooltip = tooltip_5).add_to(m)
folium.Marker([55.9751616402609, 25.0798177183858], popup = 'Panevežio_apskritis', tooltip = tooltip_6).add_to(m)
folium.Marker([55.24825227738376, 22.29501453149007], popup = 'Tauragės_apskritis', tooltip = tooltip_7).add_to(m)
folium.Marker([55.9790078321016, 22.25038452365091], popup = 'Telšių_apskritis', tooltip = tooltip_8).add_to(m)
folium.Marker([55.49987587972921, 25.60791218551143], popup = 'Utenos_apskritis', tooltip = tooltip_9).add_to(m)
folium.Marker([54.808622296543824, 25.217868210446827], popup = 'Vilnius_apskritis', tooltip = tooltip_10).add_to(m)


m.save('name.html')
#55.74522103685154, 21.115998695107294
#55.93541715494644, 23.314281451279456
# 54.899226753963404, 23.90700517624643
# 54.40144587269272, 24.0402348014765
# 54.55393386606704, 23.354531619269398
# 55.73413071383902, 24.36117277569358
# 55.24825227738376, 22.29501453149007
# 55.9790078321016, 22.250384523650915
# 55.49987587972921, 25.60791218551143
# 55.93189532554277, 23.310371928321867

df2 = pd.read_csv('Apskritis.csv')
# print(df2)
df2 = pd.DataFrame(df2)
Apskritis = df2.groupby(['Administracinė teritorija'])['Reikšmė'].sum().astype(int)
print(Apskritis)
