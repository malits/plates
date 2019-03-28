import bs4 as bs
import requests
import pprint as p

def get_tracks(start, end):
    username = 'maxlitster'
    start = '2019-02-01'
    end = '2019-02-28'

    url = "https://www.last.fm/user/{}/library/tracks?from={}&to={}".format(username, start, end)

    sauce = requests.get(url)
    soup = bs.BeautifulSoup(sauce.content, 'html.parser')

    top_tracks = soup.find_all('span', class_='chartlist-ellipsis-wrap')
    for track in top_tracks:
        print(track.text)



if __name__ == '__main__':
    username = 'maxlitster'
    start = '2019-02-01'
    end = '2019-02-28'
    url = "https://www.last.fm/user/{}/library/tracks?from={}&to={}".format(username, start, end)

    get_tracks(start, end)
