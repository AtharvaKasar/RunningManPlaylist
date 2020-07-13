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

try:
    token = util.prompt_for_user_token(username, scope='user-library-read')
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope='user-library-read')

# Create our spotifyObject

spotifyObject = spotipy.Spotify(auth = token)

user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))

displayName = user['display_name']
print(displayName)

followers = user['followers']['total']
print(followers)

# this is just a test, we're going to go through a playlist and give a 0 or 1 depending on if theyre in liked songs or not

def get_liked_songs():
    url = "https://api.spotify.com/v1/me/tracks"
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

    results = response_json["items"]

    arr = []

    i = 0

    while i < len(results):
        arr.append(results[i]["track"]["id"])
        # print(results[i]["track"]["id"])
        i = i + 1

    if results:
        print("we good")
        print(arr)
        return arr
    else:
        raise Exception("could not find new releases") 

def get_playlist_songs(playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    )

    response_json = response.json()

    results = response_json["items"]

    arr = []

    i = 0

    while i < len(results):
        if results[i]["track"]["id"] != None:
            arr.append(results[i]["track"]["id"])
            # print(results[i]["track"]["id"])
        i = i + 1

    if results:
        print("we good")
        print(arr)
        return arr
    else:
        raise Exception("could not find new releases") 

liked = get_liked_songs()

list_songs = get_playlist_songs("0XKAJhzULzJoV5kljqtpgf")

def get_song_info(song_id):
    url = f"https://api.spotify.com/v1/audio-features/{song_id}"
    response = requests.get(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
    )

    response_json = response.json()

    # print(json.dumps(response_json, indent=2))

    return response_json

    '''

    results = response_json["items"]

    return results

    arr = []

    i = 0

    while i < len(results):
        if results[i]["track"]["id"] != None:
            arr.append(results[i]["track"]["id"])
            print(results[i]["track"]["id"])
        i = i + 1

    if results:
        print("we good")
        print(arr)
        return arr
    else:
        raise Exception("could not find new releases") 
    '''

f = open("data.csv", 'w')
f.write("track ID, tempo, danceability, time signature, valence, target")

def write_to_file():
    a = 0
    while a < len(list_songs):
        t = 0
        curr_song = list_songs[a]
        if curr_song in liked:
            t = 1
        song_info = get_song_info(curr_song)
        print("\n")
        print("NEW SONG")
        print(song_info["id"])
        a = a + 1
        f.write("\n")
        string_to_add = song_info["id"]
        string_to_add += "," + str(song_info["tempo"])
        string_to_add += "," + str(song_info["danceability"])
        string_to_add += "," + str(song_info["time_signature"])
        string_to_add += "," + str(song_info["valence"])
        string_to_add += "," + str(t)
        print (string_to_add)
        # bruh = f"{str(song_info["id"])}, {str(song_info["tempo"])}, {str(song_info["danceability"])}, {str(song_info["time_signature"])}, {str(song_info["valence"])}, {str(t)}"
        # print(bruh)
        f.write(string_to_add)


get_song_info(list_songs[0])

write_to_file()
