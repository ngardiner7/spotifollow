# import requests
# import json

# CLIENT_SECRET = 'e5c5cab28a87494c8ceda121ac403790'
# CLIENT_ID = '33390eea405d4badaf917ba7b06da77e'
# REDIRECT_URI = 'https://seatgeek.com'
# AUTHORIZATION_CODE = 'AQDEXDUCuDDfR5gTnZDzucREHYOuhbfTF___xYneppOikS1aARBL1pRWxllJNWNaQ-j-rxvkR_z_AbgGTKCNLR3fdPyYrM_JgL74iBaLsgo1knji5rJ3tPoEH-o9ntB27IGx53UNPU0Cbz4mu-wQPFe7fSB3bvjltN4HTny5L7PVcmMcTwFXygVVeJNgFn-oK_lBPw_HlGEvKOW4r9LeHbT4t7PTP9TIKufmkw_XaYLcARYxy80Dk25h-SRipf4c5Rr290az9x-1U-TlRfshw2ukQMv51C0h_G20aMi9JMMFo6rn-VgAh03llh3wypfgKnkLzA'
# REFRESH_TOKEN = 'AQAMezcfmoIQQPKiVzCerrOE6PmiJkp_9J8roeFcg2jJ-lPkXM2zDdZqnHtGw9zE0dMM5g_QNuCKjWHkEJ0NrgJi0U21iiKS5pfFPryx1XtM5od8KKdUt1Gd6TqzpPbyzjY'
#
# SANIKA_AUTHORIZATION = 'AQBAyBgO9VHBKUc4ArnqAFnmjdP7PTCEnlwMMI30uKqHVjXqk4cW6pWRuenmya4Du1PKF9-DUqmTmD-hBPXnBnIKF3znVcWeGOIwZ7Han3x7dCA_Ux2a4T66V9CONGl8gYPzopwt6cfvnze0wdxn-t7I3YKKqpgppKUrVIGrQyXvGtlASbutjA9Jph5C1sKDQXV-Hr-laL5yEoY3UWhGI2XoZjP6LQQiT4pkBq7ndQWSWogaPOMswBLpFBShATbXX8NxCTF8r4wqSExhSyEZSQVaOnjAKOnXD6y115Wi-mWEGa2TK8z_ywdnYD7BcPweB26tog'
# SANIKA_REFRESH_TOKEN = 'AQBXKGXs-A9RK6MHjdeAGdqwT-KhKex3ZEG8Z0HWITFwDoKaISpUhPvrGLHLDpRXpy7hDQMFXu6X8M9m7POBs18tOvOVDfw-Te2Nk4AiBnNYR7ZiPYnyTMlaaVF1HUvjHNA'


def do_tings():
    print "hello"
#
# ##Auth
# def getAuthCode():
#     params = {
#         'client_id' : CLIENT_ID,
#         'response_type' : 'code',
#         'redirect_uri' : CLIENT_SECRET,
#         'scope' : 'playlist-modify-private user-follow-read user-follow-modify playlist-modify-public user-library-read'
#     }
#     r = requests.get('https://accounts.spotify.com/authorize', params=params['auth_code']['params'])
#
# def getInitialAccessToken():
#     body = {
#         'grant_type' : 'authorization_code',
#         'code' : AUTHORIZATION_CODE,
#         'redirect_uri' : REDIRECT_URI
#     }
#     r = requests.post('https://accounts.spotify.com/api/token', auth=(CLIENT_ID, CLIENT_SECRET), data=body)
#     return json.loads(r.content)
#
# def getNewAccessToken():
#     body = {
#         'grant_type' : 'refresh_token',
#         'refresh_token' : REFRESH_TOKEN
#     },
#     r = requests.post('https://accounts.spotify.com/api/token', auth=(CLIENT_ID, CLIENT_SECRET), data=body)
#     return json.loads(r.content)
#
# ##user
# def getUserId():
#     token = {
#         'Authorization' : TOKEN_TYPE + ' ' + ACCESS_TOKEN
#     }
#
#     r = requests.get('https://api.spotify.com/v1/me', headers=token)
#     return json.loads(r.content)['id']
#
# ##artists
# def getUserFollowedArtists(after_id, access_token, token_type):
#     params = {
#         'type' : 'artist',
#         'limit' : '50',
#     }
#
#     if(after_id != ''):
#         params['after'] = after_id
#
#     token = {
#         'Authorization' : token_type + ' ' + access_token
#     }
#
#     r = requests.get('https://api.spotify.com/v1/me/following', params=params, headers=token)
#     return json.loads(r.content)
#
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
# def getNextUserLikedArtists(next_request, access_token, token_type):
#     token = {
#         'Authorization' : token_type + ' ' + access_token
#     }
#
#     r = requests.get(next_request, headers=token)
#     return json.loads(r.content)
#
# ##albums
# def getIntitialArtistAlbums(artist_id):
#     params = {
#         'album_type' : 'album,single,compilation',
#         'market' : 'US',
#         'limit' : '50',
#     }
#
#     endpoint = 'https://api.spotify.com/v1/artists/' + artist_id + '/albums'
#     r = requests.get(endpoint, params=params)
#     return json.loads(r.content)
#
# def getNextArtistAlbums(next_request):
#     r = requests.get(next_request)
#     return json.loads(r.content)
#
# def getArtistAlbums(next_request, artist_id):
#     if(next_request == ''):
#         return getIntitialArtistAlbums(artist_id)
#     else:
#         return getNextArtistAlbums(next_request)
#
# ##tracks
# def getAlbum(album_id):
#     endpoint = 'https://api.spotify.com/v1/albums/' + album_id
#     r = requests.get(endpoint)
#     return json.loads(r.content)
#
#
# ##playlists
#
# def addTracksToPlaylist(user_id, access_token, token_type, uris, playlist_id):
#     token = {
#         'Authorization' : token_type + ' ' + access_token,
#         'Content-Type' : 'application/json'
#     }
#
#     body = {
#         'uris' : uris,
#     }
#
#     endpoint = 'https://api.spotify.com/v1/users/' + user_id + '/playlists/' + playlist_id + '/tracks'
#     r = requests.post(endpoint, data=json.dumps(body), headers=token)
#
# def createNewPlaylist(user_id, access_token, token_type, playlist_name):
#     token = {
#         'Authorization' : token_type + ' ' + access_token,
#         'Content-Type' : 'application/json'
#     }
#     body = {
#         'name' : playlist_name,
#         'public' : 'true'
#     }
#     endpoint = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
#     r = requests.post(endpoint, data=json.dumps(body), headers=token)
#
#     playlist_data = json.loads(r.content)
#     return playlist_data["id"]
#
# def getInitialUserPlaylists(user_id, access_token, token_type):
#     params = {
#         'limit' : '50',
#     }
#
#     token = {
#         'Authorization' : token_type + ' ' + access_token
#     }
#
#     endpoint = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
#     r = requests.get(endpoint, params=params, headers=token)
#     return json.loads(r.content)
#
# def getNextUserPlaylists(next_request):
#     r = requests.get(next_request)
#     return json.loads(r.content)
