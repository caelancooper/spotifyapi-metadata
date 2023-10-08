import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Input Credentials
client_id = "YOUR ID"
client_secret = "YOUR SECRET"

# Initialize spotipy
auth_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# def get_song_metadata():
def get_song_metadata():
    # Asks user for artist and song names
    artist_name = input("Please enter the artist's name: ")
    song_name = input("Please enter the song's name: ")

    query = f'artist:{artist_name} track:{song_name}'
    result = sp.search(q=query, type='track', limit=1)


    if result['tracks']['total'] > 0:
        track = result['tracks']['items'][0]
        metadata = {
            'artist': track['artists'][0]['name'],
            'song_name': track['name'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date'],
            'popularity': track['popularity'],
            'preview_url': track['preview_url'],
            'track_id': track['id'],
            'external_url': track['external_urls']['spotify']
        }

        return metadata
    else:
        return None

metadata = get_song_metadata()
print(metadata)