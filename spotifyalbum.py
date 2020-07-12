import os
import sys
import spotipy
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# gets the username

# the username is passed as a parameter to the script manually, and it's the 1st element, 0th being name of script itself
username = sys.argv[1]

# User ID for Facebook users 22bg3h2b6ayxzpr44gma45eqy?si=cK5FiLjrTPuRSx3P3AmDPw

# Erase cache and prompt for user permission

try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create our spotifyObject

spotifyObject = spotipy.Spotify(auth = token)

user = spotifyObject.current_user()
# print(json.dumps(user, sort_keys=True, indent=4))

displayName = user['display_name']

followers = user['followers']['total']

while True:

    print()
    print('>>> Welcome to Spotipy ' + displayName + "!")
    print('>>> You have ' + str(followers) + ' followers.')
    print()
    print('0 - search for an artist')
    print('1 - exit')

    choice = input('Your choice: ')

    # Search for the artist
    if choice == "0" :
        print()
        searchQuery = input("Artist Name: ")

        # Get search results
        searchResults = spotifyObject.search(searchQuery, 1, 0, 'artist')
        print(json.dumps(searchResults, sort_keys=True, indent=4))

        # 'items' is just an array of size 1 with a lot more stuff in the middle
        # Artist details
        artist = searchResults['artists']['items'][0]

        print(artist['name'])
        print('Followers: ' + str(artist['followers']['total']))
        print(artist['genres'][0])
        print()

        webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        # Album details
        trackURIs = []
        trackArt = []
        trackNames = []
        count = 0


        # Extract Album data
        albumResults = spotifyObject.artist_albums(artistID)

        # this time items is an array of all of the albums
        albumResults = albumResults['items']

        for item in albumResults:
            print("ALBUM: " + item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)

            trackResults = trackResults['items']

            for item in trackResults:
                print(str(count) + ": " + item['name'])
                trackNames.append(item['name'])
                trackURIs.append(item['uri'])
                # print(json.dumps(spotifyObject.audio_analysis(item['id']), sort_keys=True, indent=4))
                trackArt.append(albumArt)
                count += 1

            print(trackNames[1])
            print(json.dumps(spotifyObject.audio_features([trackURIs[1]]), sort_keys=True, indent=4))

        # See the album art
        while True:
            songSelection = input("Enter a song number to see its album art (e to exit) : ")
            if songSelection == "e":
                break
            webbrowser.open(trackArt[int(songSelection)])

        # print(json.dumps(albumResults, sort_keys=True, indent=4))



    # End the program
    if choice == "1":
        break

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))

