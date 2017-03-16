from spotifollow.spotify import client


def get_user_followed_artist():
    after_id = ''
    artists = []
    while after_id is not None:
        artist_data = client.getUserFollowedArtists(after_id)
        artists.extend(artist_data['artists']['items'])
        after_id = artist_data['artists']['cursors']['after']

    return artists


# def getUserImplicitLikedArtists(next_request, access_token, token_type):
#     if(next_request == ''):
#         return client.getInitialUserLikedArtists(access_token, token_type)
#     else:
#         return client.getNextUserLikedArtists(next_request, access_token, token_type)
#
# def getUserImplicitLikedArtistsIds(access_token, token_type):
#     artist_ids = []
#     next_request = ''
#
#     while(next_request != None):
#         artist_data = getUserImplicitLikedArtists(next_request, access_token, token_type)
#         num_tracks = len(artist_data['items'])
#         for x in range(0, num_tracks):
#
#             num_artists = len(artist_data['items'][x]['track']['artists'])
#             for y in range(0, num_artists):
#
#                 artist_ids.append(artist_data['items'][x]['track']['artists'][y]['id'])
#
#         next_request = artist_data['next']
#
#     return artist_ids
#
# def getFrequentUserLikedArtistsIds(access_token, token_type):
#     user_liked_artists_ids = getUserImplicitLikedArtistsIds(access_token, token_type)
#     frequent_user_liked_artists_ids = []
#     for artist_id in user_liked_artists_ids:
#         if(user_liked_artists_ids.count(artist_id) > 1 & frequent_user_liked_artists_ids.count(artist_id) == 0):
#             frequent_user_liked_artists_ids.append(artist_id)
#
#     return frequent_user_liked_artists_ids
#
#
# def getArtistIds(access_token, token_type):
#     all_artist_ids = getUserLikedArtistsIds(access_token, token_type) + getUserImplicitLikedArtistsIds(access_token, token_type)
#     print all_artist_ids
#     print len(list(unique_everseen(all_artist_ids)))
#     return list(unique_everseen(all_artist_ids))
#
