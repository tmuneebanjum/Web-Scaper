
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

elem = soup.select('.model-footer')

print(elem)