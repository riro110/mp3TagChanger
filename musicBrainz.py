# MusicBrainz API のテスト
import requests
import json

url = "http://musicbrainz.org/ws/2/artist/3798b104-01cb-484c-a3b0-56adc6399b80"

params = {
    "fmt": "json"
}


res = requests.get(url, params=params)

if res.status_code == 200:
    with open("json/RATM_musicbrainz.json", "w") as fp:
        json.dump(res.json(), fp, indent=2)
else:
    print(res.status_code)
