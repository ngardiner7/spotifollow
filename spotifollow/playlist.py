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



# def add_tracks_to_playlists(track_uris_by_playlist):
#     user_id = client.get_user_id()
#     add_playlist_ids_to_track_uris(user_id, track_uris_by_playlist)

    # for playlist_id in playlist_ids:
    #     max_tracks = 100
    #     start_index = 0
    #     end_index = max_tracks
    #
    #     while(start_index < len(track_uris)):
    #         if(end_index > len(track_uris)):
    #             end_index = len(track_uris)
    #         client.addTracksToPlaylist(user_id, track_uris[playlist_id]['uris'][start_index:end_index], playlist_ids[playlist_id])
    #         end_index += max_tracks
    #         start_index += max_tracks

def add_playlist_ids_to_track_uris(user_id, track_uris_by_playlist):
    for playlist in track_uris_by_playlist:
        #Ideally want to be storing these playlist ids in the future
        playlist_id = get_playlist_id(user_id, playlist["playlist_name"])

        if(playlist_id != None):
            playlist["id"] = playlist_id
        else:
            playlist["id"] = client.createNewPlaylist(user_id, playlist["playlist_name"])

    return playlist_ids

def get_playlist_id(user_id, playlist_name):
    user_playlist_names = get_user_playlist_names(user_id)

    for playlist_name in user_playlist_names:
        if(user_playlist_names[key] == playlist_name):
            return key

    return None

def getUserPlaylists(next_request, user_id):
    if(next_request == ''):
        return client.getInitialUserPlaylists(user_id)
    else:
        return client.getNextUserPlaylists(next_request)

def getUserPlaylistNames(user_id):
    playlistsNames = {}
    next_request = ''

    while (next_request != None):
        user_playlists_data = getUserPlaylists(next_request, user_id)
        num_playlists = len(user_playlists_data['items'])

        for x in range(0, num_playlists):
            playlistsNames[user_playlists_data['items'][x]['id']] = user_playlists_data['items'][x]['name']

        next_request = user_playlists_data['next']

    return playlistsNames


# Other shit


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
