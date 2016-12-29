import requests
import json
from artists import getArtistIds

def getIntitialArtistAlbums(artist_id):
    params = {
        'album_type' : 'album,single,compilation',
        'market' : 'US',
        'limit' : '50',
    }

    endpoint = 'https://api.spotify.com/v1/artists/' + artist_id + '/albums'
    r = requests.get(endpoint, params=params)
    return json.loads(r.content)

def getNextArtistAlbums(next_request):
    r = requests.get(next_request)
    return json.loads(r.content)

def getArtistAlbums(next_request, artist_id):
    if(next_request == ''):
        return getIntitialArtistAlbums(artist_id)
    else:
        return getNextArtistAlbums(next_request)

def getAlbumIds(access_token, token_type):
    album_ids = []
    artist_ids = getArtistIds(access_token, token_type)
    for x in range(0, len(artist_ids)):
        next_request = ''

        while (next_request != None):
            artist_albums_data = getArtistAlbums(next_request, artist_ids[x])
            num_albums = len(artist_albums_data['items'])

            for y in range(0, num_albums):
                album_ids.append(artist_albums_data['items'][y]['id'])
            next_request = artist_albums_data['next']
    return album_ids
