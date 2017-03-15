import playlist
import tracks
import user
import requests
import artists
import client
import albums
import cProfile
import multiprocessing

# from spotify import client

def main():
    artist_ids = artists.getArtistIds()
    album_ids = albums.getAlbumIds(artist_ids)
    track_uris = tracks.getTrackUris(album_ids)

    user_id = client.getUserId()
    playlist_ids = playlist.getPlaylistIds(user_id, track_uris)
    playlist.addTracks(user_id, track_uris, playlist_ids)

# def test():
#     track_uris = tracks.getTrackUris()
#     user_id = client.getUserId()
#     playlist_ids = playlist.getPlaylistIds(user_id, track_uris)
#     playlist.addTracks(user_id, track_uris, playlist_ids)

main()
