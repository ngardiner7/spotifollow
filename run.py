"""
A Simple Script that is v0.1 that creates a new playlist
for a single user with hard coded spotify user creds
"""
from spotifollow import albums
from spotifollow import artists
from spotifollow import tracks
from spotifollow import playlist
from spotifollow.spotify import client

def main():
    print "Fetching Artists"
    people = artists.get_user_followed_artist()
    artist_ids = [artist["id"] for artist in people]
    print "artist ids:"
    print artist_ids

    print "Fetching Albums"
    artist_albums = albums.get_albums_for_artist_ids(artist_ids)
    album_ids = [album["id"] for album in artist_albums]
    print "album ids:"
    print album_ids

    print "Fetching Tracks"
    track_uris_by_playlist = tracks.get_track_uris_by_playlist()
    print "track uris:"
    print track_uris_by_playlist

    # print "Adding Tracks to Playlist"
    # playlist.add_new_tracks_to_user_playlist()
    # album_ids = albums.getAlbumIds(artist_ids)
    # track_uris = tracks.getTrackUris(album_ids)
    # playlist_ids = playlist.getPlaylistIds(user_id, track_uris)
    # playlist.addTracks(user_id, track_uris, playlist_ids)

# def test():
#     track_uris = tracks.getTrackUris()
#     user_id = client.getUserId()
#     playlist_ids = playlist.getPlaylistIds(user_id, track_uris)
#     playlist.addTracks(user_id, track_uris, playlist_ids)

main()
