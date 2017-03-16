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
import sys

class item(object):
    def __init__(self,name,cost=-1,url=""):
        self.name=name
        self.cost=cost
        self.url=url

    def __str__(self):
        return "%s\t%d\t%s"%(self.name,self.cost,self.url)

def get_name(text):
    """Given the name in the URL with hyphens and stuff get the real name.
    """
    text = text.replace('/','')
    text = text.replace('-s-','\'s ')
    text = text.replace('-',' ')
    return text

base = "http://www.d20pfsrd.com/magic-items/magic-armor/specific-magic-armor/"
r = requests.get(base)
data = r.text
soup = bs(data,'lxml')
armors = []
names = []

#Assemble a list of all the names and urls
for link in soup.find_all('a'):
    url = link.get('href')
    if url.startswith(base) and len(url) > len(base):
        name =  get_name(url[len(base):])
        if name not in names: 
            names.append(name)
            armors.append(item(name,url=url))
            print armors[-1]

#Loop through the armors and get the costs
for armor in armors:
    soup = bs(requests.get(armor.url).text,'lxml')
    print type(soup)
    sys.exit()
    
