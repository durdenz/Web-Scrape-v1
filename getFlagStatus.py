import requests
import re
from bs4 import BeautifulSoup
def getFlagStatus():
    # set url to fetch
    url = 'https://starsandstripesdaily.org/'

    # Fetch url 
    page = requests.get(url)

    # Parse page
    soup = BeautifulSoup(page.content, 'html.parser')

    # extract and store target div into statusDiv[]

    statusDiv = str(soup.select('div.disclose')[0])
    dateDiv = str(soup.select('h3.date')[0])

    flagDate = re.sub(r'\<.*?\>','', dateDiv)
    flagDate = flagDate.strip()

    # Check if statusDiv contains FULL STAFF
    if (statusDiv.find('FULL') >= 0):
        flagStatus = "Full Staff"
    elif (statusDiv.find('HALF') >= 0):
        flagStatus = "Half Staff"
    else:
        flagStatus = "Error"

    flagURL = '../static/flag-widget.jpg'

    print(flagStatus)
    print(flagDate)
    print(flagURL)

    flagInfo = {
        "Status" : flagStatus,
        "Date" : flagDate,
        "FlagURL" : flagURL
    }

    return(flagInfo)
