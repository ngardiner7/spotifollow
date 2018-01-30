from spotifollow.spotify import client
from collections import Counter

PAGE_SIZE = 50
FREQUENCY_MIN = 2

def get_artists():
    artist_ids = get_user_followed_artist() + get_top_artists() + get_frequent_saved_artists()
    return dedupe(artist_ids)


def get_user_followed_artist():
    after_id = ''
    artists = []
    while after_id is not None:
        artist_data = client.get_user_followed_artists(after_id)
        artists.extend(artist_data['artists']['items'])
        after_id = artist_data['artists']['cursors']['after']

    return [artist['id'] for artist in artists]


def get_top_artists():
    artist_ids = []
    ranges = ['short_term', 'medium_term','long_term']
    for time_range in ranges:
        artist_data = client.get_user_top_artists(time_range)
        for artist in artist_data.get("items"):
            artist_ids.append(artist.get("id"))

    return artist_ids


def dedupe(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def get_frequent_saved_artists():
    frequent_artist_ids = []
    artist_ids = get_user_saved_tracks()
    artist_id_counts = Counter(artist_ids)

    for artist_id in artist_id_counts:
        if artist_id_counts.get(artist_id) >= FREQUENCY_MIN:
            frequent_artist_ids.append(artist_id)

    return frequent_artist_ids


def get_user_saved_tracks():
    artist_ids = []
    start = 0
    while True:
        saved_track_data = client.get_user_saved_tracks(start, PAGE_SIZE)
        if saved_track_data is not None:
            for track in saved_track_data.get("items"):
                # I don't like this naming, it's real annoying because of the double track reference (e.g. "track.get("track")")
                for artist in track.get("track").get("artists"):
                    artist_ids.append(artist.get("id"))
            # Worried that there are scenarios where this could break if #saved_tracks % PAGE_SIZE = 0
            if len(saved_track_data.get("items")) < PAGE_SIZE:
                break
            start += len(saved_track_data.get("items"))

    return artist_ids


def get_albums_for_artist(artist_id):
    albums = []
    start = 0
    while True:
        album_data = client.get_albums_for_artist(artist_id, start, PAGE_SIZE)
        if album_data is not None:
            albums.extend(album_data.get("items"))
            if len(album_data.get("items")) < PAGE_SIZE:
                break
            start += len(album_data.get("items"))

    return albums
