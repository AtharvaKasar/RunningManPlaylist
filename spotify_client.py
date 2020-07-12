import requests
import urllib.parse
import json
import spotipy
import spotipy.util as util

# use spotify authentication to log in and get to/access a playlist

# create a decision tree based on already chosen songs in the running playlist

# browse through new releases and pick songs from them that would fit the decision tree characteristics?

# add those songs to the playlist

class SpotifyClient(object):

    def __init__(self, api_token, username):
        # token = input("Enter Spotify Auth Token: ")
        self.api_token = api_token
        self.spotifyObject = spotipy.Spotify(auth = util.prompt_for_user_token(username))

    def get_new_releases(self):
        url = "https://api.spotify.com/v1/browse/new-releases"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        response_json = response.json()

        print(json.dumps(response_json, indent=2))

        #right now, new releases gives us ALBUMS, but we want a bunch of songs

        results = response_json["albums"]["items"]

        if results:
            print("we good")
            print(results[0]["id"])
            print(results[0]["name"])
            return results[0]["id"]
        else:
            raise Exception("could not find new releases")


    def get_first_song_from_album(self, album_id):
        url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )

        response_json = response.json()

        print(json.dumps(response_json, indent=2))

        results = response_json["items"]

        if results:
            print("we good")
            temp = results[0]["id"]
            print(f"song id: {temp}")
            print(results[0]["name"])
            return results[0]["id"]
        else:
            raise Exception("could not find tracks")

    
    def add_one_song_to_playlist(self, playlist_id, song_id):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        print(f"SONG ID: {song_id}")
        temp = "spotify:track:" + song_id
        print(f"TEMP: {temp}")
        bruh = { "ids" : [song_id] }
        response = requests.post(
            url,
            data=json.dumps(bruh),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        print(response.text)
        print(response.ok)
        return response.ok

    def add_songs_to_playlist(self, playlist_id, song_id):
        spotipyObj = spotipy.Spotify(auth=self.api_token)
        playlist_name = "NEW PLAYLIST"    
        sp.user_playlist_create(username, name=playlist_name)



