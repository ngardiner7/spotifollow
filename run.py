"""
A Simple Script that is v0.1 that creates a new playlist
for a single user with hard coded spotify user creds
"""
from spotifollow import albums
from spotifollow import artists
from spotifollow import top_artists
from spotifollow import tracks
from spotifollow import playlist
from spotifollow.spotify import client

def main():
    artist_ids = artists.get_artists()
    print "Fetching artists:"
    print artist_ids

    print "Fetching Albums"
    artist_albums = albums.get_albums_for_artist_ids(artist_ids)
    album_ids = [album["id"] for album in artist_albums]
    print "album ids:"
    print album_ids

    print "Fetching Tracks"
    track_uris_by_playlist = tracks.get_track_uris_by_playlist(album_ids)
    print "track uris:"
    print track_uris_by_playlist

    print "Adding Tracks to Playlists"
    playlist.add_tracks_to_playlists(track_uris_by_playlist)

main()

# def testing():
#     x = top_artists.get_top_artists()
#
# testing()



#FOR TESTING
    # track_uris_by_playlist = {
    #     'new_songs':
    #         {'playlist_name':'Spotifollow - New Songs',
    #         'uris': [u'spotify:track:089tprIgsyFSOrZpugamLI', u'spotify:track:13EHr5nvvsUGw8IH23WIJg', u'spotify:track:3sykiSQr56MVZW1vp3hJgK', u'spotify:track:20Qufms0u6e9mHprf81SzX', u'spotify:track:1dXgKPAylpIpOnG8se2spN', u'spotify:track:4gUAlquiVHUNppuuy5ISYa', u'spotify:track:6CbiLNbsn99SsKx5OzMWXC', u'spotify:track:6lzP0fs4FC60PxRFCLq2b4', u'spotify:track:1SWp97YZenUS5FFzublQzw', u'spotify:track:2g0pDPygeHPq64iJYnfu4b', u'spotify:track:748pmfPPHxaX5ZfniN3zju', u'spotify:track:2h4sKouhpyBNVJEVy7iQ2R', u'spotify:track:2EJymC7nXIg5VNQQagOAaf', u'spotify:track:5zL7WlS6u9iNpvDcUkcmGp', u'spotify:track:3BTravl1t7M0FVggHVNyHw', u'spotify:track:2TyObk4NTa4xkbQkfPp3UF', u'spotify:track:5ZksJ5xgDBmXi7UuJ1gmQZ', u'spotify:track:2coMhhi8xHvccmAYfFXvHU', u'spotify:track:1ynrjEZaJyv6CA0kFpdNgc', u'spotify:track:4rKTCa0uVmm3Fyhtn4IlLA', u'spotify:track:7DypEWDiM0cQEdAgIedHm1', u'spotify:track:79ychOlXCobj73aj58IIXq', u'spotify:track:4LAaR5eVxr0wMe7AHk63SU', u'spotify:track:5bL01nu6SMRjm6DdQAcibQ', u'spotify:track:4EVzwzftHn7zbY1XMMhMIv', u'spotify:track:44WCdPPn6SSwEotoRl6Bac', u'spotify:track:7rPsLboUKZjY0ibHBRPdKV', u'spotify:track:7Kv05Q8rQaUnoyl3chcMAa', u'spotify:track:40kF6HZ594elw4edYxKfA2', u'spotify:track:3PhPDeFKzRtQvRyU8cseva', u'spotify:track:016COOQeIx1AVtOLLZnaP0', u'spotify:track:089tprIgsyFSOrZpugamLI', u'spotify:track:2OmTzSUtti3Z1WjiiEnF26', u'spotify:track:69i2UyZC5RiLbgAuwyLZBL', u'spotify:track:1lf8E9Z3aywSjrEmwlxIhS', u'spotify:track:7HZHENx2hjedVbTR57XgwC', u'spotify:track:0lMQKBPmCDyLDmj0uoWuDe', u'spotify:track:03Ca4zMU1AIIcTOgrtWmyg', u'spotify:track:4zNrPZhtV4TfVsAvgfHky9', u'spotify:track:5hvm7plFbI8ereO1BqWqhl', u'spotify:track:3z7AceXFwECHGH26FOy3u8']
    #         },
    #     'remix':
    #         {'playlist_name': 'Spotifollow - Remixes',
    #         'uris': [u'spotify:track:1s0klfF3O5Zu2fJz5iCQin', u'spotify:track:0SwtoclXhvIF4pdV0iyf7z', u'spotify:track:7AnnVM4oKQQTzPmO6zT372', u'spotify:track:7mJKR78QFkBeas3q1WmDmh', u'spotify:track:3LaBQ3mMUkjavJxM6T86cp', u'spotify:track:394QnsjxanQcjp5JI8Bn7C', u'spotify:track:5AXUrzvBrTJKbZjklDnytd', u'spotify:track:0n2EGW8WSzLQESjxEyN2iu', u'spotify:track:6oISPN6Clrwt75JFiQF7aO', u'spotify:track:0rNg50D2j2Aq58V3jqdEuu', u'spotify:track:5BOSoyflOWt7LB1o1t5iOv', u'spotify:track:033eAdPpnmBbgfLvbLBih0', u'spotify:track:7J7D2Ezp32LxlYuNTZX48n', u'spotify:track:07hSIkFnDpOhpb46h475Ss', u'spotify:track:0iX9BV34AHBpdfEMgWm5mU', u'spotify:track:7BLZP3Q291G2iVKKgVRDyj', u'spotify:track:7aH3sZ85qQshN0H5ntgvnO', u'spotify:track:0Q0WJJWeLi0foXzW0K87Tr', u'spotify:track:4iv8y99OCdE2sp3pur0vIS', u'spotify:track:3WRFoIQqOML60XfxFbAXTp', u'spotify:track:7AJZq7MffOI4CECuFneTB3', u'spotify:track:64GRVJkjc5FEIw9jeBEqfp', u'spotify:track:2XFqOvmoiY9x2WIv153W62', u'spotify:track:5YNSKB9gURMMKCgOlCfM30', u'spotify:track:0q0qEV9BeLY6gSiI6dep5V', u'spotify:track:46RGxIXRRgOmnWT3aKXOOG', u'spotify:track:4UUwY667Yn0Kj0QHOfdgWY', u'spotify:track:5qxYyK1HCYpla8OVW6mjkO', u'spotify:track:66RpVMEkgt5Ew7UWL9qswY', u'spotify:track:3nLQQDW3oLjiBKFdTNNsYp', u'spotify:track:5wusiZe1lYYfgfrMZPo3bJ', u'spotify:track:6kP5Cu9ZSyXlzxaocEDUqk', u'spotify:track:3qCi4yADVrL9jCSRbs90ar', u'spotify:track:3vHyrKNvqFvanTgymPXMSN', u'spotify:track:69YGeVgKoqLtaN8jHD1YG5', u'spotify:track:7vfVE2NzjFs3WBglCA5o8Y', u'spotify:track:78VKnpbF3idDcdmnzGccOt', u'spotify:track:1tbI20mVsGiTmDebuEzfG7', u'spotify:track:6OYyiTAs8UH8HfuMYDYVt3', u'spotify:track:2i8AHMx0JmPpqV2cxY55jD', u'spotify:track:1ZS9VXa4UHvQxgEtNslRKs', u'spotify:track:3MsoN4QO0L5euLgTptk1U0', u'spotify:track:5L4Q3WfjF1KUbkwEYWeFrl', u'spotify:track:4Y6Emy4X1i955fgcfs5MOs', u'spotify:track:1cpuqM0SxJAAeiZRZflcH7', u'spotify:track:7uifm47f33Jbt2D34t5S94', u'spotify:track:4br24hxeoLjloGple4Vao4', u'spotify:track:5AXUrzvBrTJKbZjklDnytd', u'spotify:track:0n2EGW8WSzLQESjxEyN2iu', u'spotify:track:6oISPN6Clrwt75JFiQF7aO', u'spotify:track:0rNg50D2j2Aq58V3jqdEuu', u'spotify:track:5BOSoyflOWt7LB1o1t5iOv', u'spotify:track:033eAdPpnmBbgfLvbLBih0', u'spotify:track:7J7D2Ezp32LxlYuNTZX48n', u'spotify:track:07hSIkFnDpOhpb46h475Ss', u'spotify:track:0iX9BV34AHBpdfEMgWm5mU', u'spotify:track:7BLZP3Q291G2iVKKgVRDyj', u'spotify:track:7aH3sZ85qQshN0H5ntgvnO', u'spotify:track:7jnKnxBeSQbcMAuXNmK2vQ', u'spotify:track:1rr9Qt2CjTCOfaFDtcmaOs', u'spotify:track:1tcOkFEX0OiG7BeKMqKDfo', u'spotify:track:7vfVE2NzjFs3WBglCA5o8Y', u'spotify:track:41Dm9KKO3JG9oO5hJj9oRf', u'spotify:track:75yu4dXze1qjPAV6DZcDcn', u'spotify:track:756ZV0boQJ6Kbk3WFBuVjD']
    #         }
    # }
