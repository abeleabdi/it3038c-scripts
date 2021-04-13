import requests, re 
from bs4 import BeautifulSoup

data = requests.get("https://shop.funimation.com/home-video/attack-on-titan-complete-season-3/BLR-00721.html").content
#print(data)
soup = BeautifulSoup(data, 'html.parser')
d = soup.find("div", {"class":"product-name"})
title = d.string.strip()

p = soup.find("span", {"class":"value"})
price = '44'

print("the item '%s' costs $%s" % (title, price))


