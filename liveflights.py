import requests
from bs4 import BeautifulSoup
import time

def get_count():
    url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?bounds=59.09,52.64,-58.77,-47.71&faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&maxage=7200&gliders=1&stats=1"

    # Request with fake header, otherwise you will get an 403 HTTP error
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    # Parse the JSON
    data = r.json()
    counter = 0

    # Iterate over the elements to get the number of total flights
    for element in data["stats"]["total"]:
        counter += data["stats"]["total"][element]

    return counter

while True:
    print(get_count())
    time.sleep(8)