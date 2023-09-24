from bs4 import BeautifulSoup
import requests
import pandas as pd
import psycopg2

url = 'https://www.livinn.lt/vaikams/sauskelnes-ir-serveteles'
response = requests.get(url)
print(response.status_code)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)

class="item"
