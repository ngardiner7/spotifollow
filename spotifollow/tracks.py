from datetime import datetime, timedelta
from time import mktime, strptime
from spotifollow.spotify import client

BATCH_SIZE = 20
ALBUM_DATE_ELIGIBILITY = 7


def get_track_uris_by_playlist(album_ids):
    # Getting a 429 for rate limiting issues. Need to auth my requests for better rate limits ideally
    track_uris = get_tracks_for_album_ids(album_ids)
    struct_track_uris = get_tracks_dictionary()
    for track in track_uris:
        if "remix" in track["name"].lower():
            struct_track_uris["remix"]["uris"].append(track["uri"])
        else:
            struct_track_uris["new_songs"]["uris"].append(track["uri"])

    return struct_track_uris


#Add handling for remixes again
def get_tracks_for_album_ids(album_ids):
    tracks = []
    album_ids_batches = batch_album_ids(album_ids)
    for album_ids_batch in album_ids_batches:
        albums_data = client.get_albums(album_ids_batch)
        for album_data in albums_data["albums"]:
            if album_date_is_eligible(album_data):
                tracks.extend(album_data["tracks"]["items"])

    return tracks


def batch_album_ids(album_ids):
    counter = (len(album_ids)/BATCH_SIZE) + 1
    batched_album_ids = []
    for x in range(0, counter):
        start = x * BATCH_SIZE
        end = (x * BATCH_SIZE) + BATCH_SIZE
        batched_album_ids.append(stringify_ablums_ids(album_ids[start:end]))

    return batched_album_ids


def stringify_ablums_ids(album_ids):
    stringified_album_ids = ""
    for album_id in album_ids:
        stringified_album_ids += album_id + ","
    # Removes the extra commma at the end of the album_ids
    return stringified_album_ids[:-1]


def album_date_is_eligible(album_data):
    if album_data["release_date_precision"] == "day":
        album_release_date = format_string_timestamp_to_date(album_data["release_date"])
        cutoff_date = datetime.today() - timedelta(days=ALBUM_DATE_ELIGIBILITY)

        if(cutoff_date < album_release_date):
            return True
        else:
            return False


def format_string_timestamp_to_date(unstruct_time):
    struct_date = strptime(unstruct_time, "%Y-%m-%d")
    return datetime.fromtimestamp(mktime(struct_date))

# I don't really know what the best alternative here is...
def get_tracks_dictionary():
    tracks_dict = {
        "new_songs": {
            "playlist_name": "Spotifollow - New Songs - 4",
            "uris": []
        },
        'remix' : {
            "playlist_name" : "Spotifollow - Remixes - 4",
            "uris" : []
        }
    }
    return tracks_dict
