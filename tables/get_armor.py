"""
Use beautiful soup to get the armor table.

Algorithm is as follows:
1. get all the links on the armor page
2. figure out all the armor names from the links and keep them both
3. navigate to each armor's page and find the cost (tricky)
4. sort on the costs
5. print the whole thing to a text file with the entry style: Name Cost URL

"""
import requests
from bs4 import BeautifulSoup as bs

url = "http://www.d20pfsrd.com/magic-items/magic-armor/specific-magic-armor/"
r = requests.get(url)
data = r.text
soup = bs(data,'lxml')

for link in soup.find_all('a'):
    print link.get('href')
