from bs4 import BeautifulSoup
import requests
import os

WIKI_URL = "https://no.wikipedia.org/wiki/USAs_delstater"
BASE_IMG_PAGE_URL = "https://no.wikipedia.org/"

result = []

response = requests.get(WIKI_URL)

soup = BeautifulSoup(response.content, "lxml")

table = soup.find(attrs={"class": "wikitable"})

rows = table.tbody.find_all("tr")
for row in rows[1:]:
    cells = row.find_all("td")
    stateName = cells[1].getText().strip()
    stateUrl = BASE_IMG_PAGE_URL + cells[5].find("a").get("href").strip()

    imgPageRes = requests.get(stateUrl)
    imgPageSoup = BeautifulSoup(imgPageRes.content, "lxml")

    imgUrl = "https:" + imgPageSoup.find(attrs={"class": "fullImageLink"}).a.get("href").strip()

    fileName = os.path.abspath(".\\media\\" + stateName + ".svg")
    
    with open(fileName, "x+b") as file:
        res = requests.get(imgUrl)
        file.write(res.content)
        print("Downloading state map: " + stateName)
