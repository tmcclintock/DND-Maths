"""
Use beautiful soup to get the shield table.

Algorithm is as follows:
1. get all the links on the shield page
2. figure out all the shield names from the links and keep them both
3. navigate to each shield's page and find the price (tricky)
4. sort on the prices
5. print the whole thing to a text file with the entry style: Name Price URL

"""
import requests
from bs4 import BeautifulSoup as bs
import re #regular expressions for cleaning up badly formatted prices
import sys, string

class item(object):
    def __init__(self,name,price=-1,url=""):
        self.name=name
        self.price=price
        self.url=url

    def __str__(self):
        return "%s\t%d\t%s"%(self.name,self.price,self.url)

    def __cmp__(self,y):
        return cmp(self.price,y.price)

def get_name(text):
    """Given the name in the URL with hyphens and stuff get the real name.
    """
    text = text.replace('/','')
    text = text.replace('-s-','\'s ')
    text = text.replace('-',' ')
    return text

base = "http://www.d20pfsrd.com/magic-items/magic-armor/specific-magic-shields/"
r = requests.get(base)
data = r.text
soup = bs(data,'lxml')
shields = []
names = []

#Assemble a list of all the names and urls
for link in soup.find_all('a'):
    url = link.get('href')
    if url.startswith(base) and len(url) > len(base):
        name =  get_name(url[len(base):])
        if name not in names: 
            names.append(name)
            shields.append(item(string.capwords(name),url=url))
            #xprint shields[-1]

#Loop through the shields and get the prices, and keep track of any failed items
for i,shield in zip(range(len(shields)),shields):
    soup = bs(requests.get(shield.url).text,'lxml')
    if i < 2:continue
    try:
        gpstr = soup.body.find(string="Price").findParent().nextSibling.encode('utf-8')
    except Exception:
        print "Messed up format for: %s at index:%d"%(shield,i)
        shield.price = 9e14 #Huge number
        continue
    gpstr = gpstr.replace(',','')
    gpstr = gpstr.replace(' gp','')
    gpstr = re.sub("[^0-9]", "",gpstr)
    try: #Something crazy happened
        shield.price = int(gpstr)
    except Exception:
        print "This entry fails: \'%s\' \tindex:%d\tshield:%s'"%(gpstr,i,shield.name)
        shield.price = 9e14 #Huge number
        continue

#Write to file
outfile = open("shields_by_name.txt","w")
for shield in shields:
    outfile.write("%s\n"%shield)
outfile.close()

sorted_shields = sorted(shields)
outfile = open("shields_by_cost.txt","w")
for i,shield in zip(range(len(shields)),sorted_shields):
    outfile.write("%s\n"%shield)
outfile.close()
