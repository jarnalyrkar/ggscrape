from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

# Example url
url = 'http://gamlegjerpen.no/Kirkeb/Vielser/Gjerpen1810_1823.htm'

# Open connection, grab page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# Parse HTML
page_soup = soup(page_html, "html.parser")

counter = 3; # Skip irrelevant <p>'s
num_of_rows = len(page_soup.find_all('p'))

json_data = {}
json_data['marriages_1810_1823'] = []

while counter < num_of_rows:
    p = page_soup.find_all('p')[counter].get_text()

    print(len(p.splitlines()))

    if len(p.splitlines()) == 3:
        json_data['marriages_1810_1823'].append({
            "date": p.splitlines()[0],
            "bewedded": p.splitlines()[1],
            "witnesses": p.splitlines()[2]
        })
    counter += 1
    print( "Line: " + str(counter) )

with open("data.json", "w") as outfile:
    json.dump(json_data, outfile, indent=4)
