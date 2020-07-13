import pandas as pd 
import numpy as np

from sklearn import tree
from sklean.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt
import seaborn as sns

import graphviz
import pydotplus
import io
from scipy import misc

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

 # the decision tree ASSUMES THAT YOU ALREADY HAVE A PLAYLIST MADE.
 # to make a playlist and choose from a certain set of songs initially, that will have a seperate file or whatever

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

# use spotify authentication to log in and get to/access a playlist

# create a decision tree based on already chosen songs in the running playlist

# browse through new releases and pick songs from them that would fit the decision tree characteristics?

# add those songs to the playlist
