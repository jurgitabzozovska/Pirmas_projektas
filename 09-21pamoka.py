import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import random

## 1 UŽDUOTIS
## Apskaičiuokite kiekvieno produkto mėnesinį pardavimų sumažėjimą per metus.
## Sukurkite Matplotlib grafiką, kuriame būtų pateikti šie mėnesiniai sumažėjimai kiekvienam produktui
## (x ašis - mėnesiai, y ašis - sumažėjimas, produkto pavadinimas - linijos pavadinimas).
## Pridėkite pavadinimus ašims ir bendrą pavadinimą grafikui.

# df = pd.read_csv('prekybos_duomenys.csv')
# print(df.head(5))
# df['Data'] = pd.to_datetime(df['Data'])
# df['Metai'] = df['Data'].dt.year
# df['Mėnuo'] = df['Data'].dt.month
# df['Diena'] = df['Data'].dt.day
# # print(f'\n', df)
# pagal_produkta = df.groupby(['Mėnuo','Produktas']) ['Pardavimai'].sum()
# products = df['Produktas']
# result = pd.DataFrame(columns=['Produktas', 'Metai', 'Mėnuo', 'Sumazejimas'])
# for product in products:
#     product_df=df[df['Produktas']== product]
#     for year in product_df['Metai'].unique():
#         for month in range(1,13):
#             if product_df[(product_df['Metai']==year) & (product_df['Mėnuo']==month)].shape[0]>0:
#                 sales = product_df[(product_df['Metai']==year) & (product_df['Mėnuo']==month)]['Pardavimai'].sum()
#                 if month >1:
#                     praeje_metai=year
#                     peaejes_men=month-1
#                 else:
#                     praeje_metai = year-1
#                     peaejes_men = 12
#                 pr_sales=\
#                 product_df[(product_df['Metai']==praeje_metai) & (product_df['Mėnuo']== peaejes_men)]['Pardavimai'].sum()
#                 decrease = pr_sales-sales
#                 result = pd.concat([result,pd.DataFrame([[product,year,month,decrease]],columns=result.columns)],ignore_index=True)
# print(result)
# plt.plot(result['Produktas'], result['Sumazejimas'], label='linija', color='blue', linestyle ='--', marker = 'o')
# plt.xticks(rotation=90)
# plt.legend()
# plt.xlabel('Mėnesiai')
# plt.ylabel('sumažėjimas')
# plt.title('Pardavimų mažėjimas')
# plt.show()




