from bs4 import BeautifulSoup
import requests
import pandas as pd
### VARIANTAI:
##define URL link variable, get the response, and parse the HTML dom contents
# url = "https://coinmarketcap.com"
# response = requests.get(url).text
# soup = BeautifulSoup(response, 'html.parser')
# ## declare table variable and use soup to find table in HTML dom
# table = soup.find('table')
# if table:
# ## Initialize lists to store table data
#     data = {
#         'Name': [],
#         'Price': [],
#         '1h Change': [],
#         '24h Change': [],
#         '7d Change': [],
#         'Market Cap': [],
#         'Volume (24h)': [],
#     }
# ## Find all rows in the table, skipping the header row
#     rows = table.find_all('tr')[1:]
#     for row in rows:
# ## Extract data from each row
#         columns = row.find_all('td')
#         if len(columns) >= 8:
#             Name = columns[2].text.strip()
#             Price = columns[3].text.strip()
#             change_1h = columns[4].text.strip()
#             change_24h = columns[5].text.strip()
#             change_7d = columns[6].text.strip()
#             Market_Cap = columns[7].text.strip()
#             Volume_24h = columns[8].text.strip()
# ##Append the extracted data to the lists
#             data['Name'].append(Name)
#             data['Price'].append(Price)
#             data['1h Change'].append(change_1h)
#             data['24h Change'].append(change_24h)
#             data['7d Change'].append(change_7d)
#             data['Market Cap'].append(Market_Cap)
#             data['Volume (24h)'].append(Volume_24h)
# ## Create a DataFrame from the extracted data
#     df = pd.DataFrame(data)
# ## Print the first 20 rows of the DataFrame
#     print(df)

###VARIANTAS
# url = 'https://coinmarketcap.com'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
#
# data = []
# table = soup.find('table', attrs={'class':'cmc-table'})
# cols = table.find('thead').find_all('th')
# cols = [ele.text.strip() for ele in cols]
# data.append([ele for ele in cols if ele])
#
# lentele = table.find('tbody')
#
# # print(lentele)
#
# rows = lentele.find_all('tr')
# for row in rows:
#     cols = row.find_all('td')
#
#     print(cols)
#     colsTemp = []
#
#
# #     #
#     for i, col in enumerate(cols):
#         if i == 2 and len(col.findAll('p')) > 1:
#             colsTemp.append(col.findAll('p')[0].text + " " + col.findAll('p')[1].text)
#         elif i == 7 and len(col.findAll('span')) > 0:
#             span = col.findAll('span')
#             colsTemp.append(span[1].text if len(span) > 1 else span[0].text)
#         else:
#             colsTemp.append(col.text.strip())
#
#     cols = colsTemp
#     data.append([ele for ele in cols if ele]) # Get rid of empty values
#
# df = pd.DataFrame(data)
#
# print(df.head(n=20))
#
# df.to_csv('Crypto.csv', index=False)
#
# df = pd.read_csv('Crypto.csv')