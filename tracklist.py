
"""
アルバムidからトラックリスト入手
"""

import json
import requests
url = "https://itunes.apple.com/lookup?"

params = {
    "id":"191450810",   #collectionid
    "entity":"song"
}

res = requests.get(url,params=params)

if res.status_code == 200:
    content = res.json()
    with open("json/RageAgainstTheMachine_Album.json", "w") as fp:
        json.dump(content,fp,indent=2)