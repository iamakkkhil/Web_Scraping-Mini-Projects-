"""
Extracting Infobox data from Wikipedia
Dependencies = BeautifulSoup, requests

NOTE : class name of infobox table will change according to URL
"""


from bs4 import BeautifulSoup
import requests

res = requests.get("https://en.wikipedia.org/wiki/Barack_Obama")

# To check whether the url is valid or not
if res.status_code == 200:

    # converting our data into html
    soup = BeautifulSoup(res.text, "html.parser")

    # class name is where the our data is present and class name will change for every wikipedia url
    table = soup.find('table', class_='infobox vcard')

    # to store the data in dictionary
    result = {}

    # Grabbing data row by row
    for tr in table.find_all('tr'):
        if tr.find('th'):

            try:
                result[tr.find('th').text] = tr.find('td').text
            except AttributeError:
                pass

    # For printing our extracted data
    for x, y in result.items():
        print(x, " : ", y)

# Invalid url
else:
    print("Invalid URL")
