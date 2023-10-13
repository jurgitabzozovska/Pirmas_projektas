import folium
import pandas as pd

m = folium.Map(location=[55.55267395452089, 23.962904604687534], zoom_start=8)

locations = [
    {
        'coordinates': [55.85769555597272, 21.201016443516764],
        'tooltip': 'Klaipedos_apskritis',
        'įvykiai': 1360,
    },
    {
        'coordinates': [55.93541715494644, 23.314281451279456],
        'tooltip': 'Siauliu_apskritis',
        'įvykiai': 924,
    },
    {
        'coordinates': [54.987061474233016, 23.95325788817995],
        'tooltip': 'Kauno_apskritis',
        'value': 2251,
    },
    {
        'coordinates': [54.29787234367851, 24.08204682928195],
        'tooltip': 'Alytaus_apskritis',
        'value': 478,
    },
    {
        'coordinates': [54.55393386606704, 23.354531619269398],
        'tooltip': 'Marijampolės_apskritis',
        'value': 387,
    },
    {
        'coordinates': [55.9751616402609, 25.0798177183858],
        'tooltip': 'Panevežio_apskritis',
        'value': 1029,
    },
    {
        'coordinates': [55.24825227738376, 22.29501453149007],
        'tooltip': 'Tauragės_apskritis',
        'value': 280,
    },
    {
        'coordinates': [55.9790078321016, 22.25038452365091],
        'tooltip': 'Telšių_apskritis',
        'value': 482,
    },
    {
        'coordinates': [55.49987587972921, 25.60791218551143],
        'tooltip': 'Utenos_apskritis',
        'value': 356,
    },

    {
        'coordinates': [54.808622296543824, 25.217868210446827],
        'tooltip': 'Vilnius_apskritis',
        'value': 2590,
    }]

for location in locations:
    folium.Marker(
        location=location['coordinates'],
        popup=f"Value: {location['įvykiai']}",
        tooltip=location['tooltip'],

    ).add_to(m)


folium.Marker(
        location=location['coordinates'],
        icon=folium.DivIcon(html=f'<div>{location["įvykiai"]}</div>'),
    ).add_to(m)

m.save('name2.html')



df2 = pd.read_csv('Apskritis.csv')
# print(df2)
df2 = pd.DataFrame(df2)
Apskritis = df2.groupby(['Administracinė teritorija'])['Reikšmė'].sum().astype(int)
print(Apskritis)