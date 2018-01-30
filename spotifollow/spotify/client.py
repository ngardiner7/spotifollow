import requests
import json

CLIENT_SECRET = ''
CLIENT_ID = ''
REDIRECT_URI = 'https://seatgeek.com'
AUTHORIZATION_CODE = ''
REFRESH_TOKEN = ''
TOKEN_TYPE = 'Bearer'

BASE_URLS = {
    "api": "https://api.spotify.com/v1",
    "accounts": "https://accounts.spotify.com"
}

URLS = {
    "auth_code": "{0}/authorize".format(BASE_URLS.get("accounts")),
    "auth_token": "{0}/api/token".format(BASE_URLS.get("accounts")),
    "me": "{0}/me".format(BASE_URLS.get("api")),
    "library": "{0}/me/tracks".format(BASE_URLS.get("api")),
    "following": "{0}/me/following".format(BASE_URLS.get("api")),
    "artists": "{0}/artists".format(BASE_URLS.get("api")),
    "album": "{0}/albums".format(BASE_URLS.get("api")),
    "albums": "{0}/albums/?ids=".format(BASE_URLS.get("api")),
    "users": "{0}/users".format(BASE_URLS.get("api")),
    "top": "{0}/me/top".format(BASE_URLS.get("api"))
}


def getNewAccessToken():
    body = {
        'grant_type' : 'refresh_token',
        'refresh_token' : REFRESH_TOKEN
    }
    url = "{0}".format(URLS.get("auth_token"))
    r = requests.post(url, auth=(CLIENT_ID, CLIENT_SECRET), data=body)

    access_token_json = json.loads(r.content)
    return access_token_json['access_token']


ACCESS_TOKEN = getNewAccessToken()


def getAuthCode():
    params = {
        'client_id' : CLIENT_ID,
        'response_type' : 'code',
        'redirect_uri' : REDIRECT_URI,
        'scope': 'playlist-modify-private user-follow-read user-follow-modify playlist-modify-public user-library-read user-top-read'
    }
    url = "{0}".format(URLS.get("auth_code"))
    r = requests.get(url, params=params)
    return json.loads(r.content)


def getInitialAccessToken():
    body = {
        'grant_type' : 'authorization_code',
        'code' : AUTHORIZATION_CODE,
        'redirect_uri' : REDIRECT_URI
    }
    url = "{0}".format(URLS.get("auth_token"))
    r = requests.post(url, auth=(CLIENT_ID, CLIENT_SECRET), data=body)
    print json.loads(r.content)
    return json.loads(r.content)

##user
def get_user_id():
    token = {
        'Authorization' : TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }
    url = "{0}".format(URLS.get("me"))
    r = requests.get(url, headers=token)
    return json.loads(r.content)['id']

##artists https://developer.spotify.com/web-api/get-followed-artists/
def get_user_followed_artists(after_id):
    params = {
        'type': 'artist',
        'limit': '50',
    }
    if after_id != '':
        params['after'] = after_id

    token = {
        'Authorization': TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }
    url = "{0}".format(URLS.get("following"))
    r = requests.get(url, params=params, headers=token)
    return json.loads(r.content)


def get_user_top_artists(time_range):
    params = {
        'time_range': time_range,
        'limit': '50',
    }

    token = {
        'Authorization': TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }
    url = "{0}/{1}".format(URLS.get("top"), "artists")
    r = requests.get(url, params=params, headers=token)
    return json.loads(r.content)


def get_user_saved_tracks(offset, page_size):
    params = {
        'limit' : page_size,
        'offset' : offset
    }

    token = {
        'Authorization' : TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }

    url = "{0}".format(URLS.get("library"))
    r = requests.get(url, params=params, headers=token)
    return json.loads(r.content)


#   albums https://developer.spotify.com/web-api/get-several-artists/
def get_albums_for_artist(artist_id, offset, page_size):
    token = {
        'Authorization' : TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }
    params = {
        'album_type': 'album,single,compilation',
        'market': 'US',
        'limit': page_size,
        'offset': offset
    }
    url = "{0}/{1}/albums".format(URLS.get("artists"), artist_id)
    r = requests.get(url, params=params, headers=token)
    return json.loads(r.content)


##tracks
def get_album(album_id):
    token = {
        'Authorization' : TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }
    url = "{0}/{1}".format(URLS.get("album"), album_id)
    r = requests.get(url, headers=token)
    return json.loads(r.content)


def get_albums(album_ids):
    token = {
        'Authorization' : TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }
    url = "{0}{1}".format(URLS.get("albums"), album_ids)
    r = requests.get(url, headers=token)
    return json.loads(r.content)

#   playlists
def get_playlists_for_user(user_id, offset, page_size):
    params = {
        'limit': page_size,
        'offset': offset
    }

    token = {
        'Authorization': TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }

    url = "{0}/{1}/{2}".format(URLS.get("users"), user_id, "playlists")
    r = requests.get(url, params=params, headers=token)
    return json.loads(r.content)


def create_playlist(user_id, playlist_name):
    token = {
        'Authorization': TOKEN_TYPE + ' ' + ACCESS_TOKEN,
        'Content-Type': 'application/json'
    }
    body = {
        'name': playlist_name,
        'public': 'true'
    }

    url = "{0}/{1}/{2}".format(URLS.get("users"), user_id, "playlists")
    r = requests.post(url, headers=token, data=json.dumps(body))

    playlist_data = json.loads(r.content)
    return playlist_data["id"]


def add_tracks_to_playlist(user_id, uris, playlist_id):
    token = {
        'Authorization' : TOKEN_TYPE + ' ' + ACCESS_TOKEN,
        'Content-Type' : 'application/json'
    }

    body = {
        'uris' : uris,
    }

    url = "{0}/{1}/{2}/{3}/{4}".format(URLS.get("users"), user_id, "playlists", playlist_id, "tracks")
    r = requests.post(url, data=json.dumps(body), headers=token)
    return
