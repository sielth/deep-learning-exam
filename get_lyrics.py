import lyricsgenius
import numpy as np
import pandas as pd

mood_df = pd.read_csv('https://raw.githubusercontent.com/cristobalvch/Spotify-Machine-Learning/master/data/data_moods.csv')
mood_df.columns=['name', 'album', 'artist', 'id', 'release_date', 'popularity', 'length', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'valence', 'loudness', 'speechiness', 'tempo', 'key', 'time_signature', 'mood']
mood_df['lyrics'] = None


token = 'vk2-Psny9HsCHud0FDTEM0t05ElfJlIPtWRiESPIol6mKY3dwTYumFkzqQzW5CxG'
genius = lyricsgenius.Genius(token, timeout=30)

for index, row in mood_df.iterrows():
    try:
        title = row[0]
        artist = row[2]

        print(title + " " + artist)

        song = test = genius.search_song(artist=artist, title=title)

        if song is not None:
            mood_df.at[index, 'lyrics'] = song.lyrics
        else:
            mood_df.at[index, 'lyrics'] = 'NaN'
    except:
        continue

mood_df.to_csv('mood_data.csv', index=False)
