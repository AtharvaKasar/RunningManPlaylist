from spotify_client import SpotifyClient
import pandas as pd
from pandas import DataFrame
import numpy as np

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt
import seaborn as sns
import os

def run():
    #for now, we are just going to get the new releases and see what happens

    token = input("Enter Spotify Auth Token: ")
    username = input("Enter Username: ")

    spotify_client = SpotifyClient(token, username)

    # get the new release albums

    new_releases_albums = spotify_client.get_new_releases()

    # get all of the songs from the albums 

    new_releases_songs = spotify_client.get_all_songs_from_albums(new_releases_albums)

    print("NEW RELEASE SONGS")
    print(new_releases_songs)

    

    # run them through the decision tree
        # for song ID in new_releases_songs, get the song info, run that song info through the decision tree, if its 1 then add it to playlist
    '''
    first_song_id = spotify_client.get_first_song_from_album(spotify_song_id)

    playlist_id = "5aTTAzxyQ2xBVJz4WmdCx2"

    if spotify_song_id:
        print("we HERE now")
        added_song = spotify_client.add_one_song_to_playlist(playlist_id, first_song_id)
        if added_song:
            print("NEW SONG ADDED CORRECTLY!!")
    '''

    # now dealing with decision tree

    data = pd.read_csv("/Users/atharvak/Desktop/Projects/RunningManPlaylist/data.csv")

    train, test = train_test_split(data, test_size=0.15)

    c = DecisionTreeClassifier()

    features = ["tempo","danceability","time signature","valence", "energy"]

    X_train = train[features]
    y_train = train["target"]

    X_test = test[features]
    y_test = test["target"]


    dt = c.fit(X_train, y_train)

    y_pred = c.predict(X_test)

    print(y_pred)

    print(y_test)


    for song in new_releases_songs:
        json_temp = spotify_client.get_song_info(song)
        feature_list = []
        feature_list.append(json_temp["tempo"])
        feature_list.append(json_temp["danceability"])
        feature_list.append(json_temp["time_signature"])
        feature_list.append(json_temp["valence"])
        feature_list.append(json_temp["energy"])

        temp_list = []
        temp_list.append(feature_list)

        df = DataFrame(temp_list, columns=['tempo','danceability','time signature','valence','energy'])

        print(type(df))
        print(df)

        # now we have the feature list

        print(type(feature_list))
        print(feature_list)
        print(type(X_test))
        print(X_test)

        pred_for_song = c.predict(df)

        print(pred_for_song)

        if pred_for_song == 1:
            print("\nADDING A SONG CUZ TREE SAID SO")
            print(song)
            spotify_client.add_one_song_to_playlist("5aTTAzxyQ2xBVJz4WmdCx2", song)
        
        # print(json_temp)



    # VVVVVVVV this is what i want to be able to do eventually
    # get all of the new releases

    # create a decision tree based on user data

    # go through new releases and based on decision tree, decide which ones are the best ones

    # add the correct songs to a playlist, but store all data on acceptances / rejections per user in a file or something somewhere

if __name__ == "__main__":
    run()