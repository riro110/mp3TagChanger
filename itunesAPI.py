import json
import requests


class iTunesSearchAPI():
    """
    itunesでアーティストとアルバムを検索しトラックリストを取得
    """

    search_url = "https://itunes.apple.com/search?"
    lookup_url = "https://itunes.apple.com/lookup?"

    def __init__(self):
        self.ArtistName = ""
        self.AlbumName = ""

    def search(self, artistName, albumName):
        """
        アーティスト名で検索
        """

        self.AlbumName = albumName
        self.ArtistName = artistName

        self.ArtistName = self.ArtistName.replace(" ", "+")  # 検索用に変形

        params = {
            "term": self.ArtistName,
            "media": "music",
            "entity": "album",
            "attribute": "artistTerm",
            "limit": "50"
        }

        res = requests.get(iTunesSearchAPI().search_url, params=params)

        if res.status_code == 200:
            content = res.json()
            #print(json.dumps(content["results"], indent=2))
            if len(content["results"]) == 0:
                raise NotFoundError("アルバムが見つかりませんでした")

            return content

        else:
            res.raise_for_status()

    def tracklist(self, artistName, albumName):
        albumlist = self.search(artistName, albumName)

        collectionid = ""

        for album in albumlist["results"]:
            if album["collectionName"].lower() == albumName.lower():
                collectionid = str(album["collectionId"])
                break

        params = {
            "id": collectionid,  # collectionid
            "entity": "song"
        }
        res = requests.get(iTunesSearchAPI().lookup_url, params=params)

        if res.status_code == 200:
            content = res.json()
            if len(content["results"]) == 0:
                raise NotFoundError("アルバムが見つかりませんでした")

            content = self.make_tracklist(content["results"])
            return content

        else:
            res.raise_for_status()

    def make_tracklist(self, json_list):
        """
        トラックリストに必要な情報を整理
        """
        track_list = {
            "AlbumName": "",
            "ArtistName": "",
            "Genre": "",
            "trackCount": "",
            "date": "",
            "songs": []
        }
        album = json_list[0]
        songs = json_list[1:]
        if album["collectionName"]:
            track_list["AlbumName"] = album["collectionName"]

        if album["artistName"]:
            track_list["ArtistName"] = album["artistName"]

        if album["primaryGenreName"]:
            track_list["Genre"] = album["primaryGenreName"]

        if album["trackCount"]:
            track_list["trackCount"] = str(album["trackCount"])

        if album["releaseDate"]:
            track_list["date"] = album["releaseDate"].split("-")[0]

        for song in songs:
            song_dict = {
                "title": "",
                "artist": "",
                "trackNumber": "",
                "discCount": "",
                "discNumber": ""
            }

            if song["trackName"]:
                song_dict["title"] = song["trackName"]

            if song["artistName"]:
                song_dict["artist"] = song["artistName"]

            if song["trackNumber"]:
                song_dict["trackNumber"] = song["trackNumber"]

            if song["discCount"]:
                song_dict["discCount"] = song["discCount"]

            if song["discNumber"]:
                song_dict["discNumber"] = song["discNumber"]

            track_list["songs"].append(song_dict)

        return track_list


class NotFoundError(Exception):
    "検索しても見つからない"

    def __init__(self, message):
        self.message = message


"""
if __name__ == "__main__":
    itunes = iTunesSearchAPI()
    tracklist = itunes.tracklist(
        "80kidz", "80:05 - Single")
    print(json.dumps(tracklist, indent=2))
"""
