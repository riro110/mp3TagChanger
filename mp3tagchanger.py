import os
import re
from mutagen.easyid3 import EasyID3

path = input("曲が入っているフォルダのパス＝")
path = path.replace("\\","/")
print(path)
path_list = os.listdir(path) #編集したいmp3が入ったフォルダの中身一覧
path_list = [mp3 for mp3 in path_list if "mp3" in mp3]

print(path_list)
pattern1 = r"^([0-9]+)(\s|-)(.*).mp3$"
pattern2 = r"(\\).*"
Arbum = path.split("/")[-1]
Artist = path.split("/")[-2]

print("Arbum:",Arbum,"Artist:",Artist)
for mp3 in path_list:
    result = re.match(pattern1,mp3)
    trackNo = result.group(1)
    title = result.group(3)
    print("No.",trackNo,"Title",title)

    tags = EasyID3(path+"/"+mp3)
    tags['title'] = title
    tags["album"] = Arbum
    tags["artist"] = Artist
    tags["albumartist"] = Artist
    tags["tracknumber"] = trackNo
    tags.save()
