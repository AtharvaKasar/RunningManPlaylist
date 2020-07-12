from spotify_client import SpotifyClient
import os

def run():
    #for now, we are just going to get the new releases and see what happens

    token = input("Enter Spotify Auth Token: ")
    username = input("Enter Username: ")

    spotify_client = SpotifyClient(token, username)

    spotify_song_id = spotify_client.get_new_releases()

    first_song_id = spotify_client.get_first_song_from_album(spotify_song_id)

    playlist_id = "5aTTAzxyQ2xBVJz4WmdCx2"

    if spotify_song_id:
        print("we HERE now")
        added_song = spotify_client.add_one_song_to_playlist(playlist_id, first_song_id)
        if added_song:
            print("NEW SONG ADDED CORRECTLY!!")


    # VVVVVVVV this is what i want to be able to do eventually
    # get all of the new releases

    # create a decision tree based on user data????? how am i gonna do this

    # go through new releases and based on decision tree, decide which ones are the best ones

    # add the correct songs to a playlist, but store all data on acceptances / rejections per user in a file or something somewhere


if __name__ == "__main__":
    run()