import json
import requests

url = "https://itunes.apple.com/search?"

#ArtistName = input("What's the name of artist? = ")

#ArtistName= ArtistName.replace(" ","+")
ArtistName = "RageAgainstTheMachine"

params = {
    "term": ArtistName,
    "media": "music",
    "entity":"album",
    "attribute":"artistTerm",
    "limit":"50"
}

res = requests.get(url,params=params)

if res.status_code == 200:
    content = res.json()
    with open("json/RageAgainstTheMachine.json", "w") as fp:
        json.dump(content,fp,indent=2)