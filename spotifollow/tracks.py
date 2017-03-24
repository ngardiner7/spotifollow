from datetime import datetime, timedelta
from time import mktime, strptime
from spotifollow.spotify import client

def get_track_uris_by_playlist(album_ids):
    # Using these for quicker testing - album_ids = ["5fffaeeOmkUPC1dgu3sX7V", "3dbaMkITsRRtXN7YQFt9by", "0nHav4ho0ar4ZVve8H5xZn", "5rMUVMhaXB2obaFi3NCL51", "4aYdJUjG4475xqh4luLeNQ", "6ZJJi8V3NaEHpRV4FD4ZFS"]
    # Get a 429 for rate limiting issues. Need to auth my requests for better rate limits ideally
    tracks = get_tracks_for_album_ids(album_ids)
    track_uris = get_tracks_dictionary()
    for track in tracks:
        if "remix" in track["name"].lower():
            track_uris["remix"]["uris"].append(track["uri"])
        else:
            track_uris["new_songs"]["uris"].append(track["uri"])

    return track_uris


#Add handling for remixes again
def get_tracks_for_album_ids(album_ids):
    tracks = []
    for album_id in album_ids:
        #I might need to remane some of these "data" variables, it's s bit confusing tbh
        album_data = client.get_album(album_id)
        if album_date_is_eligible(album_data):
            tracks.extend(album_data["tracks"]["items"])

    return tracks


def album_date_is_eligible(album_data):
    print album_data["release_date"]
    if(album_data["release_date_precision"] == "day"):
        album_release_date = format_string_timestamp_to_date(album_data["release_date"])
        cutoff_date = datetime.today() - timedelta(days=30)

        if(cutoff_date < album_release_date):
            return True
        else:
            return False


def format_string_timestamp_to_date(unstruct_time):
    struct_date = strptime(unstruct_time, "%Y-%m-%d")
    return datetime.fromtimestamp(mktime(struct_date))


def get_tracks_dictionary():
    tracks_dict = {
        "new_songs": {
            "playlist_name": "Spotifollow - New Songs",
            "uris": []
        },
        'remix' : {
            "playlist_name" : "Spotifollow - Remixes",
            "uris" : []
        }
    }
    return tracks_dict






# def getTrackUris(album_ids):
#     ##album_ids = ['5fffaeeOmkUPC1dgu3sX7V', '3dbaMkITsRRtXN7YQFt9by', '0nHav4ho0ar4ZVve8H5xZn', '5rMUVMhaXB2obaFi3NCL51', '4aYdJUjG4475xqh4luLeNQ']
#     track_uris = setupTracksDict();
#
#     for x in range(0, len(album_ids)):
#         album_data = client.getAlbum(album_ids[x])
#
#         if(album_data['release_date_precision'] == 'day'):
#             album_release_date = getDate(album_data['release_date'])
#             cutoff_date = datetime.today() - timedelta(days=30)
#
#             if(cutoff_date < album_release_date):
#                 for y in range(0, len(album_data['tracks']['items'])):

#     return track_uris
