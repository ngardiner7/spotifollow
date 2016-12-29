import requests
import json

def getUserArtists(after_id, access_token, token_type):
    params = {
        'type' : 'artist',
        'limit' : '50',
    }

    if(after_id != ''):
        params['after'] = after_id

    token = {
        'Authorization' : token_type + ' ' + access_token
    }

    r = requests.get('https://api.spotify.com/v1/me/following', params=params, headers=token)
    return json.loads(r.content)

def getArtistIds(access_token, token_type):
    artist_ids = []
    after_id = ''
    while(after_id != None):
        artist_data = getUserArtists(after_id, access_token, token_type)
        num_artists = len(artist_data['artists']['items'])
        after_id = artist_data['artists']['cursors']['after']

        for x in range(0, num_artists):
            artist_ids.append(artist_data['artists']['items'][x]['id'])

    return artist_ids
