import auth
import playlist
import tracks
import user
import requests
import artists

def main():
    access_token_json = auth.getNewAccessToken()
    access_token = access_token_json['access_token']
    token_type = access_token_json['token_type']

    track_uris = tracks.getTrackUris(access_token, token_type)
    print "trakcs finished"
    user_id = user.getUserId(access_token, token_type)
    print "user_id finished"
    playlist_id = playlist.getPlaylistId(user_id, access_token, token_type)
    print "playlist_id finished"
    playlist.addTracks(user_id, access_token, token_type, track_uris, playlist_id)

main()
