# MusicBrainz API のテスト
import requests
import json

#url = "http://musicbrainz.org/ws/2/release/05f8a9f4-2ed6-49b9-8b07-ea62879aa9b5"
url = "http://musicbrainz.org/ws/2/release"
params = {
    "fmt": "json",
    "query": "zedd",
    "limit": "1",
}


res = requests.get(url, params=params)

if res.status_code == 200:
    with open("json/ZEDD_musicbrainz.json", "w") as fp:
        json.dump(res.json(), fp, indent=2)
    print("OK")
else:
    print(res.status_code)
