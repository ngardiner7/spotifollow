import user
import json
import requests
import auth

def getInitialUserPlaylists(user_id, access_token, token_type):
    params = {
        'limit' : '50',
    }

    token = {
        'Authorization' : token_type + ' ' + access_token
    }

    endpoint = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
    r = requests.get(endpoint, params=params, headers=token)
    return json.loads(r.content)

#THIS PROBABLY DOESN'T WORK, NO TOKEN PASSED
def getNextUserPlaylists(next_request):
    r = requests.get(next_request)
    return json.loads(r.content)

def getUserPlaylists(next_request, user_id, access_token, token_type):
    if(next_request == ''):
        return getInitialUserPlaylists(user_id, access_token, token_type)
    else:
        return getNextUserPlaylists(next_request)

def getUserPlaylistNames(user_id, access_token, token_type):
    playlistsNames = {}
    next_request = ''

    while (next_request != None):
        user_playlists_data = getUserPlaylists(next_request, user_id, access_token, token_type)
        num_playlists = len(user_playlists_data['items'])

        for x in range(0, num_playlists):
            playlistsNames[user_playlists_data['items'][x]['id']] = user_playlists_data['items'][x]['name']

        next_request = user_playlists_data['next']

    return playlistsNames

def playlistExists(user_id, access_token, token_type, playlist_name):
    user_playlist_names = getUserPlaylistNames(user_id, access_token, token_type)

    for key in user_playlist_names:
        if(user_playlist_names[key] == playlist_name):
            return key

    return None

def createNewPlaylist(user_id, access_token, token_type, playlist_name):
    token = {
        'Authorization' : token_type + ' ' + access_token,
        'Content-Type' : 'application/json'
    }
    body = {
        'name' : playlist_name,
        'public' : 'true'
    }
    endpoint = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
    r = requests.post(endpoint, data=json.dumps(body), headers=token)

    playlist_data = json.loads(r.content)
    return playlist_data["id"]

#these names are misleading
def getPlaylistId(user_id, access_token, token_type):
    playlist_name = 'Testing Spotify API3'
    playlist_id = playlistExists(user_id, access_token, token_type, playlist_name)

    if(playlist_id != None):
        return playlist_id
    else:
        return createNewPlaylist(user_id, access_token, token_type, playlist_name)

def addTracksToPlaylist(user_id, access_token, token_type, uris, playlist_id):
    token = {
        'Authorization' : token_type + ' ' + access_token,
        'Content-Type' : 'application/json'
    }

    body = {
        'uris' : uris,
    }

    endpoint = 'https://api.spotify.com/v1/users/' + user_id + '/playlists/' + playlist_id + '/tracks'
    r = requests.post(endpoint, data=json.dumps(body), headers=token)

#name change pleaseee
def addTracks(user_id, access_token, token_type, track_uris, playlist_id):
    max_tracks = 100
    start_index = 0
    end_index = max_tracks

    while(start_index < len(track_uris)):
        if(end_index > len(track_uris)):
            end_index = len(track_uris)

        addTracksToPlaylist(user_id, access_token, token_type, track_uris[start_index:end_index], playlist_id)
        end_index += max_tracks
        start_index += max_tracks
