import spotipy
import spotipy.util as util
import track_scraper as scrape
import queue

scopes = "user-read-recently-played playlist-modify-public"

#Replace this with a web interface
username = 'maxlitster'
client_id = '8894010073b04654937bb10b7cb4bdd8'
secret = '66f431a8f8db48c29b0700d15b48b563'
redirect_url = 'https://localhost:8080'

start = '2019-02-01'
end = '2019-02-28'
#Replace with Web Interface

#converts a queue of tracks to spotify song ideas
def tracks_to_ids(track_queue):
    size = track_queue.qsize()
    ids = []

    for i in range(size):

        track = track_queue.get()
        artist = track[0]
        song = track[1]

        current_track = sp.search("track:" + song + " artist:" + artist,
                                    limit=1, type='track')

        #This is very slow and jank in nature. Need to try to fix
        i = 1
        while not current_track['tracks']['items']:
            if i >= len(song):
                current_track = sp.search(song + " " + artist)
                i += 1
            elif i < len(song):
                current_track = sp.search("track:" + song[:-i] + "artist:" + artist,
                                        limit=1, type='track')
                i += 1
            else:
                break

        try:
            ids.append(current_track['tracks']['items'][0]['id'])
        except IndexError:
            pass

    return ids

def configure_playlist(name, public, description):
    #TODO change all test parts
    new_playlist = sp.user_playlist_create(username, 'test', public='True')
    playlist_id = new_playlist['id']

    sp.user_playlist_change_details(username, playlist_id, name='test2')

if __name__ == '__main__':
    token = util.prompt_for_user_token(username, scopes, client_id, secret, redirect_url)
    sp = spotipy.Spotify(auth=token)

    #queue = scrape.get_tracks(username, start, end)

    #ids = tracks_to_ids(queue)

    configure_playlist("test", "test", "test")
