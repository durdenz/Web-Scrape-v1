import requests

from bs4 import BeautifulSoup

url = 'https://codedamn.com'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text #gets the text of the <title>...</title> element
body = soup.body #get the text of the page body
head = soup.head

print(title)
print(head)