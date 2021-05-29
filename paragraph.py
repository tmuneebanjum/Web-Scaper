
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

#Get info from the webpages

paras = soup.find_all('p')
print(paras)
