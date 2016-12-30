import requests
import json

def getAuthParams():
    oauth_creds = {
        'client_secret' : 'INSERT-HERE',
        'client_id' : 'INSERT-HERE',
        'redirect_uri' : 'https://seatgeek.com'
    }

    params = {
        'auth_code' : {
            'params' : {
                'client_id' : oauth_creds['client_id'],
                'response_type' : 'code',
                'redirect_uri' : oauth_creds['redirect_uri'],
                'scope' : 'playlist-modify-private user-follow-read user-follow-modify playlist-modify-public user-library-read'
            }
        },
        'auth_token' : {
            'body' : {
                'grant_type' : 'authorization_code',
                'code' : 'INSERT-HERE',
                'redirect_uri' : oauth_creds['redirect_uri']
            },
            'header' : {
                'client_id' : oauth_creds['client_id'],
                'client_secret' : oauth_creds['client_secret']
            }
        },
        'refresh_token' : {
            'body' : {
                'grant_type' : 'refresh_token',
                'refresh_token' : 'INSERT-HERE'
            },
            'header' : {
                'client_id' : oauth_creds['client_id'],
                'client_secret' : oauth_creds['client_secret']
            }
        },
        'me' : {
            'header' : {
                'client_id' : oauth_creds['client_id'],
                'client_secret' : oauth_creds['client_secret']
            }
        }
    }
    return params

def getAuthCode():
    p = getAuthParams()
    r = requests.get('https://accounts.spotify.com/authorize', params=p['auth_code']['params'])
    print r
    print r.url

def getInitialAccessToken():
    p = getAuthParams()
    r = requests.post('https://accounts.spotify.com/api/token', auth=(p['auth_token']['header']['client_id'], p['auth_token']['header']['client_secret']), data=p['auth_token']['body'])
    print r
    print r.content
    print r.url
    return json.loads(r.content)

def getNewAccessToken():
    p = getAuthParams()
    r = requests.post('https://accounts.spotify.com/api/token', auth=(p['refresh_token']['header']['client_id'], p['refresh_token']['header']['client_secret']), data=p['refresh_token']['body'])
    print r
    print r.content
    print r.url
    return json.loads(r.content)

getAuthCode()
