from spotifollow.spotify import client

PAGE_SIZE = 50


def get_albums_for_artist(artist_id):
    albums = []
    start = 0
    while True:
        album_data = client.get_albums_for_artist(artist_id, start, PAGE_SIZE)
        albums.extend(album_data.get("items"))
        if len(album_data.get("items")) < PAGE_SIZE:
            break
        start += len(album_data.get("items"))

    return albums


def get_albums_for_artist_ids(artist_ids):
    albums = []
    for artist_id in artist_ids:
        artist_albums_data = get_albums_for_artist(artist_id)
        albums.extend(artist_albums_data)

    return albums

