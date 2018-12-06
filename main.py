import json
import requests

url = "https://itunes.apple.com/search?"

ArtistName = input("What's the name of artist? = ")

ArtistName= ArtistName.replace(" ","+")

params = {
    "term": ArtistName,
    "media": "music",
    "entity": "album",
    "attribute":"artistTerm",
    "limit":"10"
}

res = requests.get(url,params=params)

if res.status_code == 200:
    content = res.json()
    for c in content["results"]:
        print(c["collectionName"])