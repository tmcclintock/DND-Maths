"""
Use beautiful soup to get the tables for armor/shield/weapons.

Algorithm is as follows, for example for the shields:
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

bases = ["http://www.d20pfsrd.com/magic-items/magic-armor/specific-magic-armor/","http://www.d20pfsrd.com/magic-items/magic-armor/specific-magic-shields/","http://www.d20pfsrd.com/magic-items/magic-weapons/specific-magic-weapons/"]
base_names = ["armor","shields","weapons"]
for base_name,base in zip(base_names,bases):
    if base_name is "armor": continue
    if base_name is "shields": continue
    #if base_name is "weapons": continue 
    r = requests.get(base)
    data = r.text
    soup = bs(data,'lxml')
    specific_items = []
    names = []

    #Assemble a list of all the names and urls
    for link in soup.find_all('a'):
        url = link.get('href')
        if url.startswith(base) and len(url) > len(base):
            name =  get_name(url[len(base):])
            if name not in names: 
                names.append(name)
                specific_items.append(item(string.capwords(name),url=url))
                #xprint specific_items[-1]

    print "Now working with %s"%base_name
    print "Working with %d items"%len(specific_items)

    #Loop through the specific_items and get the prices, and keep track of any failed items
    for i,specific_item in zip(range(len(specific_items)),specific_items):
        #if i<25 or i>27: continue
        soup = bs(requests.get(specific_item.url).text,'lxml')
        text = soup.body.text
        ind = text.find("Price")
        stext = text[ind:ind+19]
        stext = re.sub(",","",stext).encode('utf-8')
        regex = re.compile(ur"\d+")
        try:
            pricestr = regex.findall(stext)
        except Exception:
            print "Cannot run the regex: ",stext,i
            specific_item.price = 9e14
            continue
        if not pricestr:
            print "Price not found correctly here: ",stext,i
            specific_item.price = 9e14
            continue
        price = int(re.sub("[^0-9]", "", pricestr[0].encode('utf-8')))
        if price < 10:
            print "Price found to be too small:",stext,i
            specific_item.price = 9e14
            continue
        specific_item.price = price

    #Write to file
    outfile = open("%s_by_name.txt"%base_name,"w")
    for specific_item in specific_items:
        outfile.write("%s\n"%specific_item)
    outfile.close()

    sorted_specific_items = sorted(specific_items)
    outfile = open("%s_by_cost.txt"%base_name,"w")
    for i,specific_item in zip(range(len(specific_items)),sorted_specific_items):
        outfile.write("%s\n"%specific_item)
    outfile.close()
