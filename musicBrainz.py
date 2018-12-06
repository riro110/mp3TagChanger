#MusicBrainz API のテスト
import requests
import json

url = "http://musicbrainz.org/ws/2/search?"

params = {
    "query": "Rage+Against+The+Machine",
    "type":"artist"
}


res = requests.get(url,params=params)

if res.status_code == 200:
    with open("json/RATM_musicbrainz.json", "w") as fp:
        json.dump(res.json(),fp,indent=2)