import requests

from bs4 import BeautifulSoup

url = 'https://codedamn.com'

# Fetch the page content
page = requests.get(url)

# Parse the page content from url into soup
soup = BeautifulSoup(page.content, 'html.parser')

# Create all_h1_tags as an empty list
all_h1_tags = []

# Set all_h1_tags to contain all h1 elements of the page
for element in soup.select('h1'):
    all_h1_tags.append(element.text)

# Create seventh_p_text and set to the 7th <p> element of the page
seventh_p_text = soup.select('p')[6].text

print(all_h1_tags[0], seventh_p_text)