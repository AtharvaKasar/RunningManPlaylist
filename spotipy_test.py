import os
import sys
import spotipy
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyOAuth
import requests
import urllib.parse

# gets the username

# the username is passed as a parameter to the script manually, and it's the 1st element, 0th being name of script itself
username = sys.argv[1]

# User ID for Facebook users 22bg3h2b6ayxzpr44gma45eqy?si=cK5FiLjrTPuRSx3P3AmDPw

# Erase cache and prompt for user permission

try:
    token = util.prompt_for_user_token(username, scope='playlist-modify-public')
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope='playlist-modify-public')

# Create our spotifyObject

spotifyObject = spotipy.Spotify(auth = token)

user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))

displayName = user['display_name']
print(displayName)

followers = user['followers']['total']
print(followers)

def get_new_releases():
    url = "https://api.spotify.com/v1/browse/new-releases"
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    )

    response_json = response.json()

    # print(json.dumps(response_json, indent=2))

    #right now, new releases gives us ALBUMS, but we want a bunch of songs

    results = response_json["albums"]["items"]

    if results:
        print("we good")
        print(results[0]["id"])
        print(results[0]["name"])
        return results[0]["id"]
    else:
        raise Exception("could not find new releases")   

new_id = get_new_releases()

def get_first_song_from_album(album_id):
    url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    )

    response_json = response.json()

    # print(json.dumps(response_json, indent=2))

    results = response_json["items"]

    if results:
        print("we good")
        temp = results[0]["id"]
        print(f"song id: {temp}")
        print(results[0]["name"])
        return results[0]["id"]
    else:
        raise Exception("could not find tracks")

first = get_first_song_from_album(new_id)

first = [first]

print(first)

spotifyObject.user_playlist_create(user, name="SAMPLE LIST")

spotifyObject.user_playlist_add_tracks(user, "5aTTAzxyQ2xBVJz4WmdCx2", first)

'''
def add_song_to_playlist(playlist_id, tracks):
    spotifyObject.user_playlist_add_tracks(user, playlist_id, tracks)

add_song_to_playlist("5aTTAzxyQ2xBVJz4WmdCx2", first)
'''
    