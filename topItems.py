import requests
from bs4 import BeautifulSoup

# set url to fetch
url = 'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/'

# Fetch url 
page = requests.get(url)

# Parse page
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items list
top_items = []

# extract and store top elements into top_items[]
products = soup.select('div.thumbnail')
for elem in products:
    title = elem.select('h4 > a.title')[0].text
    review_label = elem.select('div.ratings')[0].text
    info = {
        "title": title.strip(),
        "review": review_label.strip()
    }
    top_items.append(info)

print(top_items)