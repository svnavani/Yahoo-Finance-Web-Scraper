import requests 
from bs4 import BeautifulSoup
import pandas as pd 

stock = 'SGEN'
URL = 'https://finance.yahoo.com/quote/' + stock + '/key-statistics?p=' + stock
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')
table_data = soup.find_all('td')

df = pd.DataFrame(columns=['Metric Name', 'Metric'])
    
for data in range(0, len(table_data) - 1, 2):
    df = df.append({'Metric Name' : table_data[data].text, 'Metric' : table_data[data + 1].text} , ignore_index=True)

return df