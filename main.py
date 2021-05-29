#requirements

import requests
from bs4 import BeautifulSoup
import html5lib

url = "https://www.codewithharry.com"

# Get the HTML

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

#parse HTML

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# HTML tree Traversal

#title of html

title = soup.title
# print(title)

#Get info from the webpages

paras = soup.find_all('p')
# print(paras)

# Get all Anchors tags

anchors = soup.find_all('a')
# print(anchors)
# all.links = set()
#get first element

# print(soup.find('p'))

#get  classes of elements

# print(soup.find_all('p')['class'])

#find all he elements with class 

# print(soup.find_all("p", class_="any class name"))

#Get the text from tags/soup

# print(soup.find('p').get_text())
# print(soup.get_text())

#Get all Hrefs 
anchors = soup.find_all('a')
# print(anchors)
all_links = set()

for link in anchors:
    if(link != '#'):
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(link)
        print(linkText)

