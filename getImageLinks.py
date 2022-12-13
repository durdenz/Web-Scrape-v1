import requests
from bs4 import BeautifulSoup

# set url to fetch
url = 'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/'

# Fetch url 
page = requests.get(url)

# Parse page
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items list
image_links = []

# extract and store top elements into top_items[]
images = soup.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')

    image_links.append({"src":src, "alt":alt})

print(image_links)