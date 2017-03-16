"""
A Simple Script that is v0.1 that creates a new playlist
for a single user with hard coded spotify user creds
"""
from spotifollow import albums
from spotifollow import artists


def main():
    print "Fetching Artists"
    people = artists.get_user_followed_artist()
    artist_ids = [artist["id"] for artist in people]

    print "Fetching Albums"
    artist_albums = albums.get_albums_for_artist_ids(artist_ids)
    album_ids = [album["id"] for album in artist_albums]
    print album_ids


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
