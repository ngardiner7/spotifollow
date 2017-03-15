from datetime import datetime, timedelta
from time import mktime, strptime

from spotifollow import client


def getDate(unstruct_time):
    struct_date = strptime(unstruct_time, "%Y-%m-%d")
    return datetime.fromtimestamp(mktime(struct_date))

def getTrackUris(album_ids):
    ##album_ids = ['5fffaeeOmkUPC1dgu3sX7V', '3dbaMkITsRRtXN7YQFt9by', '0nHav4ho0ar4ZVve8H5xZn', '5rMUVMhaXB2obaFi3NCL51', '4aYdJUjG4475xqh4luLeNQ']
    track_uris = setupTracksDict();

    for x in range(0, len(album_ids)):
        album_data = client.getAlbum(album_ids[x])

        if(album_data['release_date_precision'] == 'day'):
            album_release_date = getDate(album_data['release_date'])
            cutoff_date = datetime.today() - timedelta(days=30)

            if(cutoff_date < album_release_date):
                for y in range(0, len(album_data['tracks']['items'])):
                    if "remix" in album_data['tracks']['items'][y]['name'].lower():
                        track_uris['remix']['uris'].append(album_data['tracks']['items'][y]['uri']);
                    else:
                        track_uris['new_songs']['uris'].append(album_data['tracks']['items'][y]['uri'])

    return track_uris

def setupTracksDict():
    tracks_dict = {
        'new_songs' : {
            'playlist_name' : "Spotifollow - New Songs",
            'uris' : []
        },
        'remix' : {
            'playlist_name' : "Spotfollow - Remixes",
            'uris' : []
        }
    }
    return tracks_dict
