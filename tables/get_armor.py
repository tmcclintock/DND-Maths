"""
Use beautiful soup to get the armor table.
"""
import requests
from bs4 import BeautifulSoup as bs

url = "http://www.d20pfsrd.com/magic-items/magic-armor/specific-magic-armor/"
r = requests.get(url)
data = r.text
soup = bs(data,'lxml')

for link in soup.find_all('a'):
    print link.get('href')
