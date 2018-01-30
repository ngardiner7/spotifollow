from spotifollow.spotify import client

PAGE_SIZE = 50


def add_tracks_to_playlists(track_uris_by_playlist):
    user_id = client.get_user_id()
    user_playlists = get_playlists_for_user(user_id)
    get_spotifollow_playlist_ids(track_uris_by_playlist, user_playlists, user_id)
    add_songs_to_playlists(track_uris_by_playlist, user_id)


def get_playlists_for_user(user_id):
    playlists = []
    start = 0
    while True:
        playlist_data = client.get_playlists_for_user(user_id, start, PAGE_SIZE)
        if playlist_data is not None:
            playlists.extend(playlist_data.get("items"))
            if len(playlist_data.get("items")) < PAGE_SIZE:
                break
            start += len(playlist_data.get("items"))

    return playlists


def get_spotifollow_playlist_ids(track_uris_by_playlist, user_playlists, user_id):
    for spotifollow_playlist in track_uris_by_playlist:
        track_uris_by_playlist[spotifollow_playlist]["id"] = get_spotifollow_playlist_id(track_uris_by_playlist[spotifollow_playlist], user_playlists, user_id)

# change the spotifollow_playlist name, it's very confusing
def get_spotifollow_playlist_id(spotifollow_playlist, user_playlists, user_id):
    for user_playlist in user_playlists:
        if spotifollow_playlist.get("playlist_name") == user_playlist.get("name"):
            return user_playlist.get("id")

    return client.create_playlist(user_id, spotifollow_playlist.get("playlist_name"))


def add_songs_to_playlists(track_uris_by_playlist, user_id):
    for playlist in track_uris_by_playlist:

        max_tracks = 100
        start_index = 0
        end_index = max_tracks

        print len(track_uris_by_playlist[playlist].get("uris"))
        while start_index < len(track_uris_by_playlist[playlist].get("uris")):
            if end_index > len(track_uris_by_playlist[playlist].get("uris")):
                end_index = len(track_uris_by_playlist[playlist].get("uris"))
            client.add_tracks_to_playlist(user_id, track_uris_by_playlist[playlist].get("uris")[start_index:end_index], track_uris_by_playlist[playlist].get("id"))
            end_index += max_tracks
            start_index += max_tracks
