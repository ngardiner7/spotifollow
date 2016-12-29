import auth
import requests
import json

def getUserId(access_token, token_type):
    p = auth.getAuthParams()

    token = {
        'Authorization' : token_type + ' ' + access_token
    }

    r = requests.get('https://api.spotify.com/v1/me', headers=token)
    return json.loads(r.content)['id']
