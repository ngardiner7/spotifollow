import requests
from  more_itertools import unique_everseen
import json

def getUserFollowedArtists(after_id, access_token, token_type):
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

def getUserFollowedArtistsIds(access_token, token_type):
    artist_ids = []
    after_id = ''
    while(after_id != None):
        artist_data = getUserFollowedArtists(after_id, access_token, token_type)
        num_artists = len(artist_data['artists']['items'])
        after_id = artist_data['artists']['cursors']['after']

        for x in range(0, num_artists):
            artist_ids.append(artist_data['artists']['items'][x]['id'])

    return artist_ids

def getInitialUserLikedArtists(access_token, token_type):
    params = {
        'limit' : '50',
    }

    token = {
        'Authorization' : token_type + ' ' + access_token
    }

    endpoint = 'https://api.spotify.com/v1/me/tracks'
    r = requests.get(endpoint, params=params, headers=token)
    return json.loads(r.content)

def getNextUserLikedArtists(next_request, access_token, token_type):
    token = {
        'Authorization' : token_type + ' ' + access_token
    }

    r = requests.get(next_request, headers=token)
    return json.loads(r.content)

def getUserLikedArtists(next_request, access_token, token_type):
    if(next_request == ''):
        return getInitialUserLikedArtists(access_token, token_type)
    else:
        return getNextUserLikedArtists(next_request, access_token, token_type)

def getUserLikedArtistsIds(access_token, token_type):
    artist_ids = []
    next_request = ''

    while(next_request != None):
        artist_data = getUserLikedArtists(next_request, access_token, token_type)
        num_tracks = len(artist_data['items'])
        for x in range(0, num_tracks):

            num_artists = len(artist_data['items'][x]['track']['artists'])
            for y in range(0, num_artists):

                artist_ids.append(artist_data['items'][x]['track']['artists'][y]['id'])

        next_request = artist_data['next']

    return artist_ids

def getArtistIds(access_token, token_type):
    all_artist_ids = getUserFollowedArtistsIds(access_token, token_type) + getUserLikedArtistsIds(access_token, token_type)
    return list(unique_everseen(all_artist_ids))
