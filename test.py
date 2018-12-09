from mutagen.easyid3 import EasyID3
import os

"""
tagがついてないmp3を含むディレクトリのリストを返す
"""

dir_list = []

path = input("path=")

path = path.replace("\\", "/")

artist_list = os.listdir(path)
album_list = []
for artist in artist_list:
    album_list = os.listdir(path+"/"+artist)
    for album in album_list:
        if os.path.isdir(album) == False:
            continue
        music_list = [s for s in os.listdir(
            path+"/"+artist+"/"+album) if s.endswith("mp3")]
        #print(album, music_list)
        if music_list == []:
            continue
        tags = EasyID3(path+"/"+artist+"/"+album+"/"+music_list[0])
        if tags["title"] == "":
            dir_list.append(path+"/"+artist+"/"+album)

print(dir_list)
