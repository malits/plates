import spotipy
import spotipy.util as util

scopes = "user-read-recently-played playlist-modify-public"

#Replace this with a web interface
username = 'maxlitster'
client_id = '8894010073b04654937bb10b7cb4bdd8'
secret = '66f431a8f8db48c29b0700d15b48b563'
redirect_url = 'https://localhost:8080'
#Replace with Web Interface



if __name__ == '__main__':
    token = util.prompt_for_user_token(username, scopes, client_id, secret, redirect_url)
    sp = spotipy.Spotify(auth=token)
