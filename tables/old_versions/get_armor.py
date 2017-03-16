"""
Use beautiful soup to get the armor table.

Algorithm is as follows:
1. get all the links on the armor page
2. figure out all the armor names from the links and keep them both
3. navigate to each armor's page and find the price (tricky)
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
            armors.append(item(string.capwords(name),url=url))
            #xprint armors[-1]

#Loop through the armors and get the prices, and keep track of any failed items
for i,armor in zip(range(len(armors)),armors):
    soup = bs(requests.get(armor.url).text,'lxml')
    try:
        gpstr = soup.body.find(string="Price").findParent().nextSibling.encode('utf-8')
    except Exception:
        print "Messed up format for: %s"%armor,i
        continue
    gpstr = gpstr.replace(',','')
    gpstr = gpstr.replace(' gp','')
    gpstr = re.sub("[^0-9]", "",gpstr)
    try: #Something crazy happened
        armor.price = int(gpstr)
    except Exception:
        print "This entry fails: \'%s\' \tindex:%d\tarmor:%s'"%(gpstr,i,armor.name)
        armor.price = 9e14 #Huge number
        continue

#Write to file
outfile = open("armors_by_name.txt","w")
for armor in armors:
    outfile.write("%s\n"%armor)
outfile.close()

sorted_armors = sorted(armors)
outfile = open("armors_by_cost.txt","w")
for i,armor in zip(range(len(armors)),sorted_armors):
    outfile.write("%s\n"%armor)
outfile.close()
