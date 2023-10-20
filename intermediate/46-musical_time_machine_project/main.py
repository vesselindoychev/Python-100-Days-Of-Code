import os

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import lxml
from dotenv import load_dotenv

load_dotenv(verbose=True)

SPOTIFY_CLIENT_ID = os.environ['CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = os.environ['REDIRECT_URI']

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope='playlist-modify-private',
                                               cache_path='token.env'))


user_id = sp.current_user()['id']

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
BILLBOARD_URL = f'https://www.billboard.com/charts/hot-100/{date}'

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
CREATE_SPOTIFY_PLAYLIST_ENDPOINT = f'https://api.spotify.com/v1/users/{user_id}/playlists'
HEADERS = {
    'Authorization': f"Bearer {ACCESS_TOKEN}"
}
request_body = {
    'name': f'{date} Billboard 100',
    'description': 'Top hits from that date',
    'public': False
}


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

response = requests.get(url=BILLBOARD_URL)
webpage_text = response.text
soup = BeautifulSoup(webpage_text, 'lxml')

hits = [sn.getText().strip() for sn in soup.select(selector='li ul li h3')]
song_uris = []
year = date.split('-')[0]

for hit in hits:
    result = sp.search(q=f"track:{hit} year:{year}", type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"'{hit}' doesn't exist in Spotify. Skipped")

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
# sp.playlist_upload_cover_image(playlist_id=playlist['id'], image_b64='image.jpg')

