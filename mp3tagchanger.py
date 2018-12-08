import os
import glob
import re
from mutagen.easyid3 import EasyID3
from mutagen.easymp4 import EasyMP4
from itunesAPI import iTunesSearchAPI
import json

path = input("Musicフォルダのパス＝")
path = path.replace("\\", "/")

def mp3TagChange(path):
print(path) 

path_list = os.listdir(path)  # 編集したいmp3が入ったフォルダの中身一覧
path_list = [mp3 for mp3 in path_list if ("mp3" or "m4a") in mp3]

print(path_list)

pattern1 = r"^([0-9]+)(\s|-)(.*).mp3$"
pattern2 = r"(\\).*"

Arbum = path.split("/")[-1]
Artist = path.split("/")[-2]

print("Arbum:", Arbum, "Artist:", Artist)
try:
    itunes = iTunesSearchAPI()
    tracklist = itunes.tracklist(Artist, Arbum)
except:

print(json.dumps(tracklist, indent=2))

sure = input("Are you OK?[y/n]\n")
if sure == "y":
    pass
else:
    exit(1)
    

for mp3 in path_list:
    result = re.match(pattern1, mp3)
    trackNo = result.group(1)
    title = result.group(3)
    print("No.", trackNo, "Title", title)
    tags = None
    if "mp3" in mp3:
        tags = EasyID3(path+"/"+mp3)
    if "m4a" in mp3:
        tags = EasyMP4
    tags['title'] = title
    tags["album"] = Arbum
    tags["artist"] = Artist
    tags["albumartist"] = Artist
    tags["tracknumber"] = trackNo
    tags.save()
