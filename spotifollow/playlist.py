from spotifollow.spotify import client


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

def playlistExists(user_id, playlist_name):
    user_playlist_names = getUserPlaylistNames(user_id)

    for key in user_playlist_names:
        if(user_playlist_names[key] == playlist_name):
            return key

    return None

#these names are misleading
def getPlaylistIds(user_id, track_uris):
    playlist_ids = {}
    for key in track_uris:
        playlist_name = track_uris[key]["playlist_name"]
        playlist_id = playlistExists(user_id, playlist_name)

        if(playlist_id != None):
            playlist_ids[key] = playlist_id
        else:
            playlist_ids[key] = client.createNewPlaylist(user_id, playlist_name)

    return playlist_ids

#name change pleaseee
def addTracks(user_id, track_uris, playlist_ids):
    for playlist_id in playlist_ids:
        max_tracks = 100
        start_index = 0
        end_index = max_tracks

        while(start_index < len(track_uris)):
            if(end_index > len(track_uris)):
                end_index = len(track_uris)
            client.addTracksToPlaylist(user_id, track_uris[playlist_id]['uris'][start_index:end_index], playlist_ids[playlist_id])
            end_index += max_tracks
            start_index += max_tracks
