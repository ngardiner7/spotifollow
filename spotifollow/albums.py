from spotifollow.spotify import client

PAGE_SIZE = 50


def get_albums_for_artist(artist_id):
    albums = []
    start = 0
    while True:
        album_data = client.get_albums_for_artist(artist_id, start, PAGE_SIZE)
        # Get a 429 for rate limiting issues. Need to auth my requests for better rate limits ideally
        if album_data is not None:
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

# The code is breaking occassionaly for artist_id = '6mA4csYsYvf4Mq02PleZEV' with the following error: TypeError: 'NoneType' object is not iterable
# Sometimes works, sometimes doesn't...
