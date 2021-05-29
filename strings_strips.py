
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

# .contents - a tag's childerns are available as a list
# .contents - a tag's childerns are available as a generator

navbarSupportedContent =  soup.find(id = 'navbarSupportedContent')
for item in navbarSupportedContent.stripped_strings:
    print(item)
