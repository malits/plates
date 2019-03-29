import bs4 as bs
import requests
import queue
import re

#this uses Last.fm... kinda janky. Want to build my own tracker.

#returns a queue containing a users top 50 last.fm tracks over a certain range of dates
def get_tracks(username, start, end):

    url = "https://www.last.fm/user/{}/library/tracks?from={}&to={}".format(username, start, end)

    sauce = requests.get(url)
    soup = bs.BeautifulSoup(sauce.content, 'html.parser')

    #TODO weed out gym music?
    top_tracks = soup.find_all('span', class_='chartlist-ellipsis-wrap')
    tracks = queue.Queue(50)

    for track in top_tracks:
        artist = track.find_all('span', class_='chartlist-artists')[0]
        song = track.find_all('a', class_='link-block-target')[0]

        name_no_space = re.search('(?<=\n)\w[^\n]*', artist.text)

        item = (name_no_space.group(0), song.text)
        tracks.put(item)

    return tracks
