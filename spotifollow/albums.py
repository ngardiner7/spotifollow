from spotifollow.spotify import client


def getArtistAlbums(next_request, artist_id):
    if(next_request == ''):
        return client.getIntitialArtistAlbums(artist_id)
    else:
        return client.getNextArtistAlbums(next_request)

def getAlbumIds(artist_ids):
    album_ids = []
    for x in range(0, len(artist_ids)):
        next_request = ''

        while (next_request != None):
            artist_albums_data = getArtistAlbums(next_request, artist_ids[x])
            num_albums = len(artist_albums_data['items'])

            for y in range(0, num_albums):
                album_ids.append(artist_albums_data['items'][y]['id'])
            next_request = artist_albums_data['next']
    return album_ids
