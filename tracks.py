import requests
import json
from time import mktime, strptime
from datetime import datetime, timedelta
from albums import getAlbumIds

def getAlbum(album_id):
    endpoint = 'https://api.spotify.com/v1/albums/' + album_id
    r = requests.get(endpoint)
    return json.loads(r.content)

def getDate(unstruct_time):
    struct_date = strptime(unstruct_time, "%Y-%m-%d")
    return datetime.fromtimestamp(mktime(struct_date))

def getTrackUris(access_token, token_type):
    album_ids = getAlbumIds(access_token, token_type)
    #album_ids = ['5fffaeeOmkUPC1dgu3sX7V', '5eKLb6aljErWJyIv7BgUlg', '5SXT6dwhHX56Sos7KMcMF5', '6g86ETFJBa1KiFhum0lxA1', '48AO9mcRyFRYyTH1KMg4J4', '3rDbA12I5duZnlwakqDdZa', '2cWBwpqMsDJC1ZUwz813lo', '3vOgbDjgsZBAPwV2M3bNOj', '6t7956yu5zYf5A829XRiHC']
    track_uris = []

    for x in range(0, len(album_ids)):
        album_data = getAlbum(album_ids[x])

        if(album_data['release_date_precision'] == 'day'):
            album_release_date = getDate(album_data['release_date'])
            cutoff_date = datetime.today() - timedelta(days=30)

            if(cutoff_date < album_release_date):
                for y in range(0, len(album_data['tracks']['items'])):
                    print album_data['tracks']['items'][y]['uri']
                    track_uris.append(album_data['tracks']['items'][y]['uri'])

    return track_uris
