import requests
from bs4 import BeautifulSoup

# set url to fetch
url = 'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/'

# Fetch url 
page = requests.get(url)

# Parse page
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items list
all_links = []

# extract and store top elements into top_items[]
links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''

    all_links.append({"href":href, "text":text})

print(all_links)