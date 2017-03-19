import requests
import json

# SANIKA_AUTHORIZATION = 'AQBAyBgO9VHBKUc4ArnqAFnmjdP7PTCEnlwMMI30uKqHVjXqk4cW6pWRuenmya4Du1PKF9-DUqmTmD-hBPXnBnIKF3znVcWeGOIwZ7Han3x7dCA_Ux2a4T66V9CONGl8gYPzopwt6cfvnze0wdxn-t7I3YKKqpgppKUrVIGrQyXvGtlASbutjA9Jph5C1sKDQXV-Hr-laL5yEoY3UWhGI2XoZjP6LQQiT4pkBq7ndQWSWogaPOMswBLpFBShATbXX8NxCTF8r4wqSExhSyEZSQVaOnjAKOnXD6y115Wi-mWEGa2TK8z_ywdnYD7BcPweB26tog'
# SANIKA_REFRESH_TOKEN = 'AQBXKGXs-A9RK6MHjdeAGdqwT-KhKex3ZEG8Z0HWITFwDoKaISpUhPvrGLHLDpRXpy7hDQMFXu6X8M9m7POBs18tOvOVDfw-Te2Nk4AiBnNYR7ZiPYnyTMlaaVF1HUvjHNA'

CLIENT_SECRET = 'e5c5cab28a87494c8ceda121ac403790'
CLIENT_ID = '33390eea405d4badaf917ba7b06da77e'
REDIRECT_URI = 'https://seatgeek.com'
AUTHORIZATION_CODE = 'AQACw12d8VZwCraAA8NgJOyatAWFDvkmkMDsYZ6FTaLmOLM4KMiF__EEEbUIfk8Gyp7cLcSajcAdiBFH7Urb_eaCHGQJ0K1M1ba5ftbDhboZ-jEQnTm1UKBzDu1wSB_coJjXXpTs_pGUV9NGa4n8AY9s0UDv46mjQF6LF4Qv6sic-m9b2WmfubHkzk_T7i4qJxDyxgTh-PdUz-G-FCL8ND0Ciq3Ls7Sn2rKey3I2snVnh2k3KhGy97RbYe42EdhsL9A3XASgRFVk0klEP3nYpoQTLFBFWn-d4in3iN9Sx_aWLYC-JBVFA9S4ZAXLSwLNS-GxMg'
REFRESH_TOKEN = 'AQC56n0LRxYkQHhz3xe-XssVZwWOcDYZGlOMSzO8YxvwvRXEwbN_KRq_dNbyZeGRW8WI61O3dNvCD1PFMAWa71tsErXsoBUxGvW6XvqgL6-fslY916tmA6L5wDNpIDLVrGE'
TOKEN_TYPE = 'Bearer'

BASE_URLS = {
    "api": "https://api.spotify.com/v1",
    "accounts": "https://accounts.spotify.com"
}

URLS = {
    "auth_code": "{0}/authorize".format(BASE_URLS.get("accounts")),
    "auth_token": "{0}/api/token".format(BASE_URLS.get("accounts")),
    "user": "{0}/me".format(BASE_URLS.get("api")),
    "user_following": "{0}/me/following".format(BASE_URLS.get("api")),
    "artists": "{0}/artists".format(BASE_URLS.get("api")),
    "albums": "{0}/albums".format(BASE_URLS.get("api"))
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

##Auth
def getAuthCode():
    params = {
        'client_id' : CLIENT_ID,
        'response_type' : 'code',
        'redirect_uri' : REDIRECT_URI,
        'scope': 'playlist-modify-private user-follow-read user-follow-modify playlist-modify-public user-library-read'
    }
    url = "{0}".format(URLS.get("auth_code"))
    r = requests.get(url, params=params)

def getInitialAccessToken():
    body = {
        'grant_type' : 'authorization_code',
        'code' : AUTHORIZATION_CODE,
        'redirect_uri' : REDIRECT_URI
    }
    url = "{0}".format(URLS.get("auth_token"))
    r = requests.post(url, auth=(CLIENT_ID, CLIENT_SECRET), data=body)
    return json.loads(r.content)

##user
def get_user_id():
    token = {
        'Authorization' : TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }
    url = "{0}".format(URL.get("user"))
    r = requests.get('https://api.spotify.com/v1/me', headers=token)
    return json.loads(r.content)['id']

##artists https://developer.spotify.com/web-api/get-followed-artists/
def getUserFollowedArtists(after_id):
    params = {
        'type': 'artist',
        'limit': '50',
    }
    if after_id != '':
        params['after'] = after_id
    token = {
        'Authorization': TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }
    url = "{0}".format(URLS.get("user_following"))
    r = requests.get(url, params=params, headers=token)
    return json.loads(r.content)

# def getInitialUserLikedArtists(access_token, token_type):
#     params = {
#         'limit' : '50',
#     }
#
#     token = {
#         'Authorization' : token_type + ' ' + access_token
#     }
#
#     endpoint = 'https://api.spotify.com/v1/me/tracks'
#     r = requests.get(endpoint, params=params, headers=token)
#     return json.loads(r.content)
#
#
# def getNextUserLikedArtists(next_request, access_token, token_type):
#     token = {
#         'Authorization' : TOKEN_TYPE + ' ' + ACCESS_TOKEN
#     }
#
#     r = requests.get(next_request, headers=token)
#     return json.loads(r.content)


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
    url = "{0}/{1}".format(URLS.get("albums"), album_id)
    r = requests.get(url, headers=token)
    return json.loads(r.content)


#   playlists
def getInitialUserPlaylists(user_id):
    params = {
        'limit': '50',
    }

    token = {
        'Authorization': TOKEN_TYPE + ' ' + ACCESS_TOKEN
    }

    endpoint = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
    r = requests.get(endpoint, params=params, headers=token)
    return json.loads(r.content)


def getNextUserPlaylists(next_request):
    r = requests.get(next_request)
    return json.loads(r.content)


def createNewPlaylist(user_id, playlist_name):
    token = {
        'Authorization': TOKEN_TYPE + ' ' + ACCESS_TOKEN,
        'Content-Type': 'application/json'
    }
    body = {
        'name': playlist_name,
        'public': 'true'
    }
    endpoint = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
    r = requests.post(endpoint, data=json.dumps(body), headers=token)

    playlist_data = json.loads(r.content)
    return playlist_data["id"]

def addTracksToPlaylist(user_id, uris, playlist_id):
    token = {
        'Authorization' : TOKEN_TYPE + ' ' + ACCESS_TOKEN,
        'Content-Type' : 'application/json'
    }

    body = {
        'uris' : uris,
    }

    endpoint = 'https://api.spotify.com/v1/users/' + user_id + '/playlists/' + playlist_id + '/tracks'
    r = requests.post(endpoint, data=json.dumps(body), headers=token)


# TESTING
# TESTING


# def user_top_tracks():
#     token = {
#         'Authorization': TOKEN_TYPE + ' ' + ACCESS_TOKEN
#     }
#     params = {
#         "limit": 50,
#         "time_range": "medium_term"
#     }
#     url = "https://api.spotify.com/v1/me/top/artists"
#     r = requests.get(url, params=params, headers=token)
#     print r.content
#     return json.loads(r.content)
