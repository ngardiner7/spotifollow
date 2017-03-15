from spotifollow import artists


def main():
    people = artists.get_user_followed_artist()
    artist_ids = [artist["id"] for artist in people]
    print artist_ids


    # album_ids = albums.getAlbumIds(artist_ids)
    # track_uris = tracks.getTrackUris(album_ids)



    # user_id = client.getUserId()
    # playlist_ids = playlist.getPlaylistIds(user_id, track_uris)
    # playlist.addTracks(user_id, track_uris, playlist_ids)

# def test():
#     track_uris = tracks.getTrackUris()
#     user_id = client.getUserId()
#     playlist_ids = playlist.getPlaylistIds(user_id, track_uris)
#     playlist.addTracks(user_id, track_uris, playlist_ids)

main()
